"""Canonical DNA alphabet utilities."""

from __future__ import annotations

DNA_ALPHABET: tuple[str, ...] = ("A", "C", "G", "T")
DNA_BASES = frozenset(DNA_ALPHABET)
BASE_TO_INDEX = {base: index for index, base in enumerate(DNA_ALPHABET)}


def normalize_sequence(sequence: str) -> str:
    """Remove ASCII whitespace and normalize a DNA sequence to uppercase."""

    if not isinstance(sequence, str):
        raise TypeError("sequence must be a string")
    return "".join(sequence.split()).upper()


def validate_sequence(sequence: str, *, allow_empty: bool = False) -> str:
    """Return a normalized sequence or raise with the invalid symbols."""

    normalized = normalize_sequence(sequence)
    if not normalized and not allow_empty:
        raise ValueError("DNA sequence must not be empty")
    invalid = sorted(set(normalized) - DNA_BASES)
    if invalid:
        raise ValueError(f"invalid DNA bases: {', '.join(invalid)}")
    return normalized

