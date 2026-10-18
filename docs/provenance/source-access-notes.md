# Source-access notes (archived from chapter sources)

These notes were moved out of the reader-facing book on 2026-10-18 when the per-chapter
bibliographies were unified into `book/backmatter/references.bib`. They record how deeply each
source was inspected by earlier authoring passes. They are provenance, not reader text; the
original files remain in Git history.

## Chapters 1-3 (opening bibliography)

```latex
\begin{thebibliography}{99}
\addcontentsline{toc}{chapter}{Bibliography}
\bibitem{adleman} Leonard M. Adleman. Molecular computation of solutions to combinatorial problems. Science 266 (1994), 1021--1024. \href{https://computingbiology.github.io/docs/adleman1994.pdf}{Source link}.

\bibitem{dna} Bruce Alberts et al. The Structure and Function of DNA. Molecular Biology of the Cell, 4th edition (2002). \href{https://www.ncbi.nlm.nih.gov/books/NBK26821/}{Source link}.

\bibitem{ligase} New England Biolabs. T4 DNA Ligase, product description. \href{https://www.neb.com/en-us/products/m0202-t4-dna-ligase}{Source link}.

\bibitem{pcr} National Human Genome Research Institute. Polymerase Chain Reaction Fact Sheet. \href{https://www.genome.gov/about-genomics/fact-sheets/Polymerase-Chain-Reaction-Fact-Sheet}{Source link}.

\bibitem{gel} National Human Genome Research Institute. Electrophoresis. \href{https://www.genome.gov/genetics-glossary/Electrophoresis}{Source link}.

\bibitem{hamilton} Frank Pfenning. Lecture 36: The Hamiltonian Path Problem. Carnegie Mellon University, 15-453. \href{https://www.cs.cmu.edu/~fp/courses/flac/lectures/lecture36.html}{Source link}.

\bibitem{si} Bureau International des Poids et Mesures. SI base unit: mole. \href{https://www.bipm.org/en/si-base-units/mole}{Source link}.

\bibitem{benenson} Yaakov Benenson et al. Programmable and autonomous computing machine made of biomolecules. Nature 414 (2001), 430--434. \href{https://www.nature.com/articles/35106533}{Source link}.

\bibitem{crn} David Soloveichik, Georg Seelig, and Erik Winfree. DNA as a universal substrate for chemical kinetics. PNAS 107 (2010), 5393--5398. \href{https://doi.org/10.1073/pnas.0909380107}{Source link}.

\bibitem{circuits} Lulu Qian and Erik Winfree. Scaling up digital circuit computation with DNA strand displacement cascades. Science 332 (2011), 1196--1201. \href{https://www.qianlab.caltech.edu/seesaw_digital_circuits2011.pdf}{Source link}.

\bibitem{assembly} Erik Winfree, Furong Liu, Lisa A. Wenzler, and Nadrian C. Seeman. Design and self-assembly of two-dimensional DNA crystals. Nature 394 (1998), 539--544. \href{https://www.nature.com/articles/28998}{Source link}.
\bibitem{d2santalucia} John SantaLucia Jr. A unified view of polymer, dumbbell, and oligonucleotide DNA nearest-neighbor thermodynamics. PNAS 95 (1998), 1460--1465. \href{https://pmc.ncbi.nlm.nih.gov/articles/PMC19045/}{Primary article}.

\bibitem{d2lipton} Richard J. Lipton. DNA solution of hard computational problems. Science 268 (1995), 542--545. \href{https://pubmed.ncbi.nlm.nih.gov/7725098/}{Primary abstract}.

\bibitem{d2boneh} Dan Boneh, Christopher Dunworth, Richard J. Lipton and Jiri Sgall. On the computational power of DNA. Discrete Applied Mathematics 71 (1996), 79--94. \href{https://crypto.stanford.edu/~dabo/pubs/abstracts/biocircuit.html}{Author publication record}.

\bibitem{d2seelig} Georg Seelig, David Soloveichik, David Y. Zhang and Erik Winfree. Enzyme-free nucleic acid logic circuits. Science 314 (2006), 1585--1588. \href{https://authors.library.caltech.edu/records/vf8a9-45s13}{Author manuscript record}.

\end{thebibliography}
```

## Chapter 4

```latex
\begin{thebibliography}{9}
\bibitem{bipm} Bureau International des Poids et Mesures. \emph{SI base unit: mole}. Official definition of amount of substance and the exact Avogadro constant. Accessed 13 September 2026. \url{https://www.bipm.org/en/si-base-units/mole}.
\bibitem{neb} New England Biolabs. \emph{DNA Ligation}. Manufacturer's explanation of nick sealing and ATP-dependent ligase chemistry. Accessed 13 September 2026. \url{https://www.neb.com/en/applications/cloning-and-synthetic-biology/dna-ligation}.
\end{thebibliography}
\section*{Evidence and illustration boundaries}
The probability derivations, numerical cases, code, and vector plates in this chapter are original teaching constructions. The sources above support the SI definition and the stated biochemical mechanism; they do not validate the chapter's hypothetical success probabilities, rate constant, or cost model. No experimental throughput, energy advantage, or universal complexity lower bound is asserted. Figures are mechanism schematics, not copied source artwork. Technical and visual checks by the authoring workflow do not constitute independent specialist review.
```

## Chapter 5

```latex
\renewcommand{\bibname}{Sources and reading notes}
\begin{thebibliography}{9}
\addcontentsline{toc}{chapter}{Sources and reading notes}
\bibitem{iupac-conformation}
IUPAC--IUB Joint Commission on Biochemical Nomenclature.
\emph{Abbreviations and Symbols for the Description of Conformations of
Polynucleotide Chains}, Recommendations 1982, published 1983.
\url{https://iupac.qmul.ac.uk/misc/pnuc1.html}.
Relevant nomenclature body inspected: atom numbering, chain direction,
and internucleotide connectivity. Our drawings are simplified topological
projections, not reproductions of the source figures.

\bibitem{iupac-symbols}
IUPAC--IUB. \emph{Abbreviations and Symbols for Nucleic Acids,
Polynucleotides and their Constituents}, Recommendations 1970.
\url{https://iupac.qmul.ac.uk/misc/naabb.html}.
Relevant nucleoside/nucleotide and phosphate-position conventions inspected.
Modern ambiguity symbols are taken from INSDC, not inferred from this
historical nomenclature document.

\bibitem{nhgri}
National Human Genome Research Institute.
\emph{Deoxyribonucleic Acid (DNA) Fact Sheet}, updated 24 August 2020.
\url{https://www.genome.gov/about-genomics/fact-sheets/Deoxyribonucleic-Acid-Fact-Sheet}.
Full fact-sheet body inspected. Used for basic components, complementary
pairing, and opposing strand directions; not as a quantitative binding model.

\bibitem{insdc}
International Nucleotide Sequence Database Collaboration.
\emph{Feature Table Definition}, Appendix 7.4.1, nucleotide base codes.
\url{https://www.insdc.org/submitting-standards/feature-table/}.
The complete relevant base-code appendix was inspected. The generated table
and set-complement algorithm are our own implementation of those code meanings.

\bibitem{stacking}
P. Yakovchuk, E. Protozanova, and M. D. Frank-Kamenetskii (2006).
Base-stacking and base-pairing contributions into thermal stability of the
DNA double helix. \emph{Nucleic Acids Research} 34(2), 564--574.
\url{https://doi.org/10.1093/nar/gkj454}.
Access was limited to indexed article text; direct PMC access encountered
a challenge page. Used only for the qualitative distinction between
stacking and pairing, not numerical parameter values.

\bibitem{stacking-correction}
Correction notice for the preceding article (2006).
\emph{Nucleic Acids Research} 34(3), 1082.
\url{https://doi.org/10.1093/nar/gkj523}.
The indexed notice reports errors in Figures 5--8 and republication.
We did not independently revalidate the corrected figures and reproduce
none of their curves, values, or decompositions.
\end{thebibliography}
```

## Chapter 6

```latex
\renewcommand{\bibname}{Sources and reading notes}
\begin{thebibliography}{9}
\addcontentsline{toc}{chapter}{Sources and reading notes}
\bibitem{santalucia}
John SantaLucia Jr. (1998). A unified view of polymer, dumbbell, and
oligonucleotide DNA nearest-neighbor thermodynamics.
\emph{PNAS} 95(4), 1460--1465.
\url{https://doi.org/10.1073/pnas.95.4.1460}.
Relevant full-text background, Table 2, and melting-concentration discussion
inspected through PMC and the Caltech-hosted paper on 19 September 2026:
\url{https://www.dna.caltech.edu/courses/cs191/paperscs191/santalucia1998a.pdf}.
The numerical implementation uses one internally consistent Table 2
convention at 1 M NaCl. It does not implement salt corrections, mismatches,
self-complementary association, or a competing-structure ensemble.

\bibitem{nupack}
NUPACK 4.0 User Guide. \emph{Model Specification}.
\url{https://docs.nupack.org/model/}.
Material, ensemble, temperature, and salt sections inspected on
19 September 2026. Used to explain why physical-model settings and parameter
versions must be explicit. NUPACK was not executed and its predictions were
not used as experimental validation of this chapter's restricted code.
\end{thebibliography}
```

## Chapter 7

```latex
\renewcommand{\bibname}{Sources and reading notes}
\begin{thebibliography}{9}
\bibitem{gillespie} Daniel T. Gillespie (1977).
Exact stochastic simulation of coupled chemical reactions.
\emph{The Journal of Physical Chemistry} 81(25), 2340--2361.
\url{https://doi.org/10.1021/j100540a008}.
Primary-paper copy: \url{https://sites.chemengr.ucsb.edu/~ceweb/courses/che154/pdf/Gillespie_JPhysChem_1977.pdf}.
Introduction, molecular-count formulation, and Section III's direct
simulation construction inspected on 19 September 2026.
The paper supports the event-sampling framework, not the assigned
DNA association rates or an experimental validation of this chapter.
\end{thebibliography}

\section*{Calculation scope}
The closed-form reversible-binding derivation, implementation, numerical
convergence experiment, finite-pool detailed-balance oracle, one-pair
counterexample, and figures are original teaching artifacts.
No published experimental trajectory or benchmark is reproduced.
The stated rates are illustrative inputs. The whole Gillespie paper's
experimental examples were not reviewed for this chapter.
```

## Chapter 8

```latex
\chapter*{Sources and further reading}
\addcontentsline{toc}{chapter}{Sources and further reading}
Vendor descriptions were inspected for substrate specificity, directionality, and activity qualifications, not for the assigned rates. The ligase paper's abstract and introduction were inspected for the adenylation mechanism. The cited IUBMB sections were inspected for kinetic definitions and transient versus steady-state rates. Access checked 20 September 2026.

\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{ecori} New England Biolabs. \emph{EcoRI}, R0101: recognition site, cleavage position, and specificity qualifications.
\url{https://www.neb.com/en-us/products/r0101-ecori}.
\bibitem{ligase} New England Biolabs. \emph{T4 DNA Ligase}, M0202: substrate and cofactor description.
\url{https://www.neb.com/en/products/m0202-t4-dna-ligase}.
\bibitem{ligasemechanism} K. Shi et al. \emph{T4 DNA ligase structure reveals a prototypical ATP-dependent ligase with a unique mode of sliding clamp interaction}. Nucleic Acids Research 46(19), 10474--10488 (2018).
\url{https://doi.org/10.1093/nar/gky776}.
\bibitem{polymerase} New England Biolabs. \emph{T4 DNA Polymerase}, M0203: direction, primer requirement, and exonuclease activity.
\url{https://www.neb.com/products/m0203-t4-dna-polymerase}.
\bibitem{kinetics} IUBMB. \emph{Symbolism and Terminology in Enzyme Kinetics} (1981), sections 4.1--4.2.
\url{https://iubmb.qmul.ac.uk/kinetics/ek4t6.html}.
\bibitem{transient} IUBMB. \emph{Symbolism and Terminology in Enzyme Kinetics} (1981), introductory definitions of steady-state and transient behavior.
\url{https://iubmb.qmul.ac.uk/kinetics/ek1t3.html}.
\end{thebibliography}
\endgroup
```

## Chapter 9

```latex
\chapter*{Sources and further reading}
\addcontentsline{toc}{chapter}{Sources and further reading}
The NEB application overview was inspected for the physical cycle and template reuse. The Svec paper's PubMed abstract and bibliographic record were inspected for the scope of efficiency-estimation uncertainty; direct PMC access presented a browser challenge. Its experimental data and detailed methods are not reproduced. Access checked 20 September 2026.

The endpoint recurrence, resource ledger, probability examples, and threshold counterexamples are explicitly derived teaching models. Their idealizations are stated where used; no measured amplification curve is supplied.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{neb} New England Biolabs. \emph{PCR: Application Overview}. Denaturation, annealing, extension, and reuse of newly synthesized templates. \url{https://www.neb.com/en/applications/dna-amplification-pcr-and-qpcr/pcr}.
\bibitem{svec} D. Svec, A. Tichopad, V. Novosadova, M. W. Pfaffl, and M. Kubista. \emph{How good is a PCR efficiency estimate: Recommendations for precise and robust qPCR efficiency assessments}. Biomolecular Detection and Quantification 3, 9--16 (2015). \url{https://doi.org/10.1016/j.bdq.2015.01.005}. Abstract inspected at \url{https://pubmed.ncbi.nlm.nih.gov/27077029/}.
\end{thebibliography}
\endgroup
```

## Chapter 10

```latex
\chapter*{Sources and further reading}
\addcontentsline{toc}{chapter}{Sources and further reading}
Access checked 21 September 2026. Addgene's introduction, analysis section,
and separation FAQ were inspected for migration direction and ladder use.
NEB's complete short FAQ was inspected for topology-dependent bands.
The Qubit guide's product description, calibration and selectivity sections
on pages 1--2 were inspected. No manufacturer performance data are reproduced.

The local log-length ruler, Gaussian profiles, response matrices, uncertainty
calculations and collection curves are explicit teaching models. They are not
fitted instrument data or a universal laboratory protocol.

\begingroup
\let\chapter\section
\begin{thebibliography}{9}
\bibitem{addgene} Addgene. \emph{Agarose Gel Electrophoresis}. Laboratory guide,
updated 20 February 2018.
\url{https://www.addgene.org/protocols/gel-electrophoresis/}.
\bibitem{neb} New England Biolabs. \emph{What are the additional bands I see on the gel?}
Technical FAQ.
\url{https://www.neb.com/en/faqs/what-are-the-additional-bands-i-see-on-the-gel}.
\bibitem{qubit} Thermo Fisher Scientific. \emph{Qubit dsDNA HS Assay Kit User Guide}.
Publication MAN0002326, revision C.0, pp. 1--2.
\url{https://www.thermofisher.com/TFS-Assets/LSG/manuals/Qubit_dsDNA_HS_Assay_UG.pdf}.
\end{thebibliography}
\endgroup
```

## Chapter 11

```latex
\chapter*{Sources and further reading}
\addcontentsline{toc}{chapter}{Sources and further reading}
Access checked 24 September 2026. NUPACK 4.0 definitions were inspected for
sequence orientation, secondary structure, design formulation and tube versus
complex design. Adleman's original article, pp.~1021--1022, was inspected for
edge encoding and splint geometry. No full NUPACK design calculation was run.
Our short words, constraint solver, codec and tests are teaching constructions;
their correctness does not establish physical selectivity.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{nupack} NUPACK authors. \emph{NUPACK 4.0 User Guide: Definitions}.
\url{https://docs.nupack.org/definitions/}.
\bibitem{adleman} L. M. Adleman. \emph{Molecular Computation of Solutions to
Combinatorial Problems}. Science 266, 1021--1024 (1994).
\url{https://doi.org/10.1126/science.7973651}.
Inspected article copy:
\url{https://computingbiology.github.io/docs/adleman1994.pdf}.
\end{thebibliography}\endgroup
```

## Chapter 12

```latex
\chapter*{Sources and further reading}
\addcontentsline{toc}{chapter}{Sources and further reading}
Access checked 24 September 2026. The original Adleman paper's algorithm and
its description of generation, endpoint selection, length selection and
affinity purification on pp.~1021--1022 were inspected.
The finite Counter model, proofs, assigned loss probabilities, capacity
counterexample and cost comparison here are original teaching artifacts.
They are not measurements or a reconstruction of the experiment.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{adleman} L. M. Adleman. \emph{Molecular Computation of Solutions to
Combinatorial Problems}. Science 266, 1021--1024 (1994).
\url{https://doi.org/10.1126/science.7973651}.
Inspected article copy:
\url{https://computingbiology.github.io/docs/adleman1994.pdf}.
\end{thebibliography}\endgroup
```

## Chapter 13

```latex
\chapter*{Sources and evidence notes}
\addcontentsline{toc}{chapter}{Sources and evidence notes}
Access checked 24 September 2026. Lipton's bibliographic record and abstract
were inspected, not the full article. The CNF construction, finite-copy
proof, coverage calculation and reference tests are original teaching
artifacts, not a claim to reproduce that paper's full method.
The 2026 paper's main-text programming, renewal and scale-up sections were
inspected; supplementary notes were not independently audited.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{lipton} R. J. Lipton. DNA solution of hard computational problems.
\emph{Science} 268(5210), 542--545 (1995).
DOI: 10.1126/science.7725098.
\url{https://pubmed.ncbi.nlm.nih.gov/7725098/}.
\bibitem{sdc} T. Stérin, A. Eshra, C. G. Evans, J. Adio and D. Woods.
A thermodynamically favoured molecular computer.
\emph{Nature} 657, 646--652 (2026), published 16 September.
\url{https://doi.org/10.1038/s41586-026-10996-5}.
\end{thebibliography}
\endgroup
Numerical outputs in this chapter are model outputs, not laboratory data.
A current-paper comparison is not an industrial performance benchmark.
```

## Chapter 14

```latex
\chapter*{Sources and evidence notes}
\addcontentsline{toc}{chapter}{Sources and evidence notes}
Access checked 24 September 2026. The Caltech record and submitted sticker
manuscript's printed pages 1--2 (PDF pages 2--3), covering representation
and formal operations, were visually inspected. Text extraction from this
older PDF was unreliable. Its physical-implementation sections were not
audited; no selective-clear protocol is claimed here.
The 2026 paper's main-text renewal and scale-up sections were inspected.
The register algebra, AND reference, error calculations and exercises are
original derivations under explicitly idealized operations.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{stickers} S. Roweis, E. Winfree, R. Burgoyne, N. V. Chelyapov,
M. F. Goodman, P. W. K. Rothemund and L. M. Adleman.
A sticker-based model for DNA computation.
\emph{Journal of Computational Biology} 5(4), 615--629 (1998).
DOI: 10.1089/cmb.1998.5.615.
\url{https://authors.library.caltech.edu/records/jvmmc-dtb97}.
Submitted manuscript:
\url{https://authors.library.caltech.edu/records/jvmmc-dtb97/files/stickers_1_.pdf}.
\bibitem{sdc} T. Stérin, A. Eshra, C. G. Evans, J. Adio and D. Woods.
A thermodynamically favoured molecular computer.
\emph{Nature} 657, 646--652 (2026).
\url{https://doi.org/10.1038/s41586-026-10996-5}.
\end{thebibliography}
\endgroup
Assigned retention probabilities are illustrative, not fitted or measured
sticker-system performance. Logical operations do not establish laboratory
feasibility.
```

## Chapter 15

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
The splicing convention was checked against the introduction and definitions in
Kari and Ng's arXiv version 1 on 24 September 2026. The two-product inventory,
examples, explorer and tests are original teaching constructions. No claim about
the complete generative-power hierarchy is needed for those constructions.
NEB's current insert-design guidance was inspected for orientation and end-design
constraints; no experimental assembly was performed. The historical Head paper
was located bibliographically, not used as an inspected full-text protocol.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{splicing} L. Kari and T. Ng.
\emph{Descriptional Complexity of Semi-Simple Splicing Systems}.
arXiv:1909.02512v1, 2019. Introduction and Sections 2--3.
\url{https://arxiv.org/html/1909.02512v1}.
\bibitem{neb} New England Biolabs.
\emph{Insert Considerations for NEBridge Golden Gate Assembly Kit (BsmBI-v2)}.
Current technical guidance, accessed 24 September 2026.
\url{https://www.neb.com/en/tools-and-resources/usage-guidelines/insert-considerations-for-neb-golden-gate-assembly-kit-bsmbi-v2-neb-e1602}.
\end{thebibliography}\endgroup
```

## Chapter 16

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
The DFA, minimal-state argument, addition invariant, code and probability channel
are original worked examples of standard finite-state constructions.
The 2026 paper's main-text domain model and FSM-programming sections were
inspected on 24 September 2026. Its supplementary experimental data and detailed
base-level pathways were not independently reproduced. The chapter figure is
an original conceptual constraint diagram, not copied artwork or a strand design
suitable for synthesis. Assigned error and loss values are not measurements.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{sdc} T. St\'erin, A. Eshra, C. G. Evans, T. Adio and D. Woods.
\emph{A thermodynamically favoured molecular computer}.
Nature 657, 646--652, 16 September 2026.
\url{https://doi.org/10.1038/s41586-026-10996-5}.
\end{thebibliography}\endgroup
```

## Chapter 17

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
The presentation, reference code, worked derivations, generated tables and
illustrations are original teaching artifacts, not claims of new automata
theorems. Classical definitions and the cited experimental architectures
remain attributed below. On 25 September 2026 the Watson--Crick automata
paper's introduction, preliminaries, acceptance and determinism definitions
were inspected. Our empty-input and nonempty-transition conventions are
stated explicitly; no hierarchy theorem is transferred to this variant.
The Benenson paper's mechanism description and Figure 2 caption were inspected
in the author-course archive copy. The mechanism plate is an original
conceptual abstraction, not a reproduction, sequence design or wet-lab protocol.
The Adar paper's abstract and Results discussion of competing transitions
and calibrated programming were inspected. The 2003 Benenson paper was
available here at abstract depth only; its reuse claim is the limited point
used. We do not reconstruct either experiment or import their performance
numbers. The renewal/race and parity-noise examples are declared mathematical
models with assigned parameters. Computed configurations and probabilities
are not measured chemical trajectories. Specialist scientific review and
reader testing remain open; author checks do not replace them.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{czeizler} E. Czeizler, E. Czeizler, L. Kari and K. Salomaa.
\emph{On the descriptional complexity of Watson--Crick automata}.
Theoretical Computer Science 410 (2009), 3250--3260.
\url{https://doi.org/10.1016/j.tcs.2009.05.001}.
Author copy: \url{https://cs.uwaterloo.ca/~lila/pdfs/Watson_Crick_automata.pdf}.
\bibitem{benenson} Y. Benenson, T. Paz-Elizur, R. Adar, E. Keinan,
Z. Livneh and E. Shapiro.
\emph{Programmable and autonomous computing machine made of biomolecules}.
Nature 414 (2001), 430--434.
\url{https://doi.org/10.1038/35106533}.
Mechanism inspected in the Duke molecular-computing course archive copy.
\bibitem{fuel} Y. Benenson, R. Adar, T. Paz-Elizur, Z. Livneh and E. Shapiro.
\emph{DNA molecule provides a computing machine with both data and fuel}.
Proceedings of the National Academy of Sciences 100 (2003), 2191--2196.
\url{https://doi.org/10.1073/pnas.0535624100}.
Abstract: \url{https://pubmed.ncbi.nlm.nih.gov/12601148/}.
\bibitem{adar} R. Adar, Y. Benenson, G. Linshiz, A. Rosner,
N. Tishby and E. Shapiro.
\emph{Stochastic computing with biomolecular automata}.
Proceedings of the National Academy of Sciences 101 (2004), 9960--9965.
\url{https://doi.org/10.1073/pnas.0400731101}.
Open text: \url{https://pmc.ncbi.nlm.nih.gov/articles/PMC454388/}.
\end{thebibliography}\endgroup
```

## Chapter 18

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
The increment proof, two-stack simulation invariant, reference implementations,
generated plots and exercises are original. The contemporary comparison is
limited to the finite-state compilation and kinetic-condition discussion in
the main text of Stérin and colleagues, inspected on 25 September 2026.
We do not claim to reproduce the experiment or to establish unbounded
universality from its bounded demonstrations. The error probability is assigned
for illustration; no chemical fidelity measurements were collected.
The code's tests and author review remain distinct from independent
scientific review.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{sterin} T. Stérin, A. Eshra, C. G. Evans, T. Adio and D. Woods.
\emph{A thermodynamically favoured molecular computer}.
Nature 657 (2026), 646--652. Published 16 September 2026.
\url{https://doi.org/10.1038/s41586-026-10996-5}.
\end{thebibliography}\endgroup
```

## Chapter 19

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Access checked 27 September 2026. Srinivas et al.: abstract, introduction,
mechanism caption and the intuitive-energy-landscape state/rate discussion
inspected in the publisher text. Zhang and Winfree: abstract and publication
metadata inspected; detailed sequences and supplementary calibration were not
reconstructed. Soloveichik et al.: abstract-level scope of the reaction-network
construction. Stérin et al.: publisher-indexed main text and design-principle
discussion inspected; no independent experimental reproduction or supplementary
proof audit. These access levels bound the claims made here.

The boundary-value derivations, assigned-rate examples, executable references,
vector plates and worked exercises are original teaching artifacts, not claims
to have invented first-passage theory. Author checks and numerical tests do not
replace independent scientific review. No wet-lab timings or yields are supplied.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{srinivas} N. Srinivas et al. \emph{On the biophysics and kinetics of
toehold-mediated DNA strand displacement}. Nucleic Acids Research 41 (2013),
10641--10658. \url{https://doi.org/10.1093/nar/gkt801}.
\bibitem{zhang} D. Y. Zhang and E. Winfree. \emph{Control of DNA strand
displacement kinetics using toehold exchange}. Journal of the American Chemical
Society 131 (2009), 17303--17314. \url{https://doi.org/10.1021/ja906987s}.
\bibitem{crn} D. Soloveichik, G. Seelig and E. Winfree. \emph{DNA as a universal
substrate for chemical kinetics}. Proceedings of the National Academy of
Sciences 107 (2010), 5393--5398. \url{https://doi.org/10.1073/pnas.0909380107}.
\bibitem{sterin} T. Stérin, A. Eshra, C. G. Evans, J. Adio and D. Woods.
\emph{A thermodynamically favoured molecular computer}. Nature 657 (2026),
646--652. Published 16 September 2026.
\url{https://doi.org/10.1038/s41586-026-10996-5}.
\end{thebibliography}\endgroup
```

## Chapter 20

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Access checked 27 September 2026. Soloveichik et al.: Caltech author-repository
abstract and publication metadata inspected; the full sequence construction
and supplement were not reconstructed. Chen et al.: author-hosted abstract,
introduction excerpt and arXiv abstract inspected for the count-valued
stable-computation characterization; the full characterization proof is not
reproduced here. Kini and Doty: arXiv abstract and author publication list
inspected for the reverse-before-cutoff model and stated result. We do not
claim to have replicated these research implementations or proofs.

All numerical rates in this chapter are assigned reference parameters;
computed trajectories and completion times are not experimental measurements.

\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{soloveichik} D. Soloveichik, G. Seelig and E. Winfree.
\emph{DNA as a universal substrate for chemical kinetics}.
Proceedings of the National Academy of Sciences 107 (2010), 5393--5398.
\url{https://doi.org/10.1073/pnas.0909380107}.
\bibitem{chen} H.-L. Chen, D. Doty and D. Soloveichik.
\emph{Deterministic function computation with chemical reaction networks}.
Natural Computing 13 (2014), 517--534.
Author manuscript: \url{https://arxiv.org/abs/1204.4176}.
\bibitem{kini} R. Kini and D. Doty.
\emph{Reverse-Robust Computation with Chemical Reaction Networks}.
DNA 2026, LIPIcs 387, Article 6.
Preprint: \url{https://arxiv.org/abs/2604.14355}.
\end{thebibliography}\endgroup
```

## Chapter 21

```latex
\clearpage
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Access checked 27 September 2026. The author-hosted Qian--Winfree paper was
inspected for threshold capture, the catalytic exchange cycle, integrating and
amplifying gates, and the distinction between gross release and free signal.
Its supplementary sequence designs and experiments were not reproduced.
The heat-rechargeable study was inspected at author-repository abstract and
publication-metadata level; its detailed reset mechanism is not reconstructed
here. All code outputs in this chapter use assigned reference parameters.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{qian} L. Qian and E. Winfree.
\emph{Scaling Up Digital Circuit Computation with DNA Strand Displacement Cascades}.
Science 332 (2011), 1196--1201.
\url{https://doi.org/10.1126/science.1200520}.
\bibitem{heat} T. Song and L. Qian.
\emph{Heat-rechargeable computation in DNA logic circuits and neural networks}.
Nature 646 (2025), 315--322.
\url{https://doi.org/10.1038/s41586-025-09570-2}.
\end{thebibliography}\endgroup
```

## Chapter 22

```latex
\clearpage
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Local verification on 6 October 2026 distinguishes access from reproduction.
The Sierpiński paper's abstract, model discussion and molecular-schema discussion
were inspected in publisher HTML; experimental images and protocols were not
independently reproduced. The author-hosted origami paper was inspected for its
abstract and scaffold/staple design discussion, including crossover geometry.
Evans--Winfree was available through the publisher's indexed abstract and metadata;
full-text access failed in this check. Proofreading was checked at author-index
and abstract level only. The local finite-grid proof, cut oracle, exploration,
assigned-rate race and original diagrams are teaching artifacts, not new wet-lab
results or independent specialist review.
\begingroup\let\chapter\section
\begin{thebibliography}{9}
\bibitem{sierpinski} P. W. K. Rothemund, N. Papadakis and E. Winfree.
\emph{Algorithmic Self-Assembly of DNA Sierpinski Triangles}.
PLOS Biology 2 (2004), e424.
\url{https://doi.org/10.1371/journal.pbio.0020424}.
\bibitem{origami} P. W. K. Rothemund.
\emph{Folding DNA to create nanoscale shapes and patterns}.
Nature 440 (2006), 297--302.
\url{https://doi.org/10.1038/nature04586}.
Author-hosted paper: \url{https://www.dna.caltech.edu/Papers/DNAorigami-nature.pdf}.
\bibitem{tilephysics} C. G. Evans and E. Winfree.
\emph{Physical principles for DNA tile self-assembly}.
Chemical Society Reviews 46 (2017), 3808--3829.
\url{https://doi.org/10.1039/C6CS00745G}.
\bibitem{proofreading} E. Winfree and R. Bekbolatov.
\emph{Proofreading Tile Sets: Error Correction for Algorithmic Self-Assembly}.
DNA Computing 9, LNCS 2943 (2004), 126--144.
\url{https://www.dna.caltech.edu/Papers/proofreading_DNA9.pdf}.
\end{thebibliography}\endgroup
```

## Chapter 23

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Local access checks on 6 October 2026 distinguish reference verification from
experimental replication. The proofreading author PDF was inspected for
Section 3 and its limitation discussion (PDF pages 10 and 16--17); the facet
paper's abstract and mechanism/results passages were inspected in its author PDF.
The redundancy result was checked against its PubMed-indexed primary abstract.
The origami source was checked in publisher HTML, abstract and introductory
off-target discussion. No experiment, image analysis or parameter fit was
independently repeated here.

Two incoming bibliographic errors were corrected: the facet paper is by
Chen, Schulman, Goel and Winfree in \emph{Nano Letters}, not the separately
published PNAS nucleation paper; the 2026 origami paper's lead author is
Shirt-Ediss. Original probability derivations, code and figures remain teaching
artifacts. Independent specialist and reader review are open.

\begin{thebibliography}{9}
\bibitem{proofreading2004} E. Winfree and R. Bekbolatov.
\emph{Proofreading Tile Sets: Error Correction for Algorithmic Self-Assembly}.
DNA Computing 9, LNCS 2943 (2004), 126--144.
\url{https://www.dna.caltech.edu/Papers/proofreading_DNA9.pdf}.
\bibitem{facet2007} H.-L. Chen, R. Schulman, A. Goel and E. Winfree.
\emph{Reducing Facet Nucleation during Algorithmic Self-Assembly}.
Nano Letters 7 (2007), 2913--2919.
\url{https://doi.org/10.1021/nl070793o}.
Author PDF: \url{https://www.dna.caltech.edu/Papers/snaked_DNA_2007.pdf}.
\bibitem{redundancy2015} R. Schulman, C. Wright and E. Winfree.
\emph{Increasing Redundancy Exponentially Reduces Error Rates during Algorithmic
Self-Assembly}. ACS Nano 9 (2015), 5760--5771.
\url{https://doi.org/10.1021/nn507493s}.
Abstract: \url{https://pubmed.ncbi.nlm.nih.gov/25965580/}.
\bibitem{origami2026} B. Shirt-Ediss et al.
\emph{Optimising DNA origami assembly by reducing off-target interactions}.
Nature Communications 17 (2026), article 6859; published 26 May 2026.
\url{https://doi.org/10.1038/s41467-026-73387-4}.
\end{thebibliography}
```

## Chapter 24

```latex
\section*{Sources and evidence}
\addcontentsline{toc}{section}{Sources and evidence}
Primary access checks on 6 October 2026 cover Boneh's author publication abstract,
the BIPM mole definition, and Landauer's scanned primary reprint, selected
Sections 3--4 and the start of Section 5 (reprint pages 264--266).
No molecular resource measurement or thermodynamic experiment was reproduced.
The occupancy, completion, transport and detection calculations are explicit
teaching models; assigned parameters do not become measured DNA rates.
Independent scientific review remains open.

\begin{thebibliography}{9}
\bibitem{dnad24:boneh} D. Boneh, C. Dunworth, R. J. Lipton and J. Sgall.
\emph{On the computational power of DNA}.
Discrete Applied Mathematics 71 (1996), 79--94.
Author abstract and publication record:
\url{https://crypto.stanford.edu/~dabo/pubs/abstracts/biocircuit.html}.
\bibitem{dnad24:si} Bureau International des Poids et Mesures.
\emph{SI base unit: mole (mol)}. Official SI definition, accessed 6 October 2026.
\url{https://www.bipm.org/en/si-base-units/mole}.
\bibitem{dnad24:landauer} R. Landauer.
\emph{Irreversibility and Heat Generation in the Computing Process}.
IBM Journal of Research and Development 5 (1961), 183--191.
\url{https://doi.org/10.1147/rd.53.0183}.
Primary reprint, IBM Journal of Research and Development 44 (2000), 261--269:
\url{https://www.cpt.univ-mrs.fr/~verga/pdfs/Landauer-1961uq.pdf}.
\end{thebibliography}
```

## Chapter 25

```latex
\chapter*{Evidence and source boundaries}
The XOR code, framing trace, finite constrained-code implementation and independent
tests are teaching references, not a new storage architecture. Enumerative coding,
error correction and molecular storage have substantial prior art.
The raw byte archive is intentionally not sequence-constrained. The rank/unrank
code proves only its GC and run bounds. No primer validation, wet-lab recovery,
channel calibration or optimized production decoder is claimed.

Primary records were checked on 6 October 2026. Goldman and Organick were inspected
at publisher abstract/metadata depth (Organick's accessible primer-design captions
were also inspected). Chen et al. were read at abstract, introduction and selected
bias/model sections in the primary PMC article. Gimpel et al. were read at abstract
and selected introduction/initial error-analysis sections. Bar-Lev et al. were
inspected at abstract/data-code-availability depth; their correction explicitly
adds missing prior work to simulated-data methods. Li et al. were inspected at
abstract and selected codebook/overview/comparison sections, not all supplementary
proofs or experimental data. None of these studies was independently reproduced.

\begin{thebibliography}{99}
\bibitem{goldman} N. Goldman et al. Towards practical, high-capacity,
low-maintenance information storage in synthesized DNA.
\emph{Nature} 494, 77--80 (2013).
\url{https://doi.org/10.1038/nature11875}.
\bibitem{organick} L. Organick et al. Random access in large-scale DNA data storage.
\emph{Nature Biotechnology} 36, 242--248 (2018), corrected publisher record.
\url{https://doi.org/10.1038/nbt.4079}.
\bibitem{bias} Y.-J. Chen et al. Quantifying molecular bias in DNA data storage.
\emph{Nature Communications} 11, 3264 (2020).
\url{https://doi.org/10.1038/s41467-020-16958-3}.
\bibitem{twin} A. L. Gimpel, W. J. Stark, R. Heckel and R. N. Grass.
A digital twin for DNA data storage based on comprehensive quantification of errors
and biases. \emph{Nature Communications} 14, 6026 (2023).
\url{https://doi.org/10.1038/s41467-023-41729-1}.
\bibitem{deep-storage} D. Bar-Lev et al. Scalable and robust DNA-based storage via
coding theory and deep learning. \emph{Nature Machine Intelligence} 7, 639--649 (2025).
\url{https://doi.org/10.1038/s42256-025-01003-z}.
\bibitem{deep-correction} D. Bar-Lev et al. Author Correction to the preceding work.
Published 30 December 2025; \emph{Nature Machine Intelligence} 8, 134 (2026).
\url{https://doi.org/10.1038/s42256-025-01175-8}.
\bibitem{bijective} J. Li, M. Dong, Z. Qi and H. Guan.
Towards density-optimal DNA storage with practical bijective coding.
\emph{Nature Communications} 17, 10261 (2026).
\url{https://doi.org/10.1038/s41467-026-77024-y}.
\end{thebibliography}
```

## Chapter 26

```latex
\chapter*{Evidence and source boundaries}
The laboratory ledger, uncertainty arithmetic, preparation-level counterexample,
figures and exercises are original teaching artifacts. The ledger checks supplied
bytes and structural history, not the truth of observations or experimental replication.
FAIR introductory material and detailed principles were inspected; the origami
primer's publisher abstract and metadata were inspected, not its full methods.
Access depths and unresolved scientific review are recorded in the integration ledger.
\begin{thebibliography}{99}
\bibitem{Wilkinson2016} M. D. Wilkinson et al.
The FAIR Guiding Principles for scientific data management and stewardship.
\emph{Scientific Data} 3, 160018 (2016).
\url{https://doi.org/10.1038/sdata.2016.18}.
\bibitem{Dey2021} S. Dey et al. DNA origami.
\emph{Nature Reviews Methods Primers} 1, 13 (28 January 2021).
\url{https://doi.org/10.1038/s43586-020-00009-8}.
\end{thebibliography}
```

## Chapter 27

```latex
\chapter*{Evidence and source boundaries}
The finite-multiset engine, proofs for its stated search contract, independent
vector oracle, fixtures and conceptual molecular plates are original teaching
artifacts. They do not implement domain-level DNA chemistry or establish kinetic
or experimental adequacy. Cardelli inspection covers the author-hosted manuscript's
abstract and introduction (pages 1--3), not its full correspondence proofs.
Soloveichik et al. inspection covers selected primary rescaling, experimental
considerations and conclusion passages; no supplementary construction was replicated.
\begin{thebibliography}{99}
\bibitem{cardelli-site} L. Cardelli. On Process Rate Semantics.
Author-hosted manuscript, dated 13 December 2007 in its page footers;
author publication listing identifies the TCS 2008 publication.
\url{https://lucacardelli.name/Papers/On\%20Process\%20Rate\%20Semantics.pdf}.
\bibitem{soloveichik2010} D. Soloveichik, G. Seelig and E. Winfree.
DNA as a universal substrate for chemical kinetics.
\emph{PNAS} 107(12), 5393--5398 (2010).
\url{https://doi.org/10.1073/pnas.0909380107}.
\end{thebibliography}
```

## Chapter 28

```latex
\renewcommand{\bibname}{Sources and references}
\begin{thebibliography}{9}
\addcontentsline{toc}{chapter}{Sources and references}
\bibitem{gillespie1977} D. T. Gillespie.
Exact stochastic simulation of coupled chemical reactions.
\emph{Journal of Physical Chemistry} 81(25), 2340--2361 (1977).
\url{https://doi.org/10.1021/j100540a008}.
Publisher metadata and the primary paper's abstract/first page inspected;
historical attribution, not a claim of full-paper replication.
\bibitem{higham2008} D. J. Higham. Modeling and simulating chemical reactions.
\emph{SIAM Review} 50(2), 347--368 (2008).
\url{https://doi.org/10.1137/060666457}.
Primary introduction and selected Sections 4 and 7 inspected for the direct
method, concentration/count scaling, and identical-reactant convention.
No published code or artwork is reproduced.
\end{thebibliography}
The original executable reference and figures illustrate declared mathematical
models, not replicated chemical experiments. Selected primary access is recorded
in the integration source ledger.
```

## Chapter 29

```latex
\renewcommand{\bibname}{Sources and references}
\begin{thebibliography}{9}
\addcontentsline{toc}{chapter}{Sources and references}
\bibitem{dnad29:crn} A. Mordvintsev, E. Randazzo and E. Niklasson.
Differentiable Programming of Chemical Reaction Networks.
arXiv:2302.02714v1 (6 February 2023).
\url{https://arxiv.org/abs/2302.02714v1}.
Primary abstract/version inspected for abstract mass-action CRN optimization.
\bibitem{dnad29:seqprop} J. Linder and G. Seelig.
Fast activation maximization for molecular sequence design.
\emph{BMC Bioinformatics} 22, 510 (20 October 2021).
\url{https://doi.org/10.1186/s12859-021-04437-5}.
Selected primary background and activation-maximization sections inspected
for relaxed-input mismatch, straight-through rules and normalization.
\bibitem{dnad29:dga} K. Rijal and P. Mehta.
A differentiable Gillespie algorithm for simulating chemical kinetics,
parameter estimation, and designing synthetic biological circuits.
\emph{eLife} 14:RP103877, Version of Record (17 March 2025).
\url{https://doi.org/10.7554/eLife.103877.3}.
Publisher-indexed abstract and publication status inspected; direct article/PDF
requests encountered a client challenge. No full-text replication is claimed.
\bibitem{dnad29:icrn} I. Lee, S. Buse and E. Winfree.
Differentiable Programming of Indexed Chemical Reaction Networks and
Reaction-Diffusion Systems.
\emph{DNA 31, LIPIcs} 347, 4:1--4:23 (19 August 2025).
\url{https://doi.org/10.4230/LIPIcs.DNA.31.4}.
Proceedings metadata/abstract and selected formalism introduction inspected.
\end{thebibliography}
```

## Chapter 30

```latex
\begin{thebibliography}{9}
\addcontentsline{toc}{chapter}{Sources and references}
\bibitem{dnad30:toggle} T. S. Gardner, C. R. Cantor and J. J. Collins.
Construction of a genetic toggle switch in Escherichia coli.
\emph{Nature} 403, 339--342 (20 January 2000).
\url{https://doi.org/10.1038/35002131}.
Primary abstract and bibliographic metadata inspected; no device replication
or full experimental protocol inspection is claimed.
\bibitem{dnad30:abc} C. P. Fulco, J. Nasser, T. R. Jones et al.
Activity-by-contact model of enhancer--promoter regulation from thousands of
CRISPR perturbations. \emph{Nature Genetics} 51, 1664--1669
(29 November 2019).
\url{https://doi.org/10.1038/s41588-019-0538-0}.
Publisher-indexed abstract and metadata inspected; direct retrieval errors
prevented full-text verification. Used for the perturbation/prediction distinction,
not as a universal transcription law.
\bibitem{dnad30:lineage} C. Weinreb, A. Rodriguez-Fraticelli, F. D. Camargo
and A. M. Klein. Lineage tracing on transcriptional landscapes links state to
fate during differentiation. \emph{Science} 367, eaaw3381
(14 February 2020; online 23 January).
\url{https://doi.org/10.1126/science.aaw3381}.
Primary abstract and Figure 1--3 captions via PubMed inspected; not full methods
or a reproduction of the barcoding experiment.
\bibitem{dnad30:grn2026} R. J. Maizels and J. Briscoe.
Gene regulatory networks: from correlative models to causal explanations.
\emph{Nature Reviews Genetics} 27, 485--498
(June 2026; online 9 March).
\url{https://doi.org/10.1038/s41576-026-00939-1}.
Authors' perspective: primary abstract and selected Figure 1--4 captions via
PubMed inspected. Used as an explicitly labeled research agenda, not an
experimental validation or full-text replication.
\end{thebibliography}
```

## Chapter 31

```latex
\begin{thebibliography}{9}
\bibitem{dna31-soloveichik} D. Soloveichik, G. Seelig and E. Winfree.
DNA as a universal substrate for chemical kinetics.
\emph{PNAS} 107, 5393--5398 (2010).
\url{https://doi.org/10.1073/pnas.0909380107}.
Access: primary abstract and indexed publisher conclusion/experimental-considerations
excerpts; direct full-text retrieval was blocked. No supplementary-data replication.
\bibitem{dna31-fern} J. Fern and R. Schulman.
Design and Characterization of DNA Strand-Displacement Circuits in
Serum-Supplemented Cell Medium. \emph{ACS Synthetic Biology} (2017).
\url{https://doi.org/10.1021/acssynbio.7b00105}.
Access: publisher-indexed abstract; direct publisher retrieval was blocked.
\bibitem{dna31-zhong} W. Zhong and J. T. Sczepanski.
Direct Comparison of D-DNA and L-DNA Strand-Displacement Reactions in Living
Mammalian Cells. \emph{ACS Synthetic Biology} 10, 209--212 (2021).
\url{https://pubmed.ncbi.nlm.nih.gov/33347747/}.
Access: primary abstract and figure captions, not a full methods or supplementary-data audit.
\end{thebibliography}
```

## Chapter 32

```latex
\begin{thebibliography}{9}
\bibitem{dna32-adleman} L. M. Adleman. Molecular computation of solutions
to combinatorial problems. \emph{Science} 266, 1021--1024 (1994).
\url{https://doi.org/10.1126/science.7973651}.
Access: primary abstract at \url{https://pubmed.ncbi.nlm.nih.gov/7973651/};
not a full methods or supplementary-data audit.
\bibitem{dna32-soloveichik} D. Soloveichik, G. Seelig and E. Winfree.
DNA as a universal substrate for chemical kinetics.
\emph{PNAS} 107, 5393--5398 (2010).
\url{https://doi.org/10.1073/pnas.0909380107}.
Access: primary abstract and indexed publisher conclusion/experimental-considerations
excerpts, as recorded in Chapter 31; direct full-text retrieval was blocked.
\bibitem{dna32-internal} DNA Computing book, Chapters 30--31.
Regulatory context, finite-fuel reference dynamics and scoped evidence contracts.
Original fiber arguments, assigned scores, encodings and figures are teaching
artifacts, not experimental results.
\end{thebibliography}
```

## Chapter 3 (in-chapter source ledger, archived 2026-10-18)

```latex
\section{Appendix B. Sources and evidence
boundaries}\label{appendix-b.-sources-and-evidence-boundaries}

\subsection{Chapter 3 source ledger}\label{chapter-3-source-ledger}

\subsubsection{Review-candidate extension, 12 September
2026}\label{review-candidate-extension-12-september-2026}

The earlier entries below retain the access record of the first two
passes. The new work/depth and missing-signal examples are original
derivations with explicit assumptions, not laboratory measurements. For
the signal calculation, survival and detection are conditional
probabilities in a per-copy chain; independence is assumed across
candidate copies only when exponentiating the no-signal probability. The
implementation is checked against explicit two-copy enumeration,
boundary cases and a small-probability stability case.

MIT 6.046J Recitation 8 was rechecked for the split-vertex reduction.
This chapter proves that map and explicitly imports the hardness of
directed Hamiltonian cycle as a premise. It does not claim to supply the
entire Cook-Karp hardness chain. Figures F9-F12 separate abstract work,
molecular population, observation and proof obligations. All twelve
figures are produced; calibrated physical accounting and independent
scientific review remain open.

Consulted 9 September 2026. This ledger distinguishes directly read
support from located-but-unread material. It is not a systematic review
or independent approval.

\subsubsection{Directly read support}\label{directly-read-support}

\begin{itemize}
\tightlist
\item
  Michael Sipser, MIT 18.404J (2020),
  \href{https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/45e2fd621349cfd7c9faf93a6ba134a3_MIT18_404f20_lec14.pdf}{Lecture
  14: P and NP, SAT, polynomial-time reducibility}. The certificate,
  input-encoding and reduction discussion was read from the instructor's
  notes. Used for class conventions, not a proof of a separation between
  P and NP.
\item
  MIT 6.046J (2015),
  \href{https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/1dee182d301235b901119a0ff57f05e2_MIT6_046JS15_Recitation8.pdf}{Recitation
  8}, section 2, physical page 2. Read the directed-cycle-to-path
  vertex-splitting construction and both existence implications. Our
  original figure uses a three-cycle; the executable extension exposes
  fixed endpoints and arbitrary pivot relabeling. The source's naive
  verifier bounds are not substituted for our separately stated
  representation-aware account.
\item
  Sipser,
  \href{https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-15-np-completeness/}{Lecture
  15 resource and transcript}. Read the caution that directed
  3SAT-to-HAMPATH gadgets require internal consistency details. No
  incomplete gadget diagram was promoted to a complete proof in this
  draft.
\end{itemize}

\subsubsection{Located but not used as a fully read
proof}\label{located-but-not-used-as-a-fully-read-proof}

\begin{itemize}
\tightlist
\item
  Stephen Cook, \emph{The Complexity of Theorem-Proving Procedures}
  (1971):
  \href{https://www.cs.toronto.edu/~sacook/homepage/1971.pdf}{author-hosted
  scan}, linked from the author's publication list. The bibliographic
  record and abstract were read; the scan did not expose
  machine-readable text in the browser. No claim that the whole paper
  was read. Its original reduction formulation needs care before
  attributing a modern many-one statement verbatim to it.
\item
  Richard Karp, \emph{Reducibility Among Combinatorial Problems} (1972):
  bibliographic identification only in this pass. Obtain and read the
  original relevant construction before expanding the full hardness
  chain.
\end{itemize}

\subsubsection{Original derivations and
computations}\label{original-derivations-and-computations}

\paragraph{Second-pass source check}\label{second-pass-source-check}

Toronto CS 2401 (Fall 2015), instructor Toniann Pitassi, lecturer Thomas
Watson, scribe Benett Axtell:
\href{https://www.cs.toronto.edu/~toni/Courses/Complexity2015/lectures/lecture3.pdf}{Lecture
3}, section 4 on physical page 4. Read the definition of coNP through
language complementation, its universal-certificate formulation, and the
statement that P is closed under complementation. Used only for these
class conventions. The manuscript supplies its own deterministic
complement-closure argument. The scribe prose about ``flip the bits of
the witness'' is imprecise and is not copied or used as a proof: it is
the verifier predicate that must be negated under the changed
quantifier. No interactive-proof theorem is invoked.

Rechecked Sipser lecture 14's representation and complement question.
The new figures show explicit counting units and quantifiers, without a
separation diagram. The edge-deletion figure is generated from the
actual retained-graph trace; its test replays every step against
independent enumeration on all 4,096 four-vertex directed graphs.

The four-vertex instance, subset recurrence proof, dense reachable-state
count, elementary vertex-position CNF clause count and edge-deletion
self-reduction explanation are derived explicitly in the manuscript and
checked by the local reference. These are pedagogical reconstructions of
standard ideas, not claims of novel algorithms.

\texttt{reference.py} uses only Python's standard library. Its oracle
enumerates interior permutations independently of the subset algorithm.
Tests cover all 4,096 simple directed four-vertex graphs for existence
agreement, all 64 three-vertex graphs with all three reduction pivots,
and all 512 Boolean assignments per three-vertex CNF instance. Counts
are algorithmic counters, not timing data.

\subsubsection{Scope exclusions}\label{scope-exclusions}

No P-versus-NP resolution, best-known exact-algorithm claim, universal
molecular lower bound or new laboratory result. The full reduction
chain, deeper work/depth treatment and physical accounting remain
publication dependencies. Earlier historical/chemical details continue
to rely on the preserved Chapter 2 source ledger; this draft does not
re-report that work as new research.
```
