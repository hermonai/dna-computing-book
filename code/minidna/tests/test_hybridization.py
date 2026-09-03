import pytest

from minidna.hybridization import aligned_hybridization


def test_perfect_reverse_complements_score_one() -> None:
    result = aligned_hybridization("AACG", "CGTT")
    assert result.matches == 4
    assert result.fraction == 1.0


def test_score_exposes_fixed_alignment_assumption() -> None:
    result = aligned_hybridization("AAAA", "AAAT")
    assert result.matches == 1
    assert result.fraction == 0.25


def test_rejects_unequal_lengths() -> None:
    with pytest.raises(ValueError, match="equal-length"):
        aligned_hybridization("ACG", "AC")

