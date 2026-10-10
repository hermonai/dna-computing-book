# DNAD-25 convergence audit

Decision: substantial rewrite. Keep storage in Chapter 25; move laboratory
provenance to 26 and retain incoming research artifacts as provenance, not evidence.

DNAD25-T1: (A,B,A XOR B) has minimum Hamming distance two and reconstructs one
located erasure from two correct, equal-width, distinct-address shards. Two
erasures are underdetermined; present parity inconsistency does not locate an error.
DNAD25-T2: byte/base map is bijective for aligned lengths divisible by four.
Header/layout validation and original length are essential to unordered recovery.
DNAD25-T3: finite constrained-language suffix counts obey the stated recurrence.
Lexical branch intervals partition the legal words; rank/unrank are inverse within
the declared finite domain, independently checked against enumeration.
DNAD25-T4: logical and physical rates differ by copy-count denominator. Bounds
on isolated payload words do not automatically constrain concatenated headers,
primers or word junctions.

DNAD25-E1 (tested): 33 chapter tests include independent all-byte arithmetic,
exhaustive short legal codebooks, all erasure slots, altered positions, indels,
trailing zeros, duplicate conflicts, header domains and probability endpoints.
DNAD25-E2 (tested digital trace): recover the 28-byte assigned source from four
groups, each missing slot A, in reversed read order with an exact duplicate.
DNAD25-E3 (implemented): n=8, GC=4, run<=2 gives 14,696 legal words, 13 payload
bits, rate 1.625 bits/nt, and rank 173 maps to AACGCTGT. Not channel capacity.

DNAD25-F1: raw archive's first strand has GC 0.225 and maximum run 18.
Recovering source bytes therefore does not prove biochemical sequence quality.
DNAD25-F2: recomputed CRCs and coherent altered parity can pass local checks;
the trusted original file digest detects the assigned altered-source example.
An attacker replacing both file and manifest defeats that external trust premise.
DNAD25-F3: ties become erasures; length-changing errors require alignment, not
column voting. Correlated systematic errors can defeat a majority.
DNAD25-O1: wet-lab synthesis/readout, primer specificity, realistic channel
calibration, adversarial authentication, optimized reconstruction and independent
scientific review remain open. No published storage performance was reproduced.

Six plates were redrawn as mechanism diagrams. Twenty questions include derivations,
traces, failure analysis and an independent-validation design rubric.
