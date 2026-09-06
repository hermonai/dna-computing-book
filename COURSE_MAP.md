# DNA Computing: undergraduate-first architecture

Status: Chapter 1 internally reviewed development draft; all later units remain planned. No learner study, independent expert certification or new research-model experiment is claimed. Generated from [pedagogy/curriculum.json](pedagogy/curriculum.json). See [Chapter 1 storyboard](research/undergraduate-ch01-storyboard.md) for the six produced figures.

## Teaching route and chapter opening maps

Each opening recalls named prior ideas, introduces only the current step, and identifies what it enables next. A dependency is a teaching requirement, not a claimed biological causal relation. Unlisted previous chapters remain available for optional practice; no later chapter may be required.

## DNAU-01 — What does it mean to compute?

**Required earlier units (planned unless marked active):** High-school arithmetic and logical reading.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** computation → input → output → rule → step.

**Tangible opening:** Can the same rule work with counters and a calculator?

**Why and how the mathematics enters:** Count tangible objects before writing 3 + 2 = 5; no variables or code syntax.

**Observable exit task:** Identify input and output; find an ambiguous instruction; explain why the material can change while the rule stays the same.

**Enables next:** DNAU-02, DNAU-03, DNAU-07.

## DNAU-02 — Symbols, information and representations

**Required earlier units (planned unless marked active):** DNAU-01: What does it mean to compute?.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** symbol → data → information → representation → encoding → set → sequence.

**Tangible opening:** How can a mark stand for something else?

**Why and how the mathematics enters:** Show membership by placing cards inside a ring before set braces; use numbered positions before sequence notation.

**Observable exit task:** Recognize a sequence versus a set; expose an ambiguous encoding; supply a decoding key.

**Enables next:** DNAU-03, DNAU-05, DNAU-07, DNAU-09, DNAU-11, DNAU-33, DNAU-34.

## DNAU-03 — Algorithms, decisions and remembered state

**Required earlier units (planned unless marked active):** DNAU-01: What does it mean to compute?; DNAU-02: Symbols, information and representations.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** algorithm → condition → logic → and → or → not → state → loop → function → relation.

**Tangible opening:** How can a recipe choose and remember?

**Why and how the mathematics enters:** Input/output pairs motivate a function; contrast with a relation permitting several outputs. Truth tables follow ordinary sentences.

**Observable exit task:** Complete a trace; test a boundary case; explain why an instruction must terminate.

**Enables next:** DNAU-04, DNAU-05, DNAU-06, DNAU-08, DNAU-12, DNAU-25, DNAU-30, DNAU-34.

## DNAU-04 — Your first small Python programs

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** source code → program → interpreter → variable → string → list → dictionary → test → error message.

**Tangible opening:** How do instructions on paper become a runnable program?

**Why and how the mathematics enters:** Assignment is explained separately from mathematical equality; indexing begins with numbered cards.

**Observable exit task:** Predict output before running; repair an index error; write a three-case test with supplied answers.

**Enables next:** DNAU-05, DNAU-06, DNAU-11, DNAU-33, DNAU-34.

## DNAU-05 — Cities, roads, graphs and paths

**Required earlier units (planned unless marked active):** DNAU-02: Symbols, information and representations; DNAU-03: Algorithms, decisions and remembered state; DNAU-04: Your first small Python programs.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** graph → vertex → edge → directed edge → undirected edge → walk → path → simple path → cycle.

**Tangible opening:** How does a city map become a graph?

**Why and how the mathematics enters:** Teach each visual term before G=(V,E); declare path means no repeated vertex, walk may repeat; count both edges and listed vertices.

**Observable exit task:** Reject a backwards road; identify repeated vertices; compare path and cycle without requiring a named hard problem.

**Enables next:** DNAU-06, DNAU-21, DNAU-25.

## DNAU-06 — Search, counting and growing work

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state; DNAU-04: Your first small Python programs; DNAU-05: Cities, roads, graphs and paths.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** search → candidate → verification → permutation → factorial → growth rate → Big-O → proposition → proof → counterexample.

**Tangible opening:** Why can a tiny choice list grow so quickly?

**Why and how the mathematics enters:** Multiplication of choices precedes factorial; 100, 10000, 1000000 comparisons precede O(n²). Explain upper bound, not exact runtime.

**Observable exit task:** Count a three-card case; find a checker bug; explain a small proof in words before notation.

**Enables next:** DNAU-21, DNAU-24, DNAU-25.

## DNAU-07 — Atoms, molecules and different kinds of bonds

**Required earlier units (planned unless marked active):** DNAU-01: What does it mean to compute?; DNAU-02: Symbols, information and representations.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** atom → molecule → chemical bond → covalent bond → hydrogen bond → charge.

**Tangible opening:** What holds a molecule together?

**Why and how the mathematics enters:** No formula needed: distinguish object counts, connections and charges before chemical symbols.

**Observable exit task:** Identify what each line style means; explain why base-pair marks must not look like backbone bonds.

**Enables next:** DNAU-08, DNAU-09, DNAU-10.

## DNAU-08 — Solutions, amounts, temperature and change

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state; DNAU-07: Atoms, molecules and different kinds of bonds.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** solution → concentration → mole → pH → temperature → energy → equilibrium → kinetics → reaction rate.

**Tangible opening:** Why does the same molecule behave differently in different solutions?

**Why and how the mathematics enters:** Unit-labeled ratios precede concentration; introduce powers of ten and logarithm intuition before pH; energy landscapes are qualitative, not parameter predictions.

**Observable exit task:** Distinguish rate from equilibrium; identify missing units; interpret a pH scale without an unsupported binding calculation.

**Enables next:** DNAU-12, DNAU-14, DNAU-15, DNAU-16, DNAU-28.

## DNAU-09 — Cells, chromosomes, genes and genomes

**Required earlier units (planned unless marked active):** DNAU-02: Symbols, information and representations; DNAU-07: Atoms, molecules and different kinds of bonds.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** cell → nucleus → chromosome → DNA → gene → genome.

**Tangible opening:** Where is DNA, and what is a genome?

**Why and how the mathematics enters:** No equation; teach nested containment and distinguish a typical nucleated cell from bacteria and exceptions.

**Observable exit task:** Distinguish gene, chromosome and genome; explain why not every cell has a nucleus.

**Enables next:** DNAU-10, DNAU-13, DNAU-32.

## DNAU-10 — From a nucleotide to a DNA strand

**Required earlier units (planned unless marked active):** DNAU-07: Atoms, molecules and different kinds of bonds; DNAU-09: Cells, chromosomes, genes and genomes.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** base → sugar → phosphate → nucleotide → nucleoside → strand → double helix → deoxyribose → phosphodiester bond.

**Tangible opening:** What do the letters A, C, G and T leave out?

**Why and how the mathematics enters:** Introduce chemical shorthand only after the object key; no atom-resolved geometry inferred from cartoons.

**Observable exit task:** Distinguish base from nucleotide; locate the backbone; identify what a flattened drawing omits.

**Enables next:** DNAU-11, DNAU-13.

## DNAU-11 — Direction, pairing and reverse complement

**Required earlier units (planned unless marked active):** DNAU-02: Symbols, information and representations; DNAU-04: Your first small Python programs; DNAU-10: From a nucleotide to a DNA strand.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** 5-prime and 3-prime → complementarity → antiparallel → duplex → reverse complement.

**Tangible opening:** Why is a complement not yet a reverse complement?

**Why and how the mathematics enters:** Show directions and paired letters before c(s) or RC(s); build round-trip reasoning from an asymmetric example.

**Observable exit task:** Compute AGTC and ATAT partners; reject a wrong orientation; explain why a string test does not predict binding.

**Enables next:** DNAU-13, DNAU-14, DNAU-16, DNAU-22, DNAU-26, DNAU-31, DNAU-33.

## DNAU-12 — Chance, encounters and repeated trials

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state; DNAU-08: Solutions, amounts, temperature and change.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** probability → event → independence → conditional probability → random sample.

**Tangible opening:** Why might a possible molecular encounter never be observed?

**Why and how the mathematics enters:** Explain sample space and fractions; 0.9 × 0.9 = 0.81 precedes 1-(1-p)^M; flag independence as an assumption.

**Observable exit task:** Compute 0.19; contrast sampling with and without replacement; identify when the model is unjustified.

**Enables next:** DNAU-15, DNAU-16, DNAU-23, DNAU-24, DNAU-28, DNAU-33, DNAU-34.

## DNAU-13 — From DNA to RNA and proteins

**Required earlier units (planned unless marked active):** DNAU-09: Cells, chromosomes, genes and genomes; DNAU-10: From a nucleotide to a DNA strand; DNAU-11: Direction, pairing and reverse complement.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** RNA → protein → transcription → translation → codon → sequence transfer → amino acid → ribosome → transfer RNA.

**Tangible opening:** What is copied, and what is translated?

**Why and how the mathematics enters:** Teach alphabet and three-letter grouping before codon notation; introduce amino acids, transfer RNA and the ribosome through a labeled translation sequence. Enzyme mechanisms follow in Chapter 14.

**Observable exit task:** Distinguish copying sequence from controlling a process; recognize that some RNAs are not translated.

**Enables next:** DNAU-14, DNAU-32.

## DNAU-14 — Enzymes and DNA replication in six frames

**Required earlier units (planned unless marked active):** DNAU-08: Solutions, amounts, temperature and change; DNAU-11: Direction, pairing and reverse complement; DNAU-13: From DNA to RNA and proteins.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** enzyme → helicase → primer → primase → polymerase → replication → leading strand → lagging strand.

**Tangible opening:** Why are the two new strands made differently?

**Why and how the mathematics enters:** Teach new-strand and template directions before counting copies; distinguish an enzyme from a consumed nucleotide.

**Observable exit task:** Locate the growing end; repair a reversed arrow; track parental versus newly synthesized strands.

**Enables next:** DNAU-15, DNAU-17, DNAU-18, DNAU-32.

## DNAU-15 — What a laboratory operation actually does

**Required earlier units (planned unless marked active):** DNAU-08: Solutions, amounts, temperature and change; DNAU-12: Chance, encounters and repeated trials; DNAU-14: Enzymes and DNA replication in six frames.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** pipette → test tube → centrifuge → control sample → measurement → calibration.

**Tangible opening:** What goes into an instrument, and what comes out?

**Why and how the mathematics enters:** Teach volume and instrument readings before uncertainty ranges; no hazardous or unsupervised recipe.

**Observable exit task:** Match instruments to purpose; spot a unit error; explain why an unlabeled tube invalidates interpretation.

**Enables next:** DNAU-16, DNAU-17, DNAU-18, DNAU-19, DNAU-20.

## DNAU-16 — Hybridization as molecular recognition

**Required earlier units (planned unless marked active):** DNAU-08: Solutions, amounts, temperature and change; DNAU-11: Direction, pairing and reverse complement; DNAU-12: Chance, encounters and repeated trials; DNAU-15: What a laboratory operation actually does.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** hybridization → melting → free energy → association → dissociation.

**Tangible opening:** Why is compatible pairing not guaranteed binding?

**Why and how the mathematics enters:** Energy difference and units before any equilibrium formula; empirical parameters must have provenance.

**Observable exit task:** Separate compatibility, occupancy and reaction speed; identify unsupported numerical predictions.

**Enables next:** DNAU-17, DNAU-18, DNAU-29, DNAU-31.

## DNAU-17 — Cutting and joining strands

**Required earlier units (planned unless marked active):** DNAU-14: Enzymes and DNA replication in six frames; DNAU-15: What a laboratory operation actually does; DNAU-16: Hybridization as molecular recognition.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** restriction enzyme → recognition site → ligation → ligase.

**Tangible opening:** How can cutting and joining act like instructions?

**Why and how the mathematics enters:** Track sequence positions before slice notation; orientation and chemical ends remain explicit.

**Observable exit task:** Predict fragments; reject incompatible orientation; distinguish association from covalent joining.

**Enables next:** DNAU-19, DNAU-22, DNAU-27.

## DNAU-18 — Copying selected DNA with PCR

**Required earlier units (planned unless marked active):** DNAU-14: Enzymes and DNA replication in six frames; DNAU-15: What a laboratory operation actually does; DNAU-16: Hybridization as molecular recognition.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** polymerase chain reaction → PCR → thermal cycler → amplification.

**Tangible opening:** How can a chosen DNA region become easier to detect?

**Why and how the mathematics enters:** Repeated doubling precedes 2^k; efficiency, plateau and unintended products are not hidden.

**Observable exit task:** Identify primer direction; calculate two cycles; explain why real yield need not double.

**Enables next:** DNAU-19, DNAU-20, DNAU-23.

## DNAU-19 — Separating molecules and retaining candidates

**Required earlier units (planned unless marked active):** DNAU-15: What a laboratory operation actually does; DNAU-17: Cutting and joining strands; DNAU-18: Copying selected DNA with PCR.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** gel → electrophoresis → affinity separation → size selection.

**Tangible opening:** How does a physical separation implement a selection rule?

**Why and how the mathematics enters:** Teach reference size and relative migration first; no universal length-to-distance law.

**Observable exit task:** Read a schematic gel; distinguish amount from length; explain what a blurry band cannot establish.

**Enables next:** DNAU-20, DNAU-23.

## DNAU-20 — Detecting and reading a result

**Required earlier units (planned unless marked active):** DNAU-15: What a laboratory operation actually does; DNAU-18: Copying selected DNA with PCR; DNAU-19: Separating molecules and retaining candidates.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** fluorescence → sequencer → DNA synthesizer → readout → detection threshold.

**Tangible opening:** How does a molecular event become a reported answer?

**Why and how the mathematics enters:** Background and threshold before binary detection; do not convert no signal into proof of no candidate.

**Observable exit task:** Explain synthesizer versus sequencer; reject an overconfident negative result; propose a control.

**Enables next:** DNAU-22, DNAU-23, DNAU-33.

## DNAU-21 — Hamiltonian paths: a visual mini-course

**Required earlier units (planned unless marked active):** DNAU-05: Cities, roads, graphs and paths; DNAU-06: Search, counting and growing work.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** Hamiltonian path → Hamiltonian cycle → specified endpoint → witness → predicate.

**Tangible opening:** Can a route visit every city exactly once?

**Why and how the mathematics enters:** Only after valid/invalid pictures, write P=(v1,...,vn) and its conditions; explain each quantifier in words.

**Observable exit task:** Recognition, route checking, implementation and reasoning ladder; fully work one valid and two invalid routes.

**Enables next:** DNAU-22, DNAU-25.

## DNAU-22 — Adleman's idea: encode a graph in DNA

**Required earlier units (planned unless marked active):** DNAU-11: Direction, pairing and reverse complement; DNAU-17: Cutting and joining strands; DNAU-20: Detecting and reading a result; DNAU-21: Hamiltonian paths: a visual mini-course.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** molecular encoding → vertex code → overlap code.

**Tangible opening:** How can a molecule represent a city and a road?

**Why and how the mathematics enters:** Define code length and overlap only after paired illustrations; distinguish teaching instance from the historical seven-vertex experiment.

**Observable exit task:** Spot encoding ambiguity; trace one joined candidate; explain that a correct code does not guarantee physical generation.

**Enables next:** DNAU-23.

## DNAU-23 — Generate, filter and read the candidates

**Required earlier units (planned unless marked active):** DNAU-12: Chance, encounters and repeated trials; DNAU-18: Copying selected DNA with PCR; DNAU-19: Separating molecules and retaining candidates; DNAU-20: Detecting and reading a result; DNAU-22: Adleman's idea: encode a graph in DNA.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** candidate population → endpoint filter → coverage filter → false positive → false negative.

**Tangible opening:** Why is one filter not enough?

**Why and how the mathematics enters:** Count retained candidates before set-filter notation; distinguish sample abundance from distinct strings.

**Observable exit task:** Keep a repeated-vertex counterexample until coverage; explain absent candidates versus missed detection.

**Enables next:** DNAU-24, DNAU-26.

## DNAU-24 — What the experiment proved, and what it did not

**Required earlier units (planned unless marked active):** DNAU-06: Search, counting and growing work; DNAU-12: Chance, encounters and repeated trials; DNAU-23: Generate, filter and read the candidates.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** soundness → completeness → resource model → parallelism.

**Tangible opening:** Why is a small successful experiment not a shortcut around hard search?

**Why and how the mathematics enters:** Plain reasoning precedes proposition and proof; explain the assumptions separately for checking survivors and generating every possible answer. Complexity-class terminology waits for the machine and reduction foundations in Chapter 25.

**Observable exit task:** Find a missing completeness premise; audit exponential material demand; state the bounded historical conclusion.

**Enables next:** DNAU-25, DNAU-35.

## DNAU-25 — Languages, machines and computational models

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state; DNAU-05: Cities, roads, graphs and paths; DNAU-06: Search, counting and growing work; DNAU-21: Hamiltonian paths: a visual mini-course; DNAU-24: What the experiment proved, and what it did not.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** alphabet → formal language → automaton → finite-state machine → transition → Turing machine → SAT → nondeterminism → decision problem → polynomial reduction → NP → NP-complete.

**Tangible opening:** What does it mean for different machines to solve the same kind of problem?

**Why and how the mathematics enters:** Teach Boolean variable, clause and satisfiability before SAT; accepted sets before formal-language notation. Explain decision tasks, polynomial-time checking and a concrete reduction before defining NP and NP-complete; distinguish nondeterminism from physical parallelism.

**Observable exit task:** Trace acceptance; explain nondeterminism versus randomness; mark theorem assumptions and idealized unlimited storage.

**Enables next:** DNAU-26, DNAU-27, DNAU-28, DNAU-31.

## DNAU-26 — Strand, sticker and paired-strand models

**Required earlier units (planned unless marked active):** DNAU-11: Direction, pairing and reverse complement; DNAU-23: Generate, filter and read the candidates; DNAU-25: Languages, machines and computational models.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** sticker model → Watson-Crick automaton → molecular instruction set.

**Tangible opening:** What changes when the allowed molecular instructions change?

**Why and how the mathematics enters:** Operation tables precede model tuples; keep variants and their computational powers separate.

**Observable exit task:** Recognize a model operation; trace a program; reject a theorem transferred between variants.

**Enables next:** DNAU-36.

## DNAU-27 — Splicing and rewriting strings

**Required earlier units (planned unless marked active):** DNAU-17: Cutting and joining strands; DNAU-25: Languages, machines and computational models.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** rewrite rule → splicing → insertion → deletion.

**Tangible opening:** Can cutting and joining describe a formal language?

**Why and how the mathematics enters:** Concrete substitutions precede formal rewriting notation; alphabet, context and rule conditions stay visible.

**Observable exit task:** Apply a rule; identify an illegal cut; distinguish formal closure from laboratory feasibility.

**Enables next:** DNAU-36.

## DNAU-28 — Reaction networks and changing amounts

**Required earlier units (planned unless marked active):** DNAU-08: Solutions, amounts, temperature and change; DNAU-12: Chance, encounters and repeated trials; DNAU-25: Languages, machines and computational models.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** chemical reaction network → recurrence → stochastic process → mass action.

**Tangible opening:** How can amounts change step by step?

**Why and how the mathematics enters:** Old amount minus loss plus input precedes recurrence; stoichiometric counts and units precede rate equations; introduce derivative as instantaneous rate only if needed.

**Observable exit task:** Compute two updates; check conservation; distinguish one random path from an average.

**Enables next:** DNAU-29, DNAU-30, DNAU-32, DNAU-35.

## DNAU-29 — Strand displacement in slow motion

**Required earlier units (planned unless marked active):** DNAU-16: Hybridization as molecular recognition; DNAU-28: Reaction networks and changing amounts.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** toehold → branch migration → strand displacement → leakage.

**Tangible opening:** How can one strand release another without an enzyme?

**Why and how the mathematics enters:** Teach domain labels before domain-level notation; rates require sourced parameters.

**Observable exit task:** Track conserved strands; correct an orientation mistake; identify omitted side reactions.

**Enables next:** DNAU-30.

## DNAU-30 — Digital and analog molecular circuits

**Required earlier units (planned unless marked active):** DNAU-03: Algorithms, decisions and remembered state; DNAU-28: Reaction networks and changing amounts; DNAU-29: Strand displacement in slow motion.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** logic gate → digital circuit → analog signal → threshold → feedback.

**Tangible opening:** How can small reactions be connected into a larger computation?

**Why and how the mathematics enters:** Truth table precedes Boolean expression; scaled concentration precedes analog formula; feedback sign is explained.

**Observable exit task:** Check all inputs; identify signal depletion; explain why correct isolated gates need not compose reliably.

**Enables next:** DNAU-31, DNAU-32, DNAU-35.

## DNAU-31 — Local assembly, tiles and DNA origami

**Required earlier units (planned unless marked active):** DNAU-11: Direction, pairing and reverse complement; DNAU-16: Hybridization as molecular recognition; DNAU-25: Languages, machines and computational models; DNAU-30: Digital and analog molecular circuits.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** tile assembly → local rule → DNA origami → addressability → geometry.

**Tangible opening:** How can local attachments create a larger pattern?

**Why and how the mathematics enters:** Coordinates follow grid pictures; no assumption that geometric assembly computes the same function as a circuit.

**Observable exit task:** Find a forbidden attachment; distinguish shape from algorithm; state the physical scale boundary.

**Enables next:** DNAU-36.

## DNAU-32 — Genes, regulation, development and evolution

**Required earlier units (planned unless marked active):** DNAU-09: Cells, chromosomes, genes and genomes; DNAU-13: From DNA to RNA and proteins; DNAU-14: Enzymes and DNA replication in six frames; DNAU-28: Reaction networks and changing amounts; DNAU-30: Digital and analog molecular circuits.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** regulation → promoter → expression → mutation → inheritance → selection → adaptation → development.

**Tangible opening:** How can the same DNA support different cellular behavior?

**Why and how the mathematics enters:** Separate within-cell state change from inherited population change; simple frequency counts precede population notation.

**Observable exit task:** Identify regulatory control versus sequence transfer; distinguish adaptation, mutation and development.

**Enables next:** DNAU-36.

## DNAU-33 — DNA storage, codes and recovery

**Required earlier units (planned unless marked active):** DNAU-02: Symbols, information and representations; DNAU-04: Your first small Python programs; DNAU-11: Direction, pairing and reverse complement; DNAU-12: Chance, encounters and repeated trials; DNAU-20: Detecting and reading a result.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** bit → error-correcting code → redundancy → random access → entropy.

**Tangible opening:** How can a message survive a damaged molecular copy?

**Why and how the mathematics enters:** Teach bit choices and code distance before coding bounds; probability and logarithm recall precede entropy, without claiming one universal capacity.

**Observable exit task:** Recover a toy message; measure overhead; distinguish storage from active molecular computation.

**Enables next:** DNAU-34, DNAU-35.

## DNAU-34 — Many numbers at once: vectors, matrices and DNA data

**Required earlier units (planned unless marked active):** DNAU-02: Symbols, information and representations; DNAU-03: Algorithms, decisions and remembered state; DNAU-04: Your first small Python programs; DNAU-12: Chance, encounters and repeated trials; DNAU-33: DNA storage, codes and recovery.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** vector → matrix → dot product → matrix multiplication → sequence model.

**Tangible opening:** Why do sequence-analysis programs use arrays of numbers?

**Why and how the mathematics enters:** Ordered measurements precede vector notation; row-column weighted sums precede matrix products and dimensions.

**Observable exit task:** Check dimensions; compute a two-row result; explain the two meanings of DNA computation.

**Enables next:** DNAU-35, DNAU-36.

## DNAU-35 — Resources, energy, reliability and design tools

**Required earlier units (planned unless marked active):** DNAU-24: What the experiment proved, and what it did not; DNAU-28: Reaction networks and changing amounts; DNAU-30: Digital and analog molecular circuits; DNAU-33: DNA storage, codes and recovery; DNAU-34: Many numbers at once: vectors, matrices and DNA data.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** resource budget → energy accounting → reliability → model validation → parameter provenance.

**Tangible opening:** What must be counted before calling a design efficient?

**Why and how the mathematics enters:** Attach units to every quantity before a cost tuple; no free-energy-to-computer-energy shortcut.

**Observable exit task:** Reconcile units; design a control; distinguish software tests from physical validation.

**Enables next:** DNAU-36.

## DNAU-36 — A measured frontier and the bridge to Evolutor

**Required earlier units (planned unless marked active):** DNAU-26: Strand, sticker and paired-strand models; DNAU-27: Splicing and rewriting strings; DNAU-31: Local assembly, tiles and DNA origami; DNAU-32: Genes, regulation, development and evolution; DNAU-34: Many numbers at once: vectors, matrices and DNA data; DNAU-35: Resources, energy, reliability and design tools.

**Book I bridge:** None. See the planned exit checks in the shared contract.

**First encounters, in planned teaching order:** research claim → baseline → falsifier → reproducibility → transfer task.

**Tangible opening:** What can you now build, explain and still not claim?

**Why and how the mathematics enters:** No new advanced formula; reconstruct earlier tools in a bounded capstone.

**Observable exit task:** Explain a mechanism, implement its checker, critique evidence and complete the Book II readiness tasks.

**Enables next:** Capstone completion and further research.
