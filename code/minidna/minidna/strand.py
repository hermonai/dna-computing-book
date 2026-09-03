"""Immutable strand representation with explicit written orientation."""

from __future__ import annotations

from dataclasses import dataclass

from .alphabet import validate_sequence
from .complement import complement, reverse_complement


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
        return Strand(complement(self.sequence))

    def reverse_complement(self) -> "Strand":
        return Strand(reverse_complement(self.sequence))

    def __str__(self) -> str:
        return f"5'-{self.sequence}-3'"

