"""A minimal controlled string-splicing example."""

from __future__ import annotations

from .alphabet import validate_sequence


def crossover(left: str, right: str, *, left_cut: int, right_cut: int) -> tuple[str, str]:
    """Exchange suffixes at declared boundaries.

    This is a formal rewrite, not a biochemical recombination simulator.
    """

    left_seq = validate_sequence(left)
    right_seq = validate_sequence(right)
    if not 0 <= left_cut <= len(left_seq):
        raise ValueError("left_cut must be a boundary in the left sequence")
    if not 0 <= right_cut <= len(right_seq):
        raise ValueError("right_cut must be a boundary in the right sequence")
    return (
        left_seq[:left_cut] + right_seq[right_cut:],
        right_seq[:right_cut] + left_seq[left_cut:],
    )

