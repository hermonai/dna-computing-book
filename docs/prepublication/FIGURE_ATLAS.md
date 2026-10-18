# Figure atlas

All new plates are native TikZ using the shared visual language in
`book/visual.tex` (strand identity by colour plus a 3′ half-arrowhead; grey rungs
for base pairs; solid covalent bonds, dashed hydrogen bonds; distinct arrow
styles for reaction, reversible association, transfer, symbolic map,
observation and inhibition; fixed colours for DNA, RNA, protein, computation and
evidence). Every plate has a semantic TXT companion beside it. Natural widths
were measured; plates now print at 90–115% of natural size, so labels are about
8–10 pt (previously some older plates were enlarged up to 1.8×).

Review status: "inspected" means rendered standalone at 100–130 dpi and checked
for overlaps, orientation and scientific geometry; then seen in the built PDF.

## New or redrawn plates

| Plate | Path | Learning purpose | Scientific checks | Status |
|---|---|---|---|---|
| Reading map | `book/frontmatter/figures/reading-map` | course paths and prerequisites | matches part/chapter list | inspected |
| Visual legend | `book/frontmatter/figures/visual-legend` | book's visual grammar | arrow and bond semantics | inspected |
| DNA helix primer | `book/chapters/ch01/figures/primer-helix` | what a strand and duplex are | right-handed; ~2 nm, 0.34 nm/bp, ~10.5 bp/turn; groove positions computed from 148° strand offset | inspected |
| Three levels | `ch01/figures/three-levels` | specification vs mechanism vs evidence | n/a | inspected |
| Workflow | `ch01/figures/workflow` | lab steps paired with predicates | 120-base band = 6 × 20 bases; primer orientation | inspected |
| Junction | `ch01/figures/junction` | splint-aligned ligation | nick 3′-OH/5′-P; antiparallel splint | inspected |
| Eras | `ch01/figures/eras` | history of the field | dates match cited works | inspected |
| Beads | `ch02/figures/beads` | attachment vs recognition | biotin on O6-primer strand; probe antiparallel | inspected |
| dAMP structure | `ch05/figures/01-nucleotide` | parts of a nucleotide | adenine Kekulé bonds; N9–C1′; 2′-H2; 3′-OH; 5′-phosphate dianion | inspected |
| Base pairs | `ch05/figures/04-pairing-stacking` | Watson–Crick pairing and stacking | A·T 2 H-bonds (N6–H···O4, N1···H–N3); G·C 3 (O6···H–N4, N1–H···N3, N2–H···O2); sugars on minor-groove edge | inspected |
| Enzymes | `ch08/figures/00-enzymes` | cut, join, copy | EcoRI G^AATTC on both strands, 5′-AATT overhangs; ligase ATP→AMP; 5′→3′ synthesis | inspected |
| PCR cycle | `ch09/figures/00-pcr-cycle` | one cycle and growth | primer orientation; curves labelled illustrative | inspected |
| Apparatus | `ch10/figures/00-apparatus` | gel and fluorescence readout | DNA migrates to +; F/Q geometry | inspected |
| Landscape | `ch19/figures/00-landscape` | toehold length and rate | qualitative; ~10⁶-fold range per Zhang & Winfree 2009 | inspected |
| Neural | `ch21/figures/06-neural` | seesaw gate, neuron, winner-take-all | domain order S_i T S_j; dot products 4 and 2 | inspected |
| Origami | `ch22/figures/00-origami` | scaffold, staples, crossovers, pixels | staples antiparallel to scaffold; crossover topology | inspected |
| Storage pipeline | `ch25/figures/00-pipeline` | write–store–read channel | per-stage error types | inspected |
| Central dogma | `book/backmatter/figures/central-dogma` | transcription and translation | template read 3′→5′, RNA 5′→3′; ribosome 5′→3′ | inspected |
| Lab toolkit | `backmatter/figures/lab-toolkit` | operations at a glance | n/a | inspected |
| Timeline | `backmatter/figures/timeline` | 1953–2026 milestones | each milestone cited in Appendix C | inspected |
| Frontiers | `backmatter/figures/frontiers` | demonstrated vs open | each demonstration cited in Epilogue | inspected |

## Removed (replaced by plates or real tables)

`ch01/figures/DNAD-01-F1, F4, F6, F7, F10` and `ch02/figures/DNAD-02-F8, F10, F14`.
F7, F10 (Ch 2) and F14 were tables drawn as figures; they are now LaTeX tables.

## Restyled retained plates (branch `restyle-retained-plates`)

Redrawn in the shared visual language with content, labels and captions kept;
TXT companions rewritten to match. Each was rendered standalone at 90–100 dpi,
checked for overlaps and geometry, and viewed in the built PDF; print scale
0.97–1.15.

| Plate | Change | Checks |
|---|---|---|
| `ch11/01-polarity` | base tiles, harpoon strands, stored-string panel | rc(AACG) = CGTT |
| `ch11/02-offset` | fixed comparison vs shifted duplex | rc(ACGTAC) = GTACGT vs TACGTA: 6 mismatches; shift gives 5 pairs |
| `ch11/03-hairpin` | inverted repeat and folded stem | GCG/CGC stem, AAA loop |
| `ch11/04-graph` | graph plus base-level junction at B | R_A L_B = TCAG CCTA; R_B L_C = GTCA GATC; splint GGAT CAGT |
| `ch11/05-seam` | domains and seam window | window [2:6] = CGTC spans the AACG/TCAG boundary |
| `ch12/03-logic` | table-as-figure → candidate chips with pass/fail badges | edges per Ch 12 edge set |
| `ch12/05-order` | boxes → capacity slots with molecules | F-then-G empty; G-then-F good |
| `ch13/05-certificate` | decoded strand, clause checks, evidence branches | 101 satisfies all three clauses |
| `ch14/03-and` | text arrows → register strands with stickers | only a=1, b=1 gains c |
| `ch14/04-reset` | merging registers; history bit | 3 + 5 = 8 copies conserved |
| `ch15/01-splice` | provenance-coloured segments; LA\|BR, MC\|DN example | products LADN, MCBR |
| `ch17/04-cleavage` | three-stage restriction–ligation cycle with enzyme | staggered offset cut; offsets unspecified |
| `ch23/01-stack` | flowchart → illustrated design/assembly/signal/label cards | arrow semantics per legend |
| `ch23/03-repetition` | copies as tiles; common-mode panel | 10p^3 leading term for r = 5 |
| `ch24/01-resource` | flowchart → illustrated resource path | n bits → 2^n identities → depth d → Q bits |
| `ch24/06-tradeoff` | text boxes → schematic resource profiles | profiles labelled schematic, not data |
| `ch25/04-redundancy` | text boxes → bit cells on addressed shards | 1010 ⊕ 0110 = 1100; syndrome 0001 |
| `ch25/06-boundary` | storage vs computation comparison with icons | n/a |

Not restyled (already clear plots, automata or recent designs): the remaining
plates of Chapters 11–18 and 23–27, including all data plots, automaton and
tree diagrams, and Chapter 26's plates.

## Retained plates

About 170 earlier plates are retained unchanged in content. They inherit the
harmonised palette from `visual.tex` and the new scaling rule. They have been
seen only at contact-sheet scale in this pass; a full-resolution review against
the new visual language is listed in `PUBLICATION_READINESS.md`.

An attempted DNA-recorder plate for Chapter 30 and a redrawn Chapter 32 map
were not completed; the original Chapter 32 map is kept with a revised note.
