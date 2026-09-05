import pytest
import torch

from minidna.complement import (
    complement,
    complement_base,
    complement_matrix,
    decode_one_hot,
    one_hot,
    one_hot_batch,
    reverse_complement,
    tensor_complement,
    tensor_reverse_complement,
)


def test_complement_and_reverse_complement_are_distinct() -> None:
    assert complement("AACG") == "TTGC"
    assert reverse_complement("AACG") == "CGTT"


@pytest.mark.parametrize(
    ("base", "expected"), (("A", "T"), ("T", "A"), ("C", "G"), ("G", "C"))
)
def test_complement_base_pairs(base: str, expected: str) -> None:
    assert complement_base(base) == expected


def test_complement_base_rejects_a_sequence() -> None:
    with pytest.raises(ValueError, match="exactly one"):
        complement_base("AC")


def test_empty_sequence_is_not_a_strand() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        reverse_complement("")


def test_reverse_complement_is_an_involution() -> None:
    sequence = "ACGTTGCA"
    assert reverse_complement(reverse_complement(sequence)) == sequence


def test_complement_matrix_is_an_involution() -> None:
    matrix = complement_matrix()
    assert torch.equal(matrix @ matrix, torch.eye(4))


def test_tensor_complement_matches_symbolic() -> None:
    sequence = "ACGTTGCA"
    encoded = one_hot(sequence)
    transformed = tensor_complement(encoded)
    assert transformed.dtype == torch.float32
    assert decode_one_hot(transformed) == complement(sequence)


def test_tensor_reverse_complement_matches_symbolic() -> None:
    sequence = "AACG"
    transformed = tensor_reverse_complement(one_hot(sequence))
    assert decode_one_hot(transformed) == reverse_complement(sequence)


def test_batched_reverse_complement_preserves_shape_and_parity() -> None:
    sequences = ("AACG", "TTAC")
    encoded = one_hot_batch(sequences)
    transformed = tensor_reverse_complement(encoded)
    assert transformed.shape == (2, 4, 4)
    assert [decode_one_hot(row) for row in transformed] == [
        reverse_complement(sequence) for sequence in sequences
    ]


def test_one_hot_batch_rejects_ragged_sequences() -> None:
    with pytest.raises(ValueError, match="equal length"):
        one_hot_batch(("AC", "ACG"))
