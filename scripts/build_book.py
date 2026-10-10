"""Assemble the active authored sources into one continuous review candidate.

Frozen editions and chapter sources are not edited. Derived TeX only rewrites
citation keys to an explicit bibliography map; label namespaces are scoped in
the wrapper. A successful build is not visual/scientific acceptance.
"""

import argparse
import importlib.util
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BOOK = "dna-computing"
BUILD = ROOT / "build/book"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bib_items(text):
    """Read the book's simple authored bibitem environments; reject ambiguity."""
    blocks = re.findall(
        r"\\begin\{thebibliography\}\{[^}]*\}(.*?)\\end\{thebibliography\}",
        text,
        flags=re.S,
    )
    items = []
    for block in blocks:
        matches = list(re.finditer(r"\\bibitem\{([^}]+)\}", block))
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(block)
            items.append((match[1], block[match.end() : end].strip()))
    if len({k for k, _ in items}) != len(items):
        raise ValueError("Duplicate bibitem key within one source")
    return items


def strip_bib(text):
    return re.sub(
        r"\\begin\{thebibliography\}\{[^}]*\}.*?\\end\{thebibliography\}",
        "",
        text,
        flags=re.S,
    )


def identity(body):
    """Conservative exact primary identifier matching, not fuzzy title guessing."""
    dois = re.findall(r"https?://doi\.org/([^}\s]+)", body)
    if dois:
        return "doi:" + dois[0].rstrip(".").lower()
    urls = re.findall(r"\\(?:url|href)\{(https?://[^}]+)\}", body)
    if urls:
        # URL paths can be case-sensitive; never merge distinct paths by case.
        return "url:" + urls[0].rstrip("/")
    return "text:" + re.sub(r"\s+", " ", body)


def remap_cites(text, mapping):
    def rewrite(match):
        keys = [k.strip() for k in match[1].split(",")]
        missing = set(keys) - mapping.keys()
        if missing:
            raise ValueError(f"Unresolved citation keys: {sorted(missing)}")
        return r"\cite{" + ",".join(mapping[k] for k in keys) + "}"

    return re.sub(r"\\cite\{([^}]+)\}", rewrite, text)


def chapter_dir(number):
    return ROOT / "book/chapters" / f"ch{number:02d}"


def run(command, cwd=ROOT):
    subprocess.run(
        command,
        cwd=cwd,
        check=True,
        env=dict(
            os.environ,
            OMP_NUM_THREADS="1",
            PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:"
            + os.environ["PATH"],
        ),
    )


def generated_assets(number):
    """Execute the retained numerical generator without a second PDF pipeline."""
    directory = chapter_dir(number)
    spec = importlib.util.spec_from_file_location(
        f"assets_ch{number:02d}", directory / "assets.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.derived()


def prepare(through, refresh, check=False):
    BUILD.mkdir(parents=True, exist_ok=True)
    deep = ROOT / "build/figures"
    deep.mkdir(parents=True, exist_ok=True)
    svgs = [
        p
        for number in range(1, through + 1)
        for p in sorted((chapter_dir(number) / "figures").glob("*.svg"))
    ]
    for source in svgs:
        output = deep / (source.stem + ".pdf")
        if not check and (
            refresh
            or not output.exists()
            or source.stat().st_mtime > output.stat().st_mtime
        ):
            run(["rsvg-convert", "-f", "pdf", "-o", str(output), str(source)])
    for number in range(4, through + 1):
        directory = chapter_dir(number)
        if not (directory / "manuscript.tex").is_file():
            raise ValueError(f"Active manuscript missing: chapter {number}")
        for path, value in generated_assets(number).items():
            if path == directory / "results.json" or check:
                if not path.is_file() or path.read_text() != value:
                    raise ValueError(
                        f"Computed asset differs from reference: {path.relative_to(ROOT)}"
                    )
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(value)
    return svgs


def assemble(through):
    opening = ROOT / "book/backmatter/opening-sources.tex"
    opening_items = bib_items(opening.read_text())
    entries = {}
    seen = {}
    provenance = []
    for key, body in opening_items:
        entries[key] = body
        # Preserve the frozen opening's key references even if identifiers repeat.
        seen.setdefault(identity(body), key)
        provenance.append(
            {
                "source": str(opening.relative_to(ROOT)),
                "original_key": key,
                "book_key": key,
            }
        )
    wrappers = [
        rf"\input{{chapters/ch{number:02d}/manuscript.tex}}" for number in range(1, 4)
    ]
    for number in range(4, through + 1):
        directory = chapter_dir(number)
        source_file = directory / "sources.tex"
        source = source_file.read_text()
        items = bib_items(source)
        mapping = {}
        for key, body in items:
            ident = identity(body)
            book_key = seen.get(ident, f"ch{number:02d}:{key}")
            seen[ident] = book_key
            # Current later record supersedes earlier display metadata for the
            # same exact identifier, retaining all contributing source records.
            entries[book_key] = body
            mapping[key] = book_key
            provenance.append(
                {
                    "source": str(source_file.relative_to(ROOT)),
                    "original_key": key,
                    "book_key": book_key,
                    "matched_identifier": ident,
                }
            )
        out = BUILD / f"ch{number:02d}"
        out.mkdir(parents=True, exist_ok=True)

        def rewrite_local_inputs(text):
            def replace(match):
                target = match[1]
                if (directory / target).is_file():
                    return rf"\input{{../build/book/ch{number:02d}/{target}}}"
                return match[0]

            return re.sub(r"\\input\{([^}]+)\}", replace, text)

        for authored in directory.glob("*.tex"):
            if authored.name in ("review.tex", "sources.tex"):
                continue
            text = authored.read_text()
            if number == 4 and authored.name == "manuscript.tex":
                # Layout-only soft breakpoint in a narrow table cell. The
                # authored source and scientific text are kept unchanged.
                text = text.replace(
                    "Concentration/volume", r"Concentration/\allowbreak volume"
                )
            (out / authored.name).write_text(
                rewrite_local_inputs(remap_cites(text, mapping))
            )
        (out / "evidence.tex").write_text(remap_cites(strip_bib(source), mapping))
        figures = out / "figures"
        figures.mkdir(exist_ok=True)
        for figure in sorted((directory / "figures").glob("*.tex")):
            (figures / figure.name).write_text(remap_cites(figure.read_text(), mapping))
        wrappers.extend(
            [
                r"\clearpage\begingroup",
                rf"\def\ChapterNamespace{{ch{number:02d}:}}",
                rf"\def\Generated{{../build/generated/{directory.name}}}",
                rf"\def\PlateDirectory{{../build/book/ch{number:02d}/figures}}",
                r"\ScopedChapterLabels",
                rf"\input{{../build/book/ch{number:02d}/manuscript.tex}}",
                rf"\input{{../build/book/ch{number:02d}/evidence.tex}}",
                r"\clearpage\endgroup",
            ]
        )
    (BUILD / "chapters.tex").write_text("\n".join(wrappers) + "\n")
    bibliography = [
        r"\begin{thebibliography}{999}",
        r"\addcontentsline{toc}{chapter}{Bibliography}",
    ]
    bibliography += [rf"\bibitem{{{k}}} {v}" for k, v in entries.items()]
    bibliography.append(r"\end{thebibliography}")
    (BUILD / "bibliography.tex").write_text("\n\n".join(bibliography) + "\n")
    (BUILD / "bibliography-map.json").write_text(
        json.dumps(provenance, indent=2) + "\n"
    )
    (BUILD / "scope.tex").write_text(rf"\def\IncludedThrough{{{through}}}" + "\n")
    return provenance


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--through", type=int, default=32)
    parser.add_argument("--refresh-assets", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--check-assets", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "book/book.json").read_text())
    expected = [f"book/chapters/ch{n:02d}/manuscript.tex" for n in range(1, 33)]
    if (
        manifest.get("title") != "DNA Computing"
        or [c.get("number") for c in manifest.get("chapters", [])] != list(range(1, 33))
        or [c.get("source") for c in manifest["chapters"]] != expected
    ):
        raise ValueError(
            "Current manifest must contain exactly the canonical Chapters 1–32"
        )
    maximum = 32 if BOOK == "dna-computing" else 52
    if not 4 <= args.through <= maximum:
        parser.error(f"--through must be between 4 and {maximum}")
    prepare(args.through, args.refresh_assets, check=args.check_assets)
    if args.check_assets:
        print(
            f"Computed results, tables, plots and literal listings verified through Chapter {args.through}."
        )
        return
    provenance = assemble(args.through)
    if args.prepare_only:
        print("Derived chapter wrappers and consolidated bibliography prepared.")
        return
    name = BOOK
    command = [
        "latexmk",
        "-xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-outdir=../build/book",
        "main.tex",
        "-jobname=" + name,
    ]
    result = subprocess.run(
        command,
        cwd=ROOT / "book",
        capture_output=True,
        text=True,
        env=dict(
            os.environ,
            PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:"
            + os.environ["PATH"],
        ),
    )
    (BUILD / "console.log").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError((result.stdout + result.stderr)[-6000:])
    # Regenerate explicitly: a stale .ind can survive host latexmk defaults.
    index = subprocess.run(
        ["makeindex", "-o", name + ".ind", name + ".idx"],
        cwd=BUILD,
        env=dict(os.environ, PATH="/Library/TeX/texbin:" + os.environ["PATH"]),
        capture_output=True,
        text=True,
        check=True,
    )
    rerun = subprocess.run(
        result.args,
        cwd=ROOT / "book",
        env=dict(os.environ, PATH="/Library/TeX/texbin:" + os.environ["PATH"]),
        capture_output=True,
        text=True,
    )
    with (BUILD / "console.log").open("a") as stream:
        stream.write(index.stdout + index.stderr + rerun.stdout + rerun.stderr)
    if rerun.returncode:
        raise RuntimeError((rerun.stdout + rerun.stderr)[-6000:])
    log = (BUILD / (name + ".log")).read_text()
    failures = [
        line
        for line in log.splitlines()
        if any(
            s in line
            for s in (
                "Overfull",
                "Missing character:",
                "undefined references",
                "multiply defined",
                "LaTeX Warning: Reference",
                "LaTeX Warning: Citation",
            )
        )
    ]
    (BUILD / "warning-audit.json").write_text(
        json.dumps({"release_blocking_warnings": failures}, indent=2) + "\n"
    )
    if failures:
        raise RuntimeError("\n".join(failures))
    output = ROOT / "output/pdf" / (name + ".pdf")
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUILD / (name + ".pdf"), output)
    info = subprocess.check_output(["pdfinfo", str(output)], text=True)
    paths = list((ROOT / "book").rglob("*")) + [Path(__file__)]
    paths = [p for p in paths if p.is_file() and "__pycache__" not in p.parts]
    paths += [p for p in (ROOT / "tests").glob("*.py")]
    paths += [ROOT / "Makefile", ROOT / "pyproject.toml"]
    for number in range(4, args.through + 1):
        paths.extend(
            p
            for p in chapter_dir(number).rglob("*")
            if p.is_file() and "__pycache__" not in p.parts
        )
    record = {
        "book": BOOK,
        "through": args.through,
        "status": "canonical authored-source manuscript; publication review pending",
        "complete_planned_range": args.through == maximum,
        "pdf": str(output.relative_to(ROOT)),
        "pages": int(re.search(r"Pages:\s+(\d+)", info)[1]),
        "pdf_sha256": sha(output),
        "bibliography_contributions": len(provenance),
        "source_hashes": {str(p.relative_to(ROOT)): sha(p) for p in sorted(set(paths))},
    }
    (BUILD / "build-record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(
        json.dumps({k: v for k, v in record.items() if k != "source_hashes"}, indent=2)
    )


if __name__ == "__main__":
    main()
