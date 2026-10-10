"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch06"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter6_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not DNA:
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}
    if DNA:
        first = r["sequence_comparison"][0]
        energy = [first["dh_kcal"], -310.15 * first["ds_cal"] / 1000]
        energy.append(sum(energy))
        files[BUILD / "energy-plot.tex"] = (
            "\n".join(
                r"\addplot[ybar,bar width=18pt,fill="
                + color
                + r",draw=none,nodes near coords,point meta=explicit symbolic,nodes near coords style={anchor="
                + ("north" if value < 0 else "south")
                + r",font=\small}] coordinates {("
                + f"{i},{value:.9f}) [{value:+.3f}]"
                + "};"
                for i, (value, color) in enumerate(
                    zip(energy, ["Blue", "Gold", "Green"])
                )
            )
            + "\n"
        )
        rows = [
            r"\begin{tabular}{lrrrr}",
            r"\toprule",
            r"Sequence & $\Delta H^\circ$ & $\Delta S^\circ$ & $K_d$ (nM) & $T_m$ ($^\circ$C)\\",
            r"\midrule",
        ]
        for v in r["sequence_comparison"]:
            rows.append(
                f"{v['sequence']} & {v['dh_kcal']:.1f} & {v['ds_cal']:.1f} & {v['kd_37_m'] * 1e9:.3f} & {v['tm_100nm_c']:.2f}"
                + r"\\"
            )
        selected = [
            "duplex_molar",
            "kd_from_thermo",
            "nn_parameters",
            "melting_kelvin",
        ]
        nn = [
            r"\begin{tabular}{lrr}",
            r"\toprule",
            r"Upper step & $\Delta H^\circ$ (kcal/mol) & $\Delta S^\circ$ (cal/mol/K)\\",
            r"\midrule",
        ]
        for key, (h, s) in r["nn_table"].items():
            nn.append(f"{key} & {h:.1f} & {s:.1f}" + r"\\")
        nn += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / "parameters.tex"] = "\n".join(nn) + "\n"
        for name, data, x, keys in [
            (
                "binding",
                r["concentration_curve"],
                "b_nm",
                ["exact_fraction", "excess_approximation"],
            ),
            (
                "melting",
                r["melting_curve"],
                "celsius",
                ["10", "100", "1000"],
            ),
        ]:
            lines = []
            for key, style in zip(
                keys,
                [
                    "Blue,thick",
                    "Red,dashed,thick",
                    "Green,dashdotted,thick",
                ],
            ):
                points = " ".join(f"({v[x]},{v[key]:.10g})" for v in data)
                lines.append(r"\addplot[" + style + "] coordinates {" + points + "};")
            files[BUILD / (name + "-plot.tex")] = "\n".join(lines) + "\n"
    else:
        rows = [
            r"\begin{tabular}{lrrl}",
            r"\toprule",
            r"Boundary policy & Final state & $\partial h_4/\partial a$ & $\partial h_4/\partial x$\\",
            r"\midrule",
        ]
        for name, v in r["chunks"].items():
            grad = ", ".join(f"{a:g}" for a in v["input_gradient"])
            rows.append(
                f"{name} & {v['final']:.3f} & {v['parameter_gradient']:.3f} & [{grad}]"
                + r"\\"
            )
        selected = ["gru_step", "lstm_step", "scan_gru", "chunk_experiment"]
        lines = []
        for z, style in zip(
            [0.5, 0.9, 0.99],
            ["Blue,thick", "Red,dashed,thick", "Green,dashdotted,thick"],
        ):
            points = " ".join(f"({n},{z**n:.10g})" for n in range(0, 101, 2))
            lines.append(r"\addplot[" + style + "] coordinates {" + points + "};")
        files[BUILD / "retention-plot.tex"] = "\n".join(lines) + "\n"
    rows += [r"\bottomrule", r"\end{tabular}"]
    files[BUILD / "results-table.tex"] = "\n".join(rows) + "\n"
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
