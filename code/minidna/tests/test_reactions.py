from minidna.reactions import cut, ligate
from minidna.splicing import crossover


def test_cut_then_ligate_round_trip() -> None:
    left, right = cut("ACGT", 2)
    assert (left, right) == ("AC", "GT")
    assert ligate(left, right) == "ACGT"


def test_crossover_exchanges_suffixes() -> None:
    assert crossover("AAAA", "CCCC", left_cut=2, right_cut=2) == (
        "AACC",
        "CCAA",
    )

