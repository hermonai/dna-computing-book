"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch10"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter10_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not DNA:
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}

    def table(name, headers, rows, fmt):
        lines = [
            r"\begin{tabular}{" + fmt + "}",
            r"\toprule",
            " & ".join(headers) + r"\\",
            r"\midrule",
        ]
        lines += [" & ".join(map(str, row)) + r"\\" for row in rows]
        lines += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / (name + ".tex")] = "\n".join(lines) + "\n"

    def plot(name, data, x, keys):
        styles = ["Blue,thick", "Red,dashed,thick", "Green,dashdotted,thick"]
        lines = []
        for key, style in zip(keys, styles):
            points = " ".join(f"({v[x]:.12g},{v[key]:.12g})" for v in data)
            lines.append(r"\addplot[" + style + "] coordinates {" + points + "};")
        files[BUILD / (name + ".tex")] = "\n".join(lines) + "\n"

    if DNA:
        table(
            "ladder-table",
            ["Length (bp)", "Distance (mm)"],
            [[v["length"], f"{v['distance']:.3f}"] for v in r["ladder"]],
            "rr",
        )
        table(
            "uncertainty-table",
            [r"$\delta$", r"SD of $\widehat n_1$"],
            [[v["delta"], f"{v['sd']:.4f}"] for v in r["uncertainty"]],
            "rr",
        )
        table(
            "window-table",
            ["Half-width (mm)", "Recovery", "Molecular purity"],
            [
                [v["width"], f"{v['recovery']:.4f}", f"{v['purity']:.4f}"]
                for v in r["windows"]
            ],
            "rrr",
        )
        plot("profile-plot", r["profiles"], "x", ["target", "other", "total"])
        plot("window-plot", r["windows"], "width", ["recovery", "purity"])
        selected = [
            "calibrate",
            "infer_length",
            "band_kernel",
            "response_matrix",
            "observe",
            "unmix",
            "roi_summary",
            "collect_window",
        ]
    else:
        table(
            "trace-table",
            ["Token", "Expert", "Gate", "Admitted"],
            [
                [v["token"], v["expert"], v["gate"], "yes" if v["admitted"] else "no"]
                for v in r["trace"]
            ],
            "rrrr",
        )
        table(
            "capacity-table",
            ["Capacity", "Admitted", "Dropped", "Unused slots"],
            [
                [v[k] for k in ("capacity", "admitted", "dropped", "unused")]
                for v in r["sweep"]
            ],
            "rrrr",
        )
        plot("capacity-plot", r["sweep"], "capacity", ["admitted", "dropped", "unused"])
        selected = [
            "plan",
            "expert",
            "dispatch",
            "dense_oracle",
            "balance_loss",
            "sparse_block",
            "cost",
        ]
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
