"""DNAD-25: finite constrained codes and an indexed erasure archive.

Pure digital references. CRC is accidental-error detection, not authentication.
Reads are oriented canonical DNA; indel alignment and physical access are outside
the decoder contract. The archive uses unconstrained two-bit mapping on purpose.
"""

from functools import lru_cache
import hashlib
import json
import math
import random
import struct
import zlib

DNA = "ACGT"
HEADER = struct.Struct(">BHBHIH")
VERSION = 1
MAX_CHUNK = 4096


def integer(value, name, lower=0, upper=None):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    if value < lower or (upper is not None and value > upper):
        raise ValueError(f"{name} is outside the reference domain")
    return value


def canonical(sequence, empty=True):
    if not isinstance(sequence, str) or (not sequence and not empty):
        raise ValueError("Expected a canonical DNA string")
    if any(base not in DNA for base in sequence):
        raise ValueError("Noncanonical DNA base")
    return sequence


def encode_bytes(data):
    if not isinstance(data, bytes):
        raise ValueError("Expected bytes, not a text/bit string")
    return "".join(DNA[(byte >> shift) & 3] for byte in data for shift in (6, 4, 2, 0))


def decode_bytes(sequence):
    canonical(sequence)
    if len(sequence) % 4:
        raise ValueError("Byte mapping requires a multiple of four nucleotides")
    return bytes(
        sum(
            DNA.index(base) << (6 - 2 * j) for j, base in enumerate(sequence[i : i + 4])
        )
        for i in range(0, len(sequence), 4)
    )


def xor_bytes(a, b):
    if not isinstance(a, bytes) or not isinstance(b, bytes) or len(a) != len(b):
        raise ValueError("XOR operands must be equal-width bytes")
    return bytes(x ^ y for x, y in zip(a, b))


def recover_group(a, b, parity):
    known = [x for x in (a, b, parity) if x is not None]
    if len(known) < 2:
        raise ValueError("Two known shards are required")
    if not all(isinstance(x, bytes) and len(x) == len(known[0]) for x in known):
        raise ValueError("Inconsistent shard widths")
    if a is None:
        a = xor_bytes(b, parity)
    elif b is None:
        b = xor_bytes(a, parity)
    elif parity is not None and xor_bytes(a, b) != parity:
        raise ValueError("Present shards violate parity")
    return a, b


def validate_manifest(manifest):
    if not isinstance(manifest, dict) or set(manifest) != {
        "version",
        "length",
        "chunk_width",
        "groups",
        "sha256",
    }:
        raise ValueError("Incomplete or unexpected archive manifest")
    if integer(manifest["version"], "version", 1) != VERSION:
        raise ValueError("Unsupported archive version")
    length = integer(manifest["length"], "length", 0, 2**32 - 1)
    width = integer(manifest["chunk_width"], "chunk_width", 1, MAX_CHUNK)
    groups = integer(manifest["groups"], "groups", 0, 65535)
    if groups != (length + 2 * width - 1) // (2 * width):
        raise ValueError("Manifest group count disagrees with length")
    digest = manifest["sha256"]
    if (
        not isinstance(digest, str)
        or len(digest) != 64
        or any(c not in "0123456789abcdef" for c in digest)
    ):
        raise ValueError("Invalid SHA-256 digest")
    return length, width, groups


def encode_archive(data, chunk_width=4):
    if not isinstance(data, bytes):
        raise ValueError("Expected byte payload")
    integer(chunk_width, "chunk_width", 1, MAX_CHUNK)
    groups = (len(data) + 2 * chunk_width - 1) // (2 * chunk_width)
    manifest = {
        "version": VERSION,
        "length": len(data),
        "chunk_width": chunk_width,
        "groups": groups,
        "sha256": hashlib.sha256(data).hexdigest(),
    }
    validate_manifest(manifest)
    strands = []
    for group in range(groups):
        start = group * 2 * chunk_width
        pair = data[start : start + 2 * chunk_width].ljust(2 * chunk_width, b"\0")
        a, b = pair[:chunk_width], pair[chunk_width:]
        for slot, shard in enumerate((a, b, xor_bytes(a, b))):
            header = HEADER.pack(VERSION, group, slot, chunk_width, len(data), groups)
            body = header + shard
            frame = body + struct.pack(">I", zlib.crc32(body))
            strands.append(encode_bytes(frame))
    return manifest, strands


def parse_read(sequence, manifest):
    """Fail a malformed read; caller may classify this as a located erasure."""
    length, width, groups = validate_manifest(manifest)
    frame = decode_bytes(sequence)
    if len(frame) != HEADER.size + width + 4:
        raise ValueError("Frame length differs from declared width")
    body, check = frame[:-4], frame[-4:]
    if zlib.crc32(body) != struct.unpack(">I", check)[0]:
        raise ValueError("Read CRC mismatch")
    version, group, slot, w, n, g = HEADER.unpack(body[: HEADER.size])
    if (version, w, n, g) != (VERSION, width, length, groups):
        raise ValueError("Read header belongs to another archive layout")
    if group >= groups or slot > 2:
        raise ValueError("Read address outside the archive")
    return group, slot, body[HEADER.size :]


def decode_archive(reads, manifest):
    """Accept an unordered pool; erase invalid reads, reject conflicting evidence."""
    length, _, groups = validate_manifest(manifest)
    shards = {}
    rejected = duplicates = 0
    for sequence in reads:
        try:
            group, slot, shard = parse_read(sequence, manifest)
        except ValueError:
            rejected += 1
            continue
        key = (group, slot)
        if key in shards:
            if shards[key] != shard:
                raise ValueError("Conflicting CRC-valid reads at the same address")
            duplicates += 1
        shards[key] = shard
    chunks = []
    recovered = 0
    for group in range(groups):
        a, b, parity = (shards.get((group, slot)) for slot in range(3))
        recovered += int(a is None or b is None)
        a, b = recover_group(a, b, parity)
        chunks.extend((a, b))
    output = b"".join(chunks)[:length]
    if hashlib.sha256(output).hexdigest() != manifest["sha256"]:
        raise ValueError("Reconstructed file fails the manifest digest")
    return output, {
        "rejected_reads": rejected,
        "duplicate_reads": duplicates,
        "recovered_groups": recovered,
        "accepted_addresses": len(shards),
    }


def strict_consensus(reads):
    """Known equal-length/aligned cluster; any tied/ambiguous position is an erasure."""
    if not reads:
        raise ValueError("No reads in cluster")
    for sequence in reads:
        canonical(sequence, empty=False)
    if any(len(s) != len(reads[0]) for s in reads):
        raise ValueError("Indels require a separate alignment model")
    consensus = []
    for column in zip(*reads):
        counts = [column.count(base) for base in DNA]
        winner = max(range(4), key=counts.__getitem__)
        if 2 * counts[winner] <= len(reads):
            return None
        consensus.append(DNA[winner])
    return "".join(consensus)


def substitutions(sequence, probability, seed):
    canonical(sequence)
    if isinstance(probability, bool) or not isinstance(probability, (int, float)):
        raise ValueError("Probability must be a finite scalar")
    if not math.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("Probability outside [0,1]")
    rng = random.Random(seed)
    return "".join(
        rng.choice(DNA.replace(base, "")) if rng.random() < probability else base
        for base in sequence
    )


class ConstraintCodec:
    """Lexicographic rank/unrank using exact suffix counts, n <= 64.

    Constraints are GC-count bounds and maximum homopolymer run only.
    No melting-temperature, hairpin, primer or cross-hybridization guarantee.
    """

    def __init__(self, length, min_gc, max_gc, max_run=2):
        self.length = integer(length, "length", 1, 64)
        self.min_gc = integer(min_gc, "min_gc", 0, length)
        self.max_gc = integer(max_gc, "max_gc", self.min_gc, length)
        self.max_run = integer(max_run, "max_run", 1, length)

        @lru_cache(None)
        def count(remaining, last, run, gc):
            if gc > self.max_gc or gc + remaining < self.min_gc:
                return 0
            if remaining == 0:
                return int(self.min_gc <= gc <= self.max_gc)
            total = 0
            for base in DNA:
                next_run = run + 1 if base == last else 1
                if next_run <= self.max_run:
                    total += count(
                        remaining - 1, base, next_run, gc + int(base in "GC")
                    )
            return total

        self._count = count

    def completions(self, prefix):
        canonical(prefix)
        if len(prefix) > self.length:
            raise ValueError("Prefix exceeds code length")
        run = 0
        last = ""
        for base in prefix:
            run = run + 1 if base == last else 1
            last = base
            if run > self.max_run:
                return 0
        gc = sum(base in "GC" for base in prefix)
        return self._count(self.length - len(prefix), last, run, gc)

    @property
    def size(self):
        return self.completions("")

    @property
    def payload_bits(self):
        return self.size.bit_length() - 1  # -1 marks an empty codebook

    def unrank(self, rank):
        integer(rank, "rank", 0, self.size - 1)
        prefix = ""
        for _ in range(self.length):
            for base in DNA:
                count = self.completions(prefix + base)
                if rank < count:
                    prefix += base
                    break
                rank -= count
        return prefix

    def rank(self, sequence):
        canonical(sequence)
        if len(sequence) != self.length or self.completions(sequence) != 1:
            raise ValueError("Sequence is outside the constrained codebook")
        rank = 0
        prefix = ""
        for base in sequence:
            for candidate in DNA[: DNA.index(base)]:
                rank += self.completions(prefix + candidate)
            prefix += base
        return rank


def gc_fraction(sequence):
    canonical(sequence, empty=False)
    return sum(base in "GC" for base in sequence) / len(sequence)


def maximum_run(sequence):
    canonical(sequence)
    best = run = 0
    last = ""
    for base in sequence:
        run = run + 1 if base == last else 1
        last = base
        best = max(best, run)
    return best


def results():
    data = b"DNA stores bytes, not proof."
    manifest, strands = encode_archive(data, 4)
    # Explicit located-erasure intervention, one data shard from each group.
    reads = [s for i, s in enumerate(strands) if i % 3 != 0]
    reads.reverse()
    reads.append(reads[0])
    decoded, report = decode_archive(reads, manifest)
    codec = ConstraintCodec(8, 4, 4, 2)
    rank = 173
    word = codec.unrank(rank)
    cluster = [substitutions(strands[0], 0.02, seed) for seed in range(11)]
    consensus = strict_consensus(cluster)
    return {
        "kind": "digital reference outputs; no laboratory measurements",
        "archive": {
            "source_bytes": len(data),
            "groups": manifest["groups"],
            "unique_strands": len(strands),
            "nt_per_strand": len(strands[0]),
            "unique_nt": sum(map(len, strands)),
            "net_bits_per_unique_nt": 8 * len(data) / sum(map(len, strands)),
            "recovered_exactly": decoded == data,
            **report,
            "first_gc_fraction": gc_fraction(strands[0]),
            "first_maximum_run": maximum_run(strands[0]),
        },
        "constraint": {
            "length": codec.length,
            "size": codec.size,
            "fixed_payload_bits": codec.payload_bits,
            "rate_bits_per_nt": codec.payload_bits / codec.length,
            "unused_words": codec.size - 2**codec.payload_bits,
            "rank": rank,
            "word": word,
            "decoded_rank": codec.rank(word),
        },
        "consensus": {
            "reads": len(cluster),
            "assigned_substitution_probability": 0.02,
            "exact_for_assigned_seeds": consensus == strands[0],
            "ambiguous_clusters_are_erasures": strict_consensus(["AC", "AG"]) is None,
        },
        "code_sizes": [
            {
                "length": n,
                "words": ConstraintCodec(n, n // 2, n // 2, 2).size,
                "bits": ConstraintCodec(n, n // 2, n // 2, 2).payload_bits,
                "rate": ConstraintCodec(n, n // 2, n // 2, 2).payload_bits / n,
            }
            for n in (4, 8, 12, 16, 24, 32)
        ],
    }


TABLES = [
    (
        "code_sizes",
        ["Length (nt)", "Legal words", "Payload (bits)", "Rate (bits/nt)"],
        ["length", "words", "bits", "rate"],
        "rrrr",
    ),
]
PLOTS = []
LISTINGS = [
    "recover_group",
    "encode_archive",
    "decode_archive",
    "strict_consensus",
    "ConstraintCodec.__init__",
    "ConstraintCodec.unrank",
    "ConstraintCodec.rank",
]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
