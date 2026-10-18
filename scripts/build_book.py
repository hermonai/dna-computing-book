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


CITE = re.compile(r"\\cite[pt]?(?:\[[^\]]*\])?\{([^}]+)\}")
BIB = ROOT / "book/backmatter/references.bib"


def bib_keys(text=None):
    """Keys of the single authored BibTeX database; duplicates are an error."""
    text = BIB.read_text() if text is None else text
    keys = re.findall(r"^@\w+\{([^,\s]+),", text, flags=re.M)
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate BibTeX key in references.bib")
    return set(keys)


def cited_keys(text):
    return [k.strip() for m in CITE.finditer(text) for k in m[1].split(",")]


def citation_map():
    """Map every cited key to the book sources that cite it; fail closed."""
    keys = bib_keys()
    used = {}
    for path in sorted((ROOT / "book").rglob("*.tex")):
        for key in cited_keys(path.read_text()):
            if key not in keys:
                raise ValueError(f"Unresolved citation key {key} in {path.relative_to(ROOT)}")
            used.setdefault(key, set()).add(str(path.relative_to(ROOT)))
    return {k: sorted(v) for k, v in sorted(used.items())}


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
    manifest = json.loads((ROOT / "book/book.json").read_text())
    parts = {p["first_chapter"]: p for p in manifest.get("parts", [])}
    wrappers = []
    for number in range(1, through + 1):
        if number in parts:
            wrappers.append(rf"\input{{{Path(parts[number]['source']).relative_to('book')}}}")
        if number <= 3:
            wrappers.append(rf"\input{{chapters/ch{number:02d}/manuscript.tex}}")
            continue
        directory = chapter_dir(number)
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
            if authored.name == "review.tex":
                continue
            text = authored.read_text()
            if number == 4 and authored.name == "manuscript.tex":
                # Layout-only soft breakpoint in a narrow table cell.
                text = text.replace(
                    "Concentration/volume", r"Concentration/\allowbreak volume"
                )
            (out / authored.name).write_text(rewrite_local_inputs(text))
        figures = out / "figures"
        figures.mkdir(exist_ok=True)
        for figure in sorted((directory / "figures").glob("*.tex")):
            (figures / figure.name).write_text(figure.read_text())
        wrappers.extend(
            [
                r"\clearpage\begingroup",
                rf"\def\ChapterNamespace{{ch{number:02d}:}}",
                rf"\def\Generated{{../build/generated/{directory.name}}}",
                rf"\def\PlateDirectory{{../build/book/ch{number:02d}/figures}}",
                r"\ScopedChapterLabels",
                rf"\input{{../build/book/ch{number:02d}/manuscript.tex}}",
                rf"\input{{../build/book/ch{number:02d}/sources.tex}}",
                r"\clearpage\endgroup",
            ]
        )
    (BUILD / "chapters.tex").write_text("\n".join(wrappers) + "\n")
    cmap = citation_map()
    (BUILD / "citation-map.json").write_text(json.dumps(cmap, indent=2) + "\n")
    (BUILD / "scope.tex").write_text(rf"\def\IncludedThrough{{{through}}}" + "\n")
    return cmap


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
        print("Derived chapter wrappers and citation map prepared.")
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
            BIBINPUTS=str(ROOT / "book") + ":",
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
        env=dict(
            os.environ,
            PATH="/Library/TeX/texbin:" + os.environ["PATH"],
            BIBINPUTS=str(ROOT / "book") + ":",
        ),
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
                "Package natbib Warning",
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
    blg = (BUILD / (name + ".blg")).read_text()
    if "Warning--" in blg or "error message" in blg:
        raise RuntimeError("BibTeX reported problems:\n" + blg[-3000:])
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
        "cited_works": len(provenance),
        "source_hashes": {str(p.relative_to(ROOT)): sha(p) for p in sorted(set(paths))},
    }
    (BUILD / "build-record.json").write_text(json.dumps(record, indent=2) + "\n")
    print(
        json.dumps({k: v for k, v in record.items() if k != "source_hashes"}, indent=2)
    )


if __name__ == "__main__":
    main()
