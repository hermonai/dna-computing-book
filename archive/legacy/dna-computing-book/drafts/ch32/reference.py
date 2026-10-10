"""Finite abstraction witnesses and paired factorial arithmetic."""

from dataclasses import dataclass
import math
import statistics


def rc(sequence):
    if not isinstance(sequence, str) or any(b not in "ACGT" for b in sequence):
        raise ValueError("canonical DNA string required")
    return sequence.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def one_hot(sequence):
    rc(sequence)
    return tuple(tuple(int(j == "ACGT".index(b)) for j in range(4)) for b in sequence)


def decode_one_hot(rows):
    decoded = []
    for row in rows:
        if (
            len(row) != 4
            or any(type(v) is not int or v not in (0, 1) for v in row)
            or sum(row) != 1
        ):
            raise ValueError("strict integer one-hot row")
        decoded.append("ACGT"[row.index(1)])
    return "".join(decoded)


@dataclass(frozen=True)
class Molecule:
    bases: str
    frame: str
    concentration: float
    environment: str

    def __post_init__(self):
        rc(self.bases)
        if self.frame not in ("forward", "reverse"):
            raise ValueError("orientation frame")
        if (
            type(self.concentration) not in (float, int)
            or not math.isfinite(self.concentration)
            or self.concentration < 0
        ):
            raise ValueError("nonnegative finite concentration")
        if not isinstance(self.environment, str) or not self.environment:
            raise ValueError("environment")


def sequence_projection(molecule):
    return molecule.bases, molecule.frame


def collision_witness(samples, projection, property_fn):
    """A finite counterexample; absence is not a global injectivity proof."""
    seen = {}
    for sample in samples:
        key, value = projection(sample), property_fn(sample)
        if key in seen and seen[key][1] != value:
            return seen[key][0], sample
        seen[key] = (sample, value)
    return None


@dataclass(frozen=True)
class Representation:
    name: str
    properties: frozenset

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("representation name")
        if not isinstance(self.properties, frozenset) or any(
            not isinstance(p, str) or not p for p in self.properties
        ):
            raise ValueError("named property set")


def project(rep, target, declared):
    declared = frozenset(declared)
    if not declared <= rep.properties:
        raise ValueError("cannot invent an absent property")
    return Representation(target, declared)


def supports(rep, required):
    """Declared coverage, not verification of truth."""
    return frozenset(required) <= rep.properties


def paired_effect(baseline, mechanism):
    """Equal-weight paired seed differences; no confidence-level claim."""
    if len(baseline) != len(mechanism) or not baseline:
        raise ValueError("nonempty paired runs")
    if not all(math.isfinite(v) for v in (*baseline, *mechanism)):
        raise ValueError("finite scores")
    delta = [b - a for a, b in zip(baseline, mechanism)]
    sd = statistics.stdev(delta) if len(delta) > 1 else None
    return {
        "pairs": len(delta),
        "mean": statistics.mean(delta),
        "sample_sd": sd,
        "standard_error": sd / math.sqrt(len(delta)) if sd is not None else None,
    }


def factorial_effect(base_off, base_on, target_off, target_on):
    transplant = paired_effect(base_off, base_on)
    ablation = paired_effect(target_off, target_on)
    if transplant["pairs"] != ablation["pairs"]:
        raise ValueError("same seed panel")
    interaction = paired_effect(
        [b - a for a, b in zip(base_off, base_on)],
        [b - a for a, b in zip(target_off, target_on)],
    )
    return {"transplant": transplant, "ablation": ablation, "interaction": interaction}


TABLES = [
    (
        "panel",
        ["Seed", "Base off", "Base on", "Target off", "Target on"],
        ["seed", "base_off", "base_on", "target_off", "target_on"],
        "rrrrr",
    )
]
PLOTS = []
LISTINGS = [
    "collision_witness",
    "project",
    "decode_one_hot",
    "paired_effect",
    "factorial_effect",
]


def results():
    off = [0.70, 0.72, 0.69, 0.71]
    on = [0.73, 0.75, 0.71, 0.74]
    toff = [0.76, 0.78, 0.75, 0.77]
    ton = [0.80, 0.81, 0.79, 0.81]
    panel = [
        dict(seed=i + 1, base_off=a, base_on=b, target_off=c, target_on=d)
        for i, (a, b, c, d) in enumerate(zip(off, on, toff, ton))
    ]
    x = Molecule("ACGT", "forward", 1.0, "buffer-A")
    y = Molecule("ACGT", "forward", 10.0, "buffer-A")
    return {
        "panel": panel,
        "same_sequence": sequence_projection(x) == sequence_projection(y),
        "concentration_counterexample": collision_witness(
            [x, y], sequence_projection, lambda m: m.concentration
        )
        is not None,
        "onehot_roundtrip": decode_one_hot(one_hot("ACGT")),
        "factorial": factorial_effect(off, on, toff, ton),
    }
