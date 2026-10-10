"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch08"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter8_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not DNA:
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}

    def plot(name, data, x, keys, styles=None):
        styles = styles or [
            "Blue,thick",
            "Red,dashed,thick",
            "Green,dashdotted,thick",
        ]
        lines = []
        for key, style in zip(keys, styles):
            points = " ".join(f"({v[x]:.12g},{v[key]:.12g})" for v in data)
            lines.append(r"\addplot[" + style + "] coordinates {" + points + "};")
        files[BUILD / (name + ".tex")] = "\n".join(lines) + "\n"

    if DNA:
        plot("rate-plot", r["substrate_curve"], "s", ["v"])
        plot(
            "transient-plot",
            r["transient"],
            "t",
            ["complex_nm", "clamped_nm"],
        )
        rows = [
            r"\begin{tabular}{rr}",
            r"\toprule",
            r"$s$ ($\mu$M) & $v$ ($\mu$M/s)\\",
            r"\midrule",
        ]
        rows += [f"{v['s']:g} & {v['v']:.6f}" + r"\\" for v in r["rates"]]
        selected = [
            "ecori_cut_sites",
            "seal_nick",
            "extend_primer",
            "rhs",
            "integrate",
            "clamped",
            "mm_rate",
        ]
    else:
        rows = [
            r"\begin{tabular}{rrrr}",
            r"\toprule",
            r"$T$ & Dense score cells & Causal pairs & KV scalars\\",
            r"\midrule",
        ]
        rows += [
            " & ".join(
                str(v[k]) for k in ["t", "score_cells", "causal_pairs", "kv_scalars"]
            )
            + r"\\"
            for v in r["work"]
        ]
        for name in ["packed_mask", "offset_mask", "wrong_upper_left"]:
            cells = []
            for i, row in enumerate(r[name]):
                for j, val in enumerate(row):
                    fill = "Blue!15" if val else "white"
                    label = r"$\bullet$" if val else r"$\times$"
                    cells.append(
                        rf"\node[draw=gray!50,fill={fill},minimum width=.64cm,"
                        rf"minimum height=.55cm,inner sep=0pt] at ({j * 0.64},{-i * 0.55}) {{{label}}};"
                    )
            files[BUILD / (name + ".tex")] = "\n".join(cells) + "\n"
        selected = [
            "packed_mask",
            "masked_softmax",
            "attention",
            "offset_mask",
            "cached_chunk",
            "split_heads",
            "merge_heads",
        ]
    rows += [r"\bottomrule", r"\end{tabular}"]
    files[BUILD / "results-table.tex"] = "\n".join(rows) + "\n"
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
