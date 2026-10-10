import pytest

from minidna.alphabet import normalize_sequence, validate_sequence


def test_normalizes_case_and_ascii_whitespace() -> None:
    assert normalize_sequence(" ac\ngt ") == "ACGT"


def test_rejects_noncanonical_bases() -> None:
    with pytest.raises(ValueError, match="N"):
        validate_sequence("ACNT")

