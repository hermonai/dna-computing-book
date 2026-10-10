"""Fully paired canonical DNA sequence views, without thermodynamics."""
from dataclasses import dataclass
from .strand import Strand, SequenceView


@dataclass(frozen=True, slots=True)
class Duplex:
    """Two sequences stored 5′ to 3′; rows display antiparallel alignment.

    This model excludes mismatches, overhangs, ambiguous bases and chemical
    modifications. It makes no claim that an actual duplex forms in solution.
    """
    top: Strand
    bottom: Strand

    def __post_init__(self):
        if not isinstance(self.top, Strand) or not isinstance(self.bottom, Strand):
            raise TypeError("duplex members must be Strand objects")
        if self.bottom.sequence != self.top.reverse_complement().sequence:
            raise ValueError("bottom must be the top reverse complement in 5′-to-3′")

    @classmethod
    def from_sequence(cls, sequence: str) -> "Duplex":
        top = Strand(sequence)
        return cls(top, top.reverse_complement())

    def rows(self) -> tuple[SequenceView, SequenceView]:
        return (SequenceView(self.top.sequence, "5to3"),
                SequenceView(self.bottom.sequence[::-1], "3to5"))


def chapter_example():
    duplex = Duplex.from_sequence("AACG")
    top, aligned = duplex.rows()
    return {"top_5to3": top.sequence, "aligned_3to5": aligned.sequence,
            "partner_5to3": duplex.bottom.sequence,
            "length_nt_per_strand": len(duplex.top), "base_pairs": len(duplex.top),
            "model": "ideal canonical sequence alignment; not a binding prediction"}
