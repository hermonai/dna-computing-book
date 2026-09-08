# Chapter 2 source and reconstruction ledger

Author-agent primary-source audit, 8 September 2026. This is not independent specialist review. The storyboard preceded prose. Historical facts, original deductions, and synthetic program output are deliberately separated.

## Historical anchor: directly inspected

Leonard M. Adleman, *Molecular computation of solutions to combinatorial problems*, Science 266 (1994), 1021–1024. [Primary-paper scan](https://computingbiology.github.io/docs/adleman1994.pdf). Read relevant article in full, including notes 4–9; inspected Fig. 1 and Fig. 2 in a high-resolution local rendering. The scan also contains unrelated adjacent articles; those are not sources.

- Fig. 1: V={0,1,2,3,4,5,6}, s=0, t=6. E={(0,1),(0,3),(0,6),(1,2),(1,3),(2,1),(2,3),(3,2),(3,4),(4,1),(4,5),(5,1),(5,2),(5,6)}. Original redrawing, not a reproduced figure. Independent permutation enumeration gives only 0,1,2,3,4,5,6.
- Fig. 2 prints O2=TATCGGATCGGTATATCCGA, O3=GCTATTCGAGCTTAAAGCTA, O4=GGCTAGGTACCAGCATGCTT, all 5′→3′. No complete historical seven-code list is invented. Internal edge fragments are R_i L_j; complementary vertex strands are splints. Terminal edges use whole start/end codes.
- Note 4: 50 pmol of each edge oligo and internal vertex complement; 100 µL ligation mixture; four hours at room temperature. These are historical inventory facts, not a current laboratory protocol.
- Steps 2–3: endpoint PCR using O0 and complementary O6; 140-bp gel fraction, with repeated amplification/purification. The logical program collapses these physical repetitions into predicates.
- Note 7: biotinylated complementary O6 labels one PCR strand. Immobilization and denaturation recover the other strand in solution. Subsequently, bead-bound biotinylated complementary vertex probes recognize targets; washing removes unbound material; denaturation recovers retained target. Repeat internal vertices 1–5. Biotin is the attachment, not the sequence recognizer.
- Graduated PCR uses O0 plus complementary Oi in separate reactions. Product sizes support vertex positions; this is not modern sequencing. The paper discusses unwanted paths, imperfect separation, and seven days of laboratory work.

## Mechanism sources and limits

1. [Alberts et al., DNA structure](https://www.ncbi.nlm.nih.gov/books/NBK26821/): direction, complementary antiparallel strands and backbone. Read relevant structural explanation; no obsolete genome-size claims used.
2. [NEB T4 DNA ligase](https://www.neb.com/en-us/products/m0202-t4-dna-ligase): directly read description of phosphodiester joining at juxtaposed 3′ OH / 5′ phosphate ends in duplex substrate. No vendor superiority claim or modern recipe imported into 1994 history.
3. [NHGRI PCR fact sheet](https://www.genome.gov/about-genomics/fact-sheets/Polymerase-Chain-Reaction-Fact-Sheet) and [electrophoresis](https://www.genome.gov/genetics-glossary/Electrophoresis): general mechanism only; amplification is not a perfect logical predicate and mobility is not simulated.
4. [SantaLucia 1998](https://pmc.ncbi.nlm.nih.gov/articles/PMC19045/): abstract/background on nearest-neighbor thermodynamics; used only to motivate sequence-context and solution-condition dependence. No parameters or free-energy predictions implemented here.
5. [BIPM mole](https://www.bipm.org/en/si-base-units/mole): exact Avogadro constant. The original conversion counts reagent molecules, not completed routes.

## Later work: narrow conceptual anchors

- [Lipton 1995](https://pubmed.ncbi.nlm.nih.gov/7725098/), abstract: SAT-style molecular search proposal, not reported here as a performed SAT experiment.
- [Boneh et al. 1996](https://crypto.stanford.edu/~dabo/pubs/abstracts/biocircuit.html): formal computational power, not an experimentally achieved general-purpose machine.
- Benenson et al. 2001, Nature 414, 430–434: abstract-level molecular automaton anchor; existing Chapter 1 bibliography.
- [Winfree et al. 1998](https://authors.library.caltech.edu/records/snfgz-51t15): abstract-level two-dimensional assembly anchor; existing Chapter 1 bibliography.
- [Seelig et al. 2006](https://authors.library.caltech.edu/records/vf8a9-45s13): abstract-level enzyme-free logic / strand-displacement anchor. The figure is a comparison of mechanisms, not a causal genealogy.

## Original work, not historical measurements

All bounded-walk counts, injected pseudo-paths, occurrence-to-band projections, sensitivity calculations, factorial examples, diagrams and proofs are original educational constructions. The legal-walk inventory stops at eight vertices; the real chemistry has no corresponding hard cutoff. No simulation estimates kinetic rates, yields, gel intensities, sequence orthogonality, or a probability of success for the historical experiment. The worked readout is a position projection, not a claim that all predicted bands must be experimentally visible.
