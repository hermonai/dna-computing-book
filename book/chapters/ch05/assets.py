"""Generate checked tables, plots and literal tested code for the canonical book."""

import ast
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DNA = True  # book identity must survive a checkout directory rename
BUILD = ROOT / "build/generated/ch05"


def derived():
    spec = importlib.util.spec_from_file_location(
        "chapter5_reference", HERE / "reference.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if not DNA:
        module.torch.set_num_threads(1)
    r = module.results()
    files = {HERE / "results.json": json.dumps(r, indent=2) + "\n"}
    if DNA:
        table = [
            r"\begin{tabular}{lll}",
            r"\toprule",
            r"Symbol & Possible bases & Complement symbol\\",
            r"\midrule",
        ]
        for symbol, row in r["ambiguity"].items():
            table.append(f"{symbol} & {row['set']} & {row['complement']}" + r"\\")
        selected = [
            "reverse_complement",
            "reverse_interval",
            "compatible_aligned",
            "expansions",
            "palindrome_count",
        ]
        filename = "ambiguity.tex"
    else:
        table = [
            r"\begin{tabular}{rrrrrr}",
            r"\toprule",
            r"$k$ & $4^k$ & Vocabulary & Disjoint $T$ & Overlap $T$ & Bytes\\",
            r"\midrule",
        ]
        for row in r["vocabulary_rows"]:
            table.append(
                " & ".join(
                    str(row[key])
                    for key in [
                        "k",
                        "full_kmers",
                        "with_tails_and_specials",
                        "disjoint_tokens_1000",
                        "overlap_tokens_1000",
                        "embedding_bytes_d64_float32",
                    ]
                )
                + r"\\"
            )
        selected = [
            "encode_kmer",
            "decode_kmer",
            "tokenize",
            "reconstruct",
            "safe_next_base_examples",
            "embedding_example",
        ]
        filename = "resources.tex"
    table += [r"\bottomrule", r"\end{tabular}"]
    files[BUILD / filename] = "\n".join(table) + "\n"
    source = (HERE / "reference.py").read_text()
    tree = ast.parse(source)
    for name in selected:
        node = next(n for n in tree.body if getattr(n, "name", None) == name)
        files[BUILD / (name + ".py")] = ast.get_source_segment(source, node) + "\n"
    return files
