# Pedagogical redesign: DNA Computing

Date: 2026-09-06. New branch: astra-undergraduate-rewrite. Status: architecture ready for user review; manuscript production not started.

## Thesis: the first course, not a compressed survey

**DNA Computing: From Molecules to Algorithms** becomes the prerequisite course for Book II. It starts with what it means to compute: a rule, some counters, a change, and an answer. The first chapter should invite curiosity, not require the ability to parse a graph-theory definition.

The previous opening immediately asked readers to understand directed Hamiltonian paths, witness conditions, set notation, soundness and completeness. Its second chapter used chemical and directional vocabulary before a beginner had built the underlying objects. The scientific discipline is worth retaining as a review standard, but those chapters are not the new baseline.

The new route is everyday computation → symbols and procedures → beginner Python and city graphs → molecules and DNA → physical operations and instruments → the historical DNA-computing experiment → formal models and molecular programs → evidence, engineering and the Book II bridge. It interleaves mathematics with the problem that motivates it. DNA biology is not deferred behind an entire discrete-mathematics course.

## Concrete relocation decisions

Chapter 1 has counters and a calculator, not Hamiltonian paths or proof notation. Chapter 5 introduces cities → dots → roads → arrows → walks → paths → cycles, one term at a time. Chapter 6 counts tiny search spaces before growth notation. Chapter 21 revisits the graph pictures to teach visiting every vertex once, named Hamiltonian paths and cycles, and independent checking. DNA encoding follows only after direction, joining and readout have been taught.

The old polarity example moves into Chapter 11 after atoms, bonds, cells, nucleotides and strand structure. The old generate/filter example is a possible audit source for Chapters 23–24, not text to paste into an introduction. DNA replication receives six sequential frames, rather than a single overloaded overview. Lab operations each explain input, action and output before they are treated as computational instructions.

## Exit contract with Evolutor

The planned exit contract is not just “read DNA Computing.” It names the chapter, terms and observable tasks that Book II imports. Relevant routes include programs and Python (1–6), molecular biology (7–14), probability (12), information and formal models (24–28), biological regulation and evolution (32), and vectors/matrices plus evidence checking (34–36).

Book I teaches small matrix operations and numerical data representations, not an untaught neural-network course. Book II must teach models, training, gradients and architecture itself. Book I's final readiness tasks require the learner to explain orientation, trace an algorithm, reason about an independent-trial assumption, multiply a tiny matrix, run a tested Python example, and separate a biological mechanism from a computational analogy. These outcomes remain planned until the corresponding chapters and exercises are actually written and reviewed.

## Pedagogical contract

The learner arrives with high-school arithmetic and algebra, curiosity, and no assumed university biology, chemistry, probability, algorithms, machine learning or software-engineering course. Teach just enough immediately before it is needed. Do not replace advanced material with vague metaphors; build the staircase to it.

The normal teaching order is prerequisite → intuition → concrete example → illustration → precise definition → mathematics → procedure → implementation → application. A departure needs a recorded reason. A first encounter includes an ordinary example and a labeled picture before notation. Equations must be assembled from quantities the reader can explain, not dropped as definitions. Technical terms in captions, exercises, code comments and chapter-opening maps count as first encounters too.

A chapter opens with a tangible question and an already-known/current/next map. Small sections teach one step at a time. It ends with what the learner now knows, what remains simplified, and what that enables next. A proof begins with reasoning and a proof idea; formal proof is introduced gradually. Code follows a manually traced procedure, with syntax explained before it is required.

## Architecture deliverables and source of truth

- [Course contents](BOOK_PLAN.md): part structure and every planned chapter.
- [Course map](COURSE_MAP.md): per-chapter prerequisites, first encounters, mathematics bridge and exit task.
- [Prerequisite graph](PREREQUISITE_GRAPH.md): typed Unicode TXT teaching dependencies, no ASCII box art.
- [Disciplinary maps](CONCEPT_MAPS.md): just-in-time concept routes.
- [Visual storyboard](VISUAL_STORYBOARD.md): teaching questions, sequential frames and comparison figures for every chapter.
- [Learning progression](LEARNING_PROGRESSION.md): exercises, code and experiments.
- [First-encounter ledger](TERMINOLOGY_AUDIT.md): planned terms, not a falsely completed glossary.
- [Previous-edition audit](PREVIOUS_EDITION_AUDIT.md): disposition of every old drafted and planned chapter.
- [Beginner review](BEGINNER_REVIEW.md) and [professional review](PROFESSIONAL_REVIEW.md): internal role-based critiques, not external endorsements.
- [Figure system](FIGURE_SYSTEM.md): scientific and engineering visual rules.
- [Review gates](REVIEW_GATES.md): criteria for authorizing and then accepting chapter production.

The canonical editable plan is pedagogy/curriculum.json. scripts/build_pedagogy.py derives the maps and inventories. A change to a title, prerequisite, first-use term or storyboard is made there first. Generated documents are checked for freshness. These files are editorial plans, not reader-facing manuscript chapters.

## Course scope and pacing

A full book is not assumed to fit one semester. The proposed small chapters are teaching units with variable length; scheduling and contact-hour estimates remain unvalidated. Readers can study at different speeds, but a short course must not skip prerequisite nodes while claiming the same exit competence. Optional research projects are separate from the baseline exit checks. No external textbook is used as a substitute for missing teaching.

Exercises progress from recognition, calculation and tracing through application, implementation, reasoning and research. Early work uses only taught tools. Provide the first solved case, a partially worked case, and a fresh case with hints and answer checks. A research question receives an evaluation rubric and explicit acceptable uncertainty rather than an invented unique solution. Include delayed retrieval of earlier ideas, not only immediate imitation.

## Evidence and access

A picture that is easy to understand can still be wrong. Biological arrows require mechanism and orientation checks; software diagrams require agreement with the code. No internal role simulation substitutes for independent subject review or observed learner testing. Existing regression tests demonstrate code properties, not textbook readability, biology, experimental advantage or intelligence.

This architecture adopts concrete-to-abstract bridges, paired verbal/visual explanations, worked examples interleaved with practice, and spaced retrieval. These choices are consistent with the recommendations in the official [IES practice guide, Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1), reviewed on 2026-09-06. The guide does not validate this curriculum or its proposed chapter count. The exact prerequisite-first invariant is our editorial requirement, not a claimed universal empirical theorem.

Research registers from the old edition remain useful leads, not automatic scientific approval. Every new chapter needs renewed section-level source review and explicit observation/model/hypothesis boundaries. Current frontier chapters require fresh primary-paper and artifact review when drafted. No benchmark, experiment or contemporary taxonomy is asserted by this outline.

## First execution boundary

This milestone produces architecture only. It does not draft Chapter 1, continue old Chapter 3, generate publication figures or animations, rewrite PDFs, run new scientific experiments, change licensing or authorship, or declare the new curriculum taught. The next execution prompt authorizes the first undergraduate-first chapter only after the architecture is reviewed. Existing astra-rewrite and main histories are preserved; neither is force-pushed or replaced.
