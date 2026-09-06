# DNA-02 review record

Date: 2026-09-06. Outline: nucleotide vocabulary; strand direction; pairing versus covalent linkage; aligned complement versus partner written 5′ to 3′; primer-extension orientation; exact representation tests; exercises.

Sources inspected: Cooper, The Cell (2000), Nucleic Acids subsection of [Molecular Composition](https://www.ncbi.nlm.nih.gov/books/NBK9879/); Alberts et al., Molecular Biology of the Cell (2002), complementary-chain subsection of [DNA structure](https://www.ncbi.nlm.nih.gov/books/NBK26821/) and [Figure 4-4 caption](https://www.ncbi.nlm.nih.gov/books/NBK26821/figure/A599/?report=objectonly); Cooper, [DNA Replication](https://www.ncbi.nlm.nih.gov/books/NBK9940/), polymerase/primer and fork sections. Scope is foundational chemistry and notation, not a current survey of polymerase families. No copied figures.

Source cautions: the retrieved Alberts Figure 4-5 caption gives an apparent inconsistent distance; no numerical helix dimension is imported. Do not turn textbook cartoons of termini into claims that every synthetic oligonucleotide has a particular terminal modification. Neither broad historical polymerase inventories nor dated open questions are adopted.

Original work: AACG/TTGC/CGTT orientation example; a fully paired symbolic Duplex view; exhaustive short-sequence invariants; representation tests; figure layout and primer-direction example. Complementarity is not a binding probability or thermal-stability calculation.

Code decision: retain legacy Strand.complement as a documented symbol transformation for compatibility; explicitly warn against using it as the aligned partner. Add an unambiguous aligned_complement view with 3′-to-5′ metadata and a validated Duplex. Physical partner written 5′ to 3′ remains reverse_complement. Test the asymmetric case, not just involutions.

Figure review requires four polarity labels, canonical pairing at each column, different encodings for covalent linkage and pairing, correct reversal without base substitution, and primer growth only at its 3′ end. Detailed atomic structures, reaction yields and helix dimensions are intentionally outside the drawings.

Internal mathematical/scientific review only; independent subject review remains open. Publication checks are recorded in CHAPTER_02_REPORT.md.
