import torch

from minidna.complement import (
    complement,
    decode_one_hot,
    one_hot,
    reverse_complement,
    tensor_complement,
)


def test_complement_and_reverse_complement_are_distinct() -> None:
    assert complement("AACG") == "TTGC"
    assert reverse_complement("AACG") == "CGTT"


def test_reverse_complement_is_an_involution() -> None:
    sequence = "ACGTTGCA"
    assert reverse_complement(reverse_complement(sequence)) == sequence


def test_tensor_complement_matches_symbolic() -> None:
    sequence = "ACGTTGCA"
    encoded = one_hot(sequence)
    transformed = tensor_complement(encoded)
    assert transformed.dtype == torch.float32
    assert decode_one_hot(transformed) == complement(sequence)

