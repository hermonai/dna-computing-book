"""Exact sequence operations used to explain cutting and ligation."""

from __future__ import annotations

from .alphabet import validate_sequence


def cut(sequence: str, position: int) -> tuple[str, str]:
    """Cut before ``position`` using Python's zero-based boundary convention."""

    normalized = validate_sequence(sequence)
    if not 0 <= position <= len(normalized):
        raise ValueError("cut position must be a sequence boundary")
    return normalized[:position], normalized[position:]


def ligate(left: str, right: str) -> str:
    """Join two validated sequence strings in the written order."""

    return validate_sequence(left) + validate_sequence(right)

