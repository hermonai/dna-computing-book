"""Literal sequence and graph contracts, not a thermodynamic designer."""

from itertools import combinations

BASES = "ACGT"
CODE = {"A": "AACGTCAG", "B": "CCTAGTCA", "C": "GATCTGAC", "D": "TGCACAGT"}
EDGES = {
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "B"),
    ("B", "D"),
    ("C", "D"),
}
LISTINGS = [
    "revcomp",
    "hamming",
    "longest_match",
    "hairpins",
    "choose_library",
    "encode_edges",
    "assemble",
    "decode",
]


def dna(s):
    if not isinstance(s, str) or not s or set(s) - set(BASES):
        raise ValueError("nonempty uppercase unambiguous DNA required")
    return s


def revcomp(s):
    """Both input and output are written 5-prime to 3-prime."""
    return dna(s).translate(str.maketrans("ACGT", "TGCA"))[::-1]


def hamming(a, b):
    dna(a), dna(b)
    if len(a) != len(b):
        raise ValueError("equal lengths required")
    return sum(x != y for x, y in zip(a, b))


def longest_match(a, b):
    """Longest contiguous exact common word; positions in written strings."""
    dna(a), dna(b)
    previous, best = [0] * (len(b) + 1), (0, 0, 0)
    for i, x in enumerate(a):
        current = [0] * (len(b) + 1)
        for j, y in enumerate(b):
            if x == y:
                current[j + 1] = previous[j] + 1
                size = current[j + 1]
                if size > best[0]:
                    best = (size, i + 1 - size, j + 1 - size)
        previous = current
    return best  # length, start in a, start in b


def hairpins(s, stem=3, loop=3):
    """Exact inverted-repeat warnings, not folding predictions."""
    dna(s)
    if type(stem) is not int or stem < 1:
        raise ValueError("positive integer stem length required")
    if type(loop) is not int or loop < 0:
        raise ValueError("nonnegative integer minimum loop required")
    return [
        (i, j)
        for i in range(len(s) - stem + 1)
        for j in range(i + stem + loop, len(s) - stem + 1)
        if s[i : i + stem] == revcomp(s[j : j + stem])
    ]


def choose_library(candidates, count, distance=3, cross_run=4):
    """Exhaustive small-library certificate for exactly these screens."""
    candidates = tuple(sorted(set(candidates)))
    if type(count) is not int or count < 1:
        raise ValueError("positive integer count required")
    if any(type(v) is not int or v < 0 for v in (distance, cross_run)):
        raise ValueError("nonnegative integer screen limits required")
    lengths = {len(dna(s)) for s in candidates}
    if len(lengths) > 1:
        raise ValueError("equal-length candidates required")
    good = [
        s
        for s in candidates
        if 0.375 <= (s.count("G") + s.count("C")) / len(s) <= 0.625
        and not any(b * 3 in s for b in BASES)
        and not hairpins(s)
        and hamming(s, revcomp(s)) >= distance
    ]
    for subset in combinations(good, count):
        if all(
            hamming(a, b) >= distance
            and hamming(a, revcomp(b)) >= distance
            and longest_match(a, revcomp(b))[0] <= cross_run
            for a, b in combinations(subset, 2)
        ):
            return subset
    return None


def encode_edges(code, edges):
    """Half-domain edge words; no endpoint exceptions in this toy codec."""
    words = [dna(s) for s in code.values()]
    if not words or len({len(s) for s in words}) != 1:
        raise ValueError("nonempty equal-width code required")
    width = len(words[0])
    if width % 2:
        raise ValueError("even word width required")
    half = width // 2
    domains = [d for s in words for d in (s[:half], s[half:])]
    if len(set(domains)) != len(domains):
        raise ValueError("this codec requires distinct half-domains")
    if any(u not in code or v not in code for u, v in edges):
        raise ValueError("edge endpoint missing from code")
    return {(u, v): code[u][half:] + code[v][:half] for u, v in edges}


def assemble(path, code, edges):
    """Digital concatenation specification, not a ligation simulator."""
    library = encode_edges(code, edges)
    if not path or any(v not in code for v in path):
        raise ValueError("nonempty path on known vertices required")
    half = len(next(iter(code.values()))) // 2
    if any((u, v) not in library for u, v in zip(path, path[1:])):
        raise ValueError("walk uses a forbidden directed edge")
    return (
        code[path[0]][:half]
        + "".join(library[u, v] for u, v in zip(path, path[1:]))
        + code[path[-1]][half:]
    )


def decode(sequence, code):
    """Known frame, exact words, substitutions/indels are not corrected."""
    encode_edges(code, set())
    dna(sequence)
    width = len(next(iter(code.values())))
    if len(sequence) % width:
        raise ValueError("incomplete fixed-width word")
    inverse = {s: v for v, s in code.items()}
    words = [
        sequence[i : i + width] for i in range(0, len(sequence), width)
    ]
    if any(s not in inverse for s in words):
        raise ValueError("unrecognized codeword")
    return tuple(inverse[s] for s in words)


def results():
    a, b = "ACGTAC", "TACGTA"
    candidates = list(CODE.values()) + [
        "ACGATCGA",
        "CATGCATG",
        "AGCTTCGA",
        "CTGACATG",
        "GACATCAG",
        "TACGAGTC",
        "ACGTACGT",
        "AAAACCCC",
    ]
    selected = choose_library(candidates, 3)
    edges = encode_edges(CODE, EDGES)
    sequence = assemble(("A", "B", "C", "D"), CODE, EDGES)
    return dict(
        code=CODE,
        edges=[["".join(k), v] for k, v in sorted(edges.items())],
        sequence=sequence,
        decoded=list(decode(sequence, CODE)),
        offset=dict(
            a=a, b=b, hamming=hamming(a, b), match=list(longest_match(a, b))
        ),
        hairpin=dict(
            sequence="GCGAAACGC",
            warnings=[list(x) for x in hairpins("GCGAAACGC")],
        ),
        selected=list(selected) if selected else None,
        seam=dict(
            left="AACG",
            right="TCAG",
            target="CGTC",
            position=("AACG" + "TCAG").find("CGTC"),
        ),
    )
