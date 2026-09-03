from minidna import Strand, aligned_hybridization

strand = Strand("ACGT")
partner = strand.reverse_complement()

print(strand)
print(partner)
print(aligned_hybridization(strand.sequence, partner.sequence))

