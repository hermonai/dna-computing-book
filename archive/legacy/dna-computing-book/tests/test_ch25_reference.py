"""Independent byte, codebook and located-erasure oracles for DNAD-25."""

import importlib.util
import itertools
from pathlib import Path
import random
import struct
import zlib

import pytest

p = Path(__file__).parents[1] / "drafts/ch25/reference.py"
spec = importlib.util.spec_from_file_location("dnad25", p)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def independent_legal(word, min_gc, max_gc, max_run):
    gc = sum(c in "GC" for c in word)
    return min_gc <= gc <= max_gc and all(
        not all(x == block[0] for x in block)
        for block in (word[i : i + max_run + 1] for i in range(len(word) - max_run))
    )


def frame_with_payload(sequence, payload):
    frame = r.decode_bytes(sequence)
    body = frame[: r.HEADER.size] + payload
    return r.encode_bytes(body + struct.pack(">I", zlib.crc32(body)))


def test_byte_mapping_all_values_independent_base4():
    for byte in range(256):
        digits = []
        value = byte
        for _ in range(4):
            value, digit = divmod(value, 4)
            digits.append("ACGT"[digit])
        expected = "".join(reversed(digits))
        assert r.encode_bytes(bytes([byte])) == expected
        assert r.decode_bytes(expected) == bytes([byte])


@pytest.mark.parametrize("bad", ["aCGT", "ACGN", "ACT", 17])
def test_decode_rejects_bad_alphabet_length_type(bad):
    with pytest.raises(ValueError):
        r.decode_bytes(bad)


def test_xor_does_not_truncate_or_accept_text():
    for a, b in [(b"A", b"AB"), ("A", b"A")]:
        with pytest.raises(ValueError):
            r.xor_bytes(a, b)


def test_all_byte_pairs_all_single_erasure_locations():
    for a in range(16):
        for b in range(16):
            pair = (bytes([a]), bytes([b]))
            shards = [*pair, bytes([a ^ b])]
            for slot in range(3):
                missing = shards.copy()
                missing[slot] = None
                assert r.recover_group(*missing) == pair


def test_two_erasures_and_present_bad_parity_fail():
    for shards in [
        (None, None, b"x"),
        (b"x", None, None),
        (b"a", b"b", b"z"),
        (b"a", b"bb", None),
    ]:
        with pytest.raises(ValueError):
            r.recover_group(*shards)


@pytest.mark.parametrize("length", [0, 1, 7, 8, 9, 28, 65])
def test_archive_lengths_unordered_and_exact_trailing_zero(length):
    data = bytes((17 * i) % 256 for i in range(length))
    manifest, strands = r.encode_archive(data)
    random.Random(length).shuffle(strands)
    assert r.decode_archive(strands, manifest)[0] == data


def test_every_single_strand_erasure_and_duplicates():
    data = b"Recovered\0\0"
    manifest, strands = r.encode_archive(data)
    for i in range(len(strands)):
        reads = strands[:i] + strands[i + 1 :] + [strands[(i + 1) % len(strands)]]
        decoded, report = r.decode_archive(reads, manifest)
        assert decoded == data
        assert report["duplicate_reads"] == 1


def test_two_missing_in_same_group_fail_not_two_across_groups():
    manifest, strands = r.encode_archive(b"123456789")
    with pytest.raises(ValueError):
        r.decode_archive(strands[2:], manifest)
    assert (
        r.decode_archive(
            [s for i, s in enumerate(strands) if i not in (0, 3)], manifest
        )[0]
        == b"123456789"
    )


def test_every_single_base_substitution_becomes_detected_erasure():
    manifest, strands = r.encode_archive(b"ABCD")
    for position, base in enumerate(strands[0]):
        for replacement in "ACGT":
            if base == replacement:
                continue
            bad = strands[0][:position] + replacement + strands[0][position + 1 :]
            decoded, report = r.decode_archive([bad, *strands[1:]], manifest)
            assert decoded == b"ABCD" and report["rejected_reads"] == 1


def test_indel_is_frame_length_error_not_aligned_by_magic():
    manifest, strands = r.encode_archive(b"ABCD")
    for bad in (strands[0][1:], strands[0] + "A"):
        decoded, report = r.decode_archive([bad, *strands[1:]], manifest)
        assert decoded == b"ABCD" and report["rejected_reads"] == 1


def test_crc_valid_conflicting_reads_rejected():
    manifest, strands = r.encode_archive(b"ABCD")
    conflicting = frame_with_payload(strands[0], b"bad!")
    with pytest.raises(ValueError, match="Conflicting"):
        r.decode_archive([*strands, conflicting], manifest)


def test_coherent_corrupt_pair_detected_by_file_digest():
    manifest, strands = r.encode_archive(b"ABCD")
    a, b = b"bad!", b"\0" * 4
    corrupt = [
        frame_with_payload(strands[i], shard)
        for i, shard in enumerate((a, b, r.xor_bytes(a, b)))
    ]
    with pytest.raises(ValueError, match="digest"):
        r.decode_archive(corrupt, manifest)


@pytest.mark.parametrize("width", [0, -1, True, 1.5, 4097])
def test_archive_domain(width):
    with pytest.raises(ValueError):
        r.encode_archive(b"x", width)


def test_bad_manifest_is_not_silently_used():
    manifest, strands = r.encode_archive(b"x")
    for key, value in [("groups", 0), ("sha256", "x" * 64), ("length", -1)]:
        bad = dict(manifest, **{key: value})
        with pytest.raises(ValueError):
            r.decode_archive(strands, bad)


def test_consensus_exact_and_tie_reject_not_lexical_default():
    assert r.strict_consensus(["ACGT", "ACGT", "AGGT"]) == "ACGT"
    assert r.strict_consensus(["A", "C"]) is None
    assert r.strict_consensus(["A", "C", "G"]) is None
    with pytest.raises(ValueError):
        r.strict_consensus([])
    with pytest.raises(ValueError):
        r.strict_consensus(["AC", "ACC"])


def test_exhaustive_codebook_rank_unrank_and_count_oracle():
    codec = r.ConstraintCodec(4, 2, 2, 2)
    legal = [
        "".join(x)
        for x in itertools.product("ACGT", repeat=4)
        if independent_legal("".join(x), 2, 2, 2)
    ]
    assert codec.size == len(legal) == 96
    for rank, word in enumerate(legal):
        assert codec.unrank(rank) == word
        assert codec.rank(word) == rank


def test_suffix_counts_exhaustive_independent_completion():
    codec = r.ConstraintCodec(6, 2, 4, 2)
    legal = [
        "".join(x)
        for x in itertools.product("ACGT", repeat=6)
        if independent_legal("".join(x), 2, 4, 2)
    ]
    for n in range(4):
        for letters in itertools.product("ACGT", repeat=n):
            prefix = "".join(letters)
            assert codec.completions(prefix) == sum(w.startswith(prefix) for w in legal)


def test_rank173_trace_and_sampled_large_rank_roundtrip():
    codec = r.ConstraintCodec(8, 4, 4, 2)
    assert codec.unrank(173) == "AACGCTGT"
    assert codec.payload_bits == 13
    for rank in [0, codec.size - 1, *range(0, codec.size, 101)]:
        word = codec.unrank(rank)
        assert independent_legal(word, 4, 4, 2)
        assert codec.rank(word) == rank


def test_constraint_domains_and_illegal_words():
    for args in [(0, 0, 0, 1), (4, 3, 2, 2), (4, 0, 4, 0), (65, 0, 65, 2)]:
        with pytest.raises(ValueError):
            r.ConstraintCodec(*args)
    codec = r.ConstraintCodec(4, 2, 2, 2)
    for bad in ("AAAA", "AC", "ACGN"):
        with pytest.raises(ValueError):
            codec.rank(bad)
    for rank in (-1, codec.size, True):
        with pytest.raises(ValueError):
            codec.unrank(rank)


def test_channel_probability_validation_and_endpoints():
    assert r.substitutions("ACGT", 0, 25) == "ACGT"
    assert all(a != b for a, b in zip("ACGT", r.substitutions("ACGT", 1, 25)))
    for p in (-1, 2, float("nan"), float("inf"), True):
        with pytest.raises(ValueError):
            r.substitutions("ACGT", p, 25)
