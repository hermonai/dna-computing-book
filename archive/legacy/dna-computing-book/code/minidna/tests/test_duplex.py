from itertools import product
import pytest
from minidna.strand import Strand, SequenceView
from minidna.duplex import Duplex, chapter_example


def test_asymmetric_orientation_example():
    duplex = Duplex.from_sequence("AACG")
    assert tuple(map(str, duplex.rows())) == ("5'-AACG-3'", "3'-TTGC-5'")
    assert str(duplex.bottom) == "5'-CGTT-3'"
    assert str(duplex.top.aligned_complement()) == "3'-TTGC-5'"
    assert chapter_example()["base_pairs"] == 4


def test_all_short_sequences_have_antiparallel_pairing_and_round_trip():
    expected_pairs = {("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")}
    for length in range(1, 6):
        for bases in product("ACGT", repeat=length):
            sequence = "".join(bases)
            duplex = Duplex.from_sequence(sequence)
            top, bottom = duplex.rows()
            assert top.direction == "5to3" and bottom.direction == "3to5"
            assert all(pair in expected_pairs for pair in zip(top.sequence, bottom.sequence))
            assert Duplex.from_sequence(duplex.bottom.sequence).bottom.sequence == sequence


def test_partner_must_not_be_unreversed_complement():
    with pytest.raises(ValueError):
        Duplex(Strand("AACG"), Strand("TTGC"))
    assert Strand("AACG").complement().sequence == "TTGC"  # legacy meaning is unchanged


def test_normalization_and_rejected_domains():
    assert Duplex.from_sequence("a a\u2003cg").top.sequence == "AACG"
    for sequence in ("", "AN", "AU", "5'-AACG-3'"):
        with pytest.raises(ValueError):
            Duplex.from_sequence(sequence)
    with pytest.raises(TypeError):
        Duplex("AACG", "CGTT")
    with pytest.raises(ValueError):
        SequenceView("A", "unknown")


def test_exercise_reverse_complements_and_palindrome():
    assert Duplex.from_sequence("AGTC").bottom.sequence == "GACT"
    assert Duplex.from_sequence("ATAT").bottom.sequence == "ATAT"
    assert Duplex.from_sequence("AACG").bottom.sequence != "AACG"
