"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch04"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter4_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not DNA:
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}
    if DNA:
        table = [
            r"\begin{tabular}{rrrr}",
            r"\toprule",
            r"$n$ & $(n-2)!$ orders & Copies, 99\% & Volume at 1 nM (L)\\",
            r"\midrule",
        ]
        for row in r["resource_table"]:
            table.append(
                f"{row['vertices']} & {row['candidate_orders']:.3e} & {row['copies_99pct_one_witness']:.3e} & {row['litres']:.3e}"
                + r"\\"
            )
        table += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / "resources.tex"] = "\n".join(table) + "\n"
        plot = []
        for key, style in [
            ("independent", "blue,mark=*"),
            ("shared_failure_10pct", "red,dashed,mark=square*"),
        ]:
            pts = " ".join(
                f"({row['copies']},{row[key]:.12g})" for row in r["miss_curves"]
            )
            plot.append(r"\addplot[" + style + "] coordinates {" + pts + "};")
        files[BUILD / "miss-plot.tex"] = "\n".join(plot) + "\n"
        selected = ["required_copies", "finite_pool_miss", "inventory"]
    else:
        table = [
            r"\begin{tabular}{rrrr}",
            r"\toprule",
            r"Update & Epoch & Targets & Training loss\\",
            r"\midrule",
        ]
        for row in r["training"]:
            table.append(
                f"{row['update']} & {row['epoch']} & {row['scored_targets']} & {row['loss']:.6f}"
                + r"\\"
            )
        table += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / "training.tex"] = "\n".join(table) + "\n"
        table = [
            r"\begin{tabular}{lrrr}",
            r"\toprule",
            r"Restored state & Max.\ error & Same rows? & Same losses?\\",
            r"\midrule",
        ]
        for key, row in r["restart"].items():
            table.append(
                key.replace("_", r"\_")
                + f" & {row['max_parameter_error']:.6f} & "
                + ("yes" if row["same_batch_trace"] else "no")
                + " & "
                + ("yes" if row["same_loss_trace"] else "no")
                + r"\\"
            )
        table += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / "restart.tex"] = "\n".join(table) + "\n"
        selected = [
            "collate",
            "masked_loss",
            "Run.step",
            "Run.checkpoint",
            "Run.restore",
        ]
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        nodes = tree.body
        for part in name.split("."):
            node = next(n for n in nodes if getattr(n, "name", None) == part)
            nodes = getattr(node, "body", [])
        segment = ast.get_source_segment(source, node)
        # ast excludes a method's decorator; the printed restore listing declares it.
        if name == "Run.restore":
            segment = "@classmethod\n" + segment
        import textwrap

        segment = textwrap.dedent(segment)
        files[BUILD / (name.replace(".", "-") + ".py")] = segment + "\n"
    return files
