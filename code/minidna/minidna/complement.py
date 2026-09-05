"""Symbolic and tensor forms of DNA complementation."""

from __future__ import annotations

from collections.abc import Sequence

import torch

from .alphabet import BASE_TO_INDEX, DNA_ALPHABET, validate_sequence

COMPLEMENT = {"A": "T", "C": "G", "G": "C", "T": "A"}


def complement_base(base: str) -> str:
    """Return the canonical complement of one DNA base."""

    normalized = validate_sequence(base)
    if len(normalized) != 1:
        raise ValueError("expected exactly one DNA base")
    return COMPLEMENT[normalized]


def complement(sequence: str) -> str:
    """Complement bases without reversing the written sequence."""

    return "".join(COMPLEMENT[base] for base in validate_sequence(sequence))


def reverse_complement(sequence: str) -> str:
    """Return the 5-prime-to-3-prime reverse complement."""

    return complement(sequence)[::-1]


def one_hot(sequence: str, *, dtype: torch.dtype = torch.float32) -> torch.Tensor:
    """Encode a sequence as [length, 4] in A, C, G, T order."""

    normalized = validate_sequence(sequence)
    indices = torch.tensor([BASE_TO_INDEX[base] for base in normalized])
    return torch.nn.functional.one_hot(indices, num_classes=4).to(dtype=dtype)


def one_hot_batch(
    sequences: Sequence[str], *, dtype: torch.dtype = torch.float32
) -> torch.Tensor:
    """Encode equal-length sequences as [batch, length, 4]."""

    if isinstance(sequences, str):
        raise TypeError("sequences must be a collection of DNA strings")
    encoded = [one_hot(sequence, dtype=dtype) for sequence in sequences]
    if not encoded:
        raise ValueError("the sequence batch must not be empty")
    lengths = {tensor.shape[0] for tensor in encoded}
    if len(lengths) != 1:
        raise ValueError("all sequences in a batch must have equal length")
    return torch.stack(encoded)


def complement_matrix(*, dtype: torch.dtype = torch.float32) -> torch.Tensor:
    """Return the A<->T, C<->G permutation matrix."""

    return torch.tensor(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ],
        dtype=dtype,
    )


def tensor_complement(encoded: torch.Tensor) -> torch.Tensor:
    """Apply exact base complementation to tensors whose final axis is four."""

    if encoded.ndim == 0 or encoded.shape[-1] != 4:
        raise ValueError("the final tensor dimension must be A, C, G, T")
    matrix = complement_matrix(dtype=encoded.dtype).to(encoded.device)
    return encoded @ matrix.T


def tensor_reverse_complement(encoded: torch.Tensor) -> torch.Tensor:
    """Reverse-complement [length, 4] or [..., length, 4] tensors."""

    if encoded.ndim < 2 or encoded.shape[-1] != 4:
        raise ValueError("expected a tensor shaped [..., length, 4]")
    return torch.flip(tensor_complement(encoded), dims=(-2,))


def decode_one_hot(encoded: torch.Tensor) -> str:
    """Decode a rank-two one-hot or score tensor by argmax."""

    if encoded.ndim != 2 or encoded.shape[-1] != 4:
        raise ValueError("expected a [length, 4] tensor")
    return "".join(DNA_ALPHABET[index] for index in encoded.argmax(dim=-1).tolist())
