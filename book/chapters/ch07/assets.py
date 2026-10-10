"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch07"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter7_reference", HERE / "reference.py"
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
        plot("kinetics-plot", r["curves"], "t", ["normal_nm", "fast_nm"])
        trace = [{"t": t, "d": d} for t, d in r["trace"]]
        trace.append({"t": 120, "d": trace[-1]["d"]})
        plot("events-plot", trace, "t", ["d"], ["Blue,thick,const plot"])
        plot(
            "distribution-plot",
            [{"d": i, "p": p} for i, p in enumerate(r["stationary"])],
            "d",
            ["p"],
            ["Blue,ybar,fill=Blue!25,bar width=7pt"],
        )
        rows = [
            r"\begin{tabular}{rr}",
            r"\toprule",
            r"Maximum step (s) & Absolute error (nM)\\",
            r"\midrule",
        ]
        for row in r["convergence"]:
            rows.append(f"{row['step']:g} & {row['error_nm']:.8f}" + r"\\")
        selected = [
            "fluxes",
            "equal_pool_exact",
            "rk4",
            "propensities",
            "ssa",
            "stationary",
        ]
    else:
        plot("memory-plot", r["memory_curve"], "step", ["fast", "slow"])
        rows = [
            r"\begin{tabular}{rrrrrr}",
            r"\toprule",
            r"$t$ & $a_t$ & $b_t$ & $P_t$ & $Q_t$ & $h_t$\\",
            r"\midrule",
        ]
        for row in r["trace"]:
            rows.append(
                " & ".join(
                    f"{row[k]:g}"
                    for k in [
                        "t",
                        "a",
                        "b",
                        "prefix_a",
                        "prefix_b",
                        "state",
                    ]
                )
                + r"\\"
            )
        selected = [
            "compose",
            "sequential",
            "prefix_pairs",
            "parallel_form",
            "zoh",
            "selected_coefficients",
            "convolution_form",
        ]
    rows += [r"\bottomrule", r"\end{tabular}"]
    files[BUILD / "results-table.tex"] = "\n".join(rows) + "\n"
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
