"""Oriented symbolic DNA; no hybridization or structure prediction."""

from itertools import product
import json

SETS = dict(
    A="A",
    C="C",
    G="G",
    T="T",
    R="AG",
    Y="CT",
    M="AC",
    K="GT",
    S="CG",
    W="AT",
    B="CGT",
    D="AGT",
    H="ACT",
    V="ACG",
    N="ACGT",
)
BASE_COMPLEMENT = dict(zip("ACGT", "TGCA"))
BY_SET = {frozenset(v): k for k, v in SETS.items()}
COMPLEMENT = {
    k: BY_SET[frozenset(BASE_COMPLEMENT[b] for b in v)]
    for k, v in SETS.items()
}


def validate(sequence):
    if not isinstance(sequence, str) or set(sequence) - SETS.keys():
        raise ValueError("uppercase ungapped IUPAC DNA string required")
    return sequence


def complement(sequence):
    return "".join(COMPLEMENT[b] for b in validate(sequence))


def reverse_complement(sequence):
    return complement(sequence)[::-1]


def reverse_interval(length, start, stop):
    if any(type(v) is not int for v in (length, start, stop)):
        raise ValueError("integer boundaries required")
    if not 0 <= start <= stop <= length:
        raise ValueError("expected 0 <= start <= stop <= length")
    return length - stop, length - start


def compatible_aligned(upper, lower):
    """Upper is 5' to 3'; lower is ALIGNED 3' to 5', not stored 5' to 3'."""
    validate(upper)
    validate(lower)
    if len(upper) != len(lower):
        return False
    return all(
        {BASE_COMPLEMENT[b] for b in SETS[a]} & set(SETS[c])
        for a, c in zip(upper, lower)
    )


def expansions(sequence, limit=4096):
    validate(sequence)
    if type(limit) is not int or limit < 1:
        raise ValueError("positive expansion budget required")
    count = 1
    for b in sequence:
        count *= len(SETS[b])
        if count > limit:
            raise ValueError("ambiguity expansion exceeds declared budget")
    return ["".join(v) for v in product(*(SETS[b] for b in sequence))]


def palindrome_count(length):
    if type(length) is not int or length < 0:
        raise ValueError("nonnegative length required")
    return 0 if length % 2 else 4 ** (length // 2)


def results():
    s = "ACGTAGCTA"
    a, b = reverse_interval(len(s), 2, 6)
    return {
        "scope": "symbolic orientation and uncertainty sets only",
        "example": {
            "input": "ACGTA",
            "complement": complement("ACGTA"),
            "reverse": "ACGTA"[::-1],
            "reverse_complement": reverse_complement("ACGTA"),
        },
        "ambiguity": {
            k: {"set": v, "complement": COMPLEMENT[k]}
            for k, v in SETS.items()
        },
        "expansion_ARN": expansions("ARN"),
        "interval": {
            "sequence": s,
            "original": [2, 6],
            "reversed": [a, b],
            "substring": s[2:6],
            "rc_substring": reverse_complement(s)[a:b],
        },
        "palindromes": [
            {"length": n, "count": palindrome_count(n)} for n in range(7)
        ],
        "controls": {
            "correct_aligned": compatible_aligned("ACGTA", "TGCAT"),
            "wrong_same_direction": compatible_aligned("ACGTA", "TACGT"),
            "possible_not_guaranteed": compatible_aligned("R", "Y"),
        },
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
