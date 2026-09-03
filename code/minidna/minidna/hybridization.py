"""Deliberately simple, aligned hybridization scoring."""

from __future__ import annotations

from dataclasses import dataclass

from .alphabet import validate_sequence
from .complement import reverse_complement


@dataclass(frozen=True, slots=True)
class HybridizationResult:
    matches: int
    length: int
    fraction: float
    partner_reverse_complement: str


def aligned_hybridization(left_5to3: str, right_5to3: str) -> HybridizationResult:
    """Score complementary bases under one fixed full-length alignment.

    Both inputs are written 5-prime to 3-prime. The right strand is reverse
    complemented before comparison. This is an exact string toy model; it is
    not a thermodynamic binding or melting-temperature predictor.
    """

    left = validate_sequence(left_5to3)
    right = validate_sequence(right_5to3)
    if len(left) != len(right):
        raise ValueError("aligned toy scoring requires equal-length strands")
    partner = reverse_complement(right)
    matches = sum(a == b for a, b in zip(left, partner, strict=True))
    return HybridizationResult(matches, len(left), matches / len(left), partner)

