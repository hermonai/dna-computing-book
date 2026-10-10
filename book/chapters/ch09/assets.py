"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch09"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter9_reference", HERE / "reference.py"
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
            "lineage-table",
            [
                r"$n$",
                "All duplexes",
                "One-end strands",
                "Exact strands",
                "Exact duplexes",
            ],
            [
                [
                    v[k]
                    for k in ("cycle", "duplexes", "one_end", "exact", "exact_duplexes")
                ]
                for v in r["lineage"]
            ],
            "rrrrr",
        )
        table(
            "budget-table",
            ["Cycle", r"$N$", r"$F$", r"$R$", r"$B$"],
            [
                [f"{v[k]:g}" for k in ("cycle", "n", "forward", "reverse", "dntp")]
                for v in r["budget"]
            ],
            "rrrrr",
        )
        table(
            "threshold-table",
            [r"$N_0$", r"$C_q$"],
            [[v["initial"], f"{v['cq']:.4f}"] for v in r["thresholds"]],
            "rr",
        )
        table(
            "sampling-table",
            [r"$\lambda$", "Empty probability"],
            [[v["mean"], f"{v['empty']:.4f}"] for v in r["sampling"]],
            "rr",
        )
        plot("growth-plot", r["growth"], "cycle", ["ideal", "reduced", "bounded"])
        plot("bias-plot", r["bias"], "cycle", ["ratio"])
        plot("signal-plot", r["signal"], "cycle", ["low", "high"])
        selected = [
            "primer_pair",
            "lineage",
            "amplify",
            "budgeted",
            "branching_moments",
            "cq",
            "efficiency_from_slope",
        ]
    else:
        table(
            "position-table",
            [r"$t$", r"$\sin t$", r"$\cos t$", r"$\sin(0.01t)$", r"$\cos(0.01t)$"],
            [[i] + [f"{v:.5f}" for v in row] for i, row in enumerate(r["positions"])],
            "rrrrr",
        )
        table(
            "training-table",
            ["Step", "Mean target loss"],
            [
                [v["step"], f"{v['loss']:.6f}"]
                for v in r["training"]
                if v["step"] % 10 == 0
            ],
            "rr",
        )
        plot("training-plot", r["training"], "step", ["loss"])
        selected = [
            "layer_norm",
            "norm_vjp",
            "positions",
            "multihead",
            "feed_forward",
            "block",
            "model",
            "next_token_loss",
            "training_trace",
        ]
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
