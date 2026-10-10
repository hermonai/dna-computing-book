"""Immutable strand representation with explicit written orientation."""

from __future__ import annotations

from dataclasses import dataclass

from .alphabet import validate_sequence
from .complement import complement, reverse_complement


@dataclass(frozen=True, slots=True)
class SequenceView:
    """An oriented written row, not a second chemical strand object."""

    sequence: str
    direction: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "sequence", validate_sequence(self.sequence))
        if self.direction not in {"5to3", "3to5"}:
            raise ValueError("direction must be 5to3 or 3to5")

    def __str__(self) -> str:
        left, right = ("5", "3") if self.direction == "5to3" else ("3", "5")
        return f"{left}'-{self.sequence}-{right}'"


@dataclass(frozen=True, slots=True)
class Strand:
    """A DNA strand written 5-prime to 3-prime.

    This class stores sequence information only. It does not model molecular
    concentration, secondary structure, temperature, or chemical modifications.
    """

    sequence: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "sequence", validate_sequence(self.sequence))

    def __len__(self) -> int:
        return len(self.sequence)

    def complement(self) -> "Strand":
        """Legacy symbol substitution, reinterpreted as a new 5′-to-3′ sequence.

        NOT the aligned physical partner. Use aligned_complement() for a
        3′-to-5′ written row or reverse_complement() for the partner in 5′-to-3′.
        Behavior is retained for compatibility, not recommended for duplexes.
        """
        return Strand(complement(self.sequence))

    def aligned_complement(self) -> SequenceView:
        """Return the ideal paired row directly below this 5′-to-3′ strand."""
        return SequenceView(complement(self.sequence), "3to5")

    def reverse_complement(self) -> "Strand":
        return Strand(reverse_complement(self.sequence))

    def __str__(self) -> str:
        return f"5'-{self.sequence}-3'"
