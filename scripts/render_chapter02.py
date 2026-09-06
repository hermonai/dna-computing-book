"""Render the canonical polarity graph, deriving paired rows from the model."""
from pathlib import Path
import sys
from svg_primitives import Canvas, BLUE

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code/minidna"))
from minidna.duplex import Duplex


def svg(meta, nodes, edges):
    if set(nodes) != {"n1", "n2", "n3"} or [(a, b, k) for a, b, k, _ in edges] != [
            ("n1", "n2", "DATA"), ("n2", "n3", "DATA")]:
        raise ValueError("unsupported polarity graph contract")
    duplex = Duplex.from_sequence(meta["SEQUENCE"])
    if len(duplex.top) != 4:
        raise ValueError("chapter figure requires four nucleotide positions")
    top, aligned = duplex.rows()
    for node, row in zip(("n1", "n2", "n3"), (str(top), str(aligned), str(duplex.bottom))):
        if row.replace("'", "′") not in nodes[node][1]:
            raise ValueError("TXT row disagrees with computed orientation")
    c = Canvas(meta)
    c.text(30, 35, meta["ID"] + " / MOLECULAR REPRESENTATION", 15, True, color=BLUE)
    c.text(30, 78, meta["TITLE"], 29, True)
    c.text(30, 111, meta["SUBTITLE"], 17)
    c.box(25, 140, 950, 370, "#fbfdff")
    c.text(45, 172, "A. Paired view: four aligned positions", 21, True)
    c.path("M190,195 H825", marker="arrow", width=1.6)
    c.text(850, 200, "5′ to 3′", 16)
    c.path("M160,230 H840", width=4)
    c.path("M160,405 H840", width=4)
    for x, base, partner in zip((300, 430, 560, 690), top.sequence, aligned.sequence):
        for y in (230, 405):
            c.circle(x, y, 14, "#e9edf0")
            c.text(x, y + 6, "S", 16, anchor="middle")
        c.path(f"M{x},244 V255")
        c.path(f"M{x},375 V391")
        c.box(x - 28, 255, 56, 45, "#dceef8", 7)
        c.box(x - 28, 330, 56, 45, "#e3eee5", 7)
        c.text(x, 285, base, 25, True, "middle")
        c.text(x, 360, partner, 25, True, "middle")
        offsets = (-5, 5) if base in "AT" else (-9, 0, 9)
        for offset in offsets:
            c.path(f"M{x+offset},302 V328", dashed=True, width=1.4)
    for x, y, label in ((112, 238, "5′"), (875, 238, "3′"), (112, 413, "3′"), (875, 413, "5′")):
        c.text(x, y, label, 27, True)
    c.path("M825,440 H190", marker="arrow", width=1.6)
    c.text(850, 445, "5′ to 3′", 16)
    c.text(45, 482, "S: sugar symbol   |   solid backbone: covalent chain   |   dashed: pairing contacts", 17)
    c.box(25, 535, 950, 175, "#f3f7f2")
    c.text(45, 572, "B. Rewrite the lower strand from its 5′ end", 21, True)
    c.text(60, 619, str(aligned).replace("'", "′"), 27, True)
    c.path("M340,610 H565", marker="arrow")
    c.text(453, 645, "read right to left", 17, anchor="middle")
    c.text(625, 619, str(duplex.bottom).replace("'", "′"), 27, True)
    c.text(45, 682, "Same partner, different written order. No synthesis or chemical reversal is shown.", 18)
    c.lines(30, 753, "READING: " + meta["READING"], width=96, size=16, step=22)
    c.lines(30, 814, "BOUNDARY: " + meta["FAILURE"], width=96, size=16, step=22)
    return c.finish()


def render_chapter02(path, meta, nodes, edges):
    target = ROOT / "book/figures" / (path.stem + ".svg")
    target.write_text(svg(meta, nodes, edges))
    return target
