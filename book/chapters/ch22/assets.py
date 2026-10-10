"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch22"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter22_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if hasattr(module, "torch"):
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}
    grid = [r"\draw[fill=Gold!60] (0,0) rectangle (1,1);"]
    for i in range(1, r["n"] + 1):
        grid += [
            rf"\draw[fill=Gold!60] ({i},0) rectangle ++(1,1);",
            rf"\node at ({i + 0.5},.5) {{{1 if i == 1 else 0}}};",
            rf"\draw[fill=Gold!60] (0,{i}) rectangle ++(1,1);",
            rf"\node at (.5,{i + 0.5}) {{0}};",
        ]
    for y, row in enumerate(r["grid"], 1):
        for x, bit in enumerate(row, 1):
            grid += [
                rf"\draw[fill={'Blue' if bit else 'Pale'}] ({x},{y}) rectangle ++(1,1);",
                rf"\node[text={'white' if bit else 'black'}] at ({x + 0.5},{y + 0.5}) {{{bit}}};",
            ]
    files[BUILD / "xor-grid.tex"] = "\n".join(grid) + "\n"

    def table(name, headers, rows, fmt):
        lines = [
            r"\begin{tabular}{" + fmt + "}",
            r"\toprule",
            " & ".join(headers) + r"\\",
            r"\midrule",
        ]
        lines += [
            " & ".join(
                (f"{v:.6g}" if isinstance(v, float) else str(v)).replace("_", r"\_")
                for v in row
            )
            + r"\\"
            for row in rows
        ]
        lines += [r"\bottomrule", r"\end{tabular}"]
        files[BUILD / (name + ".tex")] = "\n".join(lines) + "\n"

    def plot(name, data, x, keys):
        styles = [
            "Blue,thick",
            "Red,dashed,thick",
            "Green,dashdotted,thick",
        ]
        lines = []
        for key, style in zip(keys, styles):
            if key == "path":
                style += ",const plot"
            points = " ".join(f"({v[x]:.12g},{v[key]:.12g})" for v in data)
            lines.append(r"\addplot[" + style + "] coordinates {" + points + "};")
        files[BUILD / (name + ".tex")] = "\n".join(lines) + "\n"

    for name, headers, keys, fmt in module.TABLES:
        table(name, headers, [[v[k] for k in keys] for v in r[name]], fmt)
    for name, key, x, ys in module.PLOTS:
        plot(name, r[key], x, ys)
    selected = module.LISTINGS
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        first = min(
            [node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])]
        )
        files[BUILD / (name + ".py")] = (
            "\n".join(source.splitlines()[first - 1 : node.end_lineno]) + "\n"
        )
    return files
