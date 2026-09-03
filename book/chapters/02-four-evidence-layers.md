# Chapter 2 - Four Evidence Layers

After this chapter, you will be able to tell what kind of evidence a DNA-computing statement requires, prevent a software analogy from becoming a biological claim, and design a path by which a hypothesis can earn stronger language.

## 2.1 Why this separation is necessary

DNA is simultaneously biological material, an information-bearing polymer, a substrate for engineered molecular systems, and a source of ideas for software. The proximity of these subjects makes them easy to blend. A description may begin with Watson-Crick pairing, pass through a tensor operation, and end by claiming a new form of intelligence without marking where established science ended.

This book uses four evidence layers to stop that drift:

```text
MOLECULAR EXECUTION
physical strands, reactions, concentrations, temperature, assays
        |
        | abstraction and measurement model
        v
DIGITAL SIMULATION
software state that executes declared molecular or formal transitions
        |
        | optional relaxation / parameterization
        v
DIFFERENTIABLE MODEL
tensor computation trained by gradients
        |
        | architecture hypothesis and evaluation
        v
DNA-INSPIRED AI ARCHITECTURE
model for prediction, generation, retrieval, or control
```

The arrows are research programs, not implications. Success at one layer does not prove success at the next.

## 2.2 Layer one: molecular execution

A molecular-execution claim concerns matter. Relevant variables may include strand sequences and modifications, concentrations, buffers, temperature schedules, enzyme lots, incubation time, leakage reactions, yield, and assay sensitivity. Evidence normally requires an experimental protocol and measurements, not merely code.

For example, strand displacement uses an invading strand to bind an exposed toehold and displace a previously bound strand through branch migration. An abstract domain diagram can specify the intended reaction. Demonstrating that a designed system behaves as intended requires kinetic and experimental evidence. Seelig and colleagues' enzyme-free nucleic-acid logic circuits are one primary example of experimentally constructed strand-displacement logic ([DOI 10.1126/science.1132493](https://doi.org/10.1126/science.1132493)).

## 2.3 Layer two: digital simulation

A digital simulation represents a declared system in software. Its first obligation is semantic fidelity to that declaration.

MiniDNA's aligned hybridization function is intentionally modest. It reverse-complements one equal-length strand, compares a fixed alignment, and reports a match fraction. Tests can prove that the implementation follows this definition. The function omits concentrations, kinetic pathways, dangling ends, loop formation, nearest-neighbor energies, and experimental noise. It should therefore be described as an *aligned complementarity toy score*, not as a binding predictor.

```python
result = aligned_hybridization("AACG", "CGTT")
assert result.matches == 4
assert result.fraction == 1.0
```

The code is exact relative to its small model. Its smallness is a feature because the omitted assumptions are visible.

## 2.4 Layer three: differentiable model

A differentiable model replaces or augments exact operations with tensor functions that can participate in gradient-based learning. For one-hot bases ordered A, C, G, T, exact complementation is a permutation:

\[
C_{\mathrm{DNA}}=
\begin{bmatrix}
0&0&0&1\\
0&0&1&0\\
0&1&0&0\\
1&0&0&0
\end{bmatrix},
\qquad
\mathbf{x}_{\mathrm{comp}}=C_{\mathrm{DNA}}\mathbf{x}.
\]

This matrix is exact for the selected symbolic representation. A learned compatibility matrix would be different: it might improve a prediction task, but its entries would not become binding energies merely because the matrix was initialized from complement rules.

Differentiability answers “can gradients flow through this computation?” It does not answer “does chemistry execute this computation?” or “does the model generalize?”

## 2.5 Layer four: DNA-inspired AI architecture

At the architecture layer, components are organized to solve machine-learning tasks. The model may use attention, recurrence, state-space transitions, graphs, conditional routing, or mixtures of these. DNA may motivate symmetry constraints, paired-strand representations, regulation-inspired conditioning, or structural variation.

Each proposal is a hypothesis. A reverse-complement-equivariant model might learn genomic tasks more efficiently. A regulation-inspired router might reduce executed compute. A recurrent state may fit streaming tasks. These claims require controlled comparisons on named tasks.

Biological vocabulary has no evidentiary force. A module called a *promoter* is a software gate until experiments establish a stronger relationship. A parameter called *temperature* is a scalar unless it is calibrated to a physical model.

## 2.6 Claim labels and permitted verbs

The repository's evidence legend distinguishes established biology, established computer science, established DNA-computing results, source-derived claims, interpretations, analogies, hypotheses, conjectures, and open questions.

The labels constrain prose:

- a paper *reports* an experiment;
- a specification *defines* a model;
- code *implements* a function;
- a test *checks* an invariant;
- a benchmark *measures* behavior under its protocol;
- an ablation may *support* a causal interpretation;
- a proof *establishes* a theorem under assumptions.

“Shows” is often too ambiguous. It can conceal whether the evidence was a unit test, a three-seed experiment, a visual analogy, or a mathematical proof.

## 2.7 How a claim earns promotion

Consider the hypothesis: “reverse-complement equivariance improves genomic sequence modeling.” A disciplined evidence path is:

```text
define the symmetry exactly
        |
implement the transform and parity tests
        |
build a plain baseline
        |
add one equivariant mechanism
        |
freeze data, splits, budgets, metrics, and seeds
        |
run intervention and leakage checks
        |
compare per-seed outcomes and uncertainty
        |
replicate on an independent dataset or implementation
```

Even a positive result would remain scoped to the tasks, data, budgets, and model sizes tested. It would not prove that biological double strands explain the improvement.

## 2.8 Failure modes this book will avoid

### Analogy laundering

A biological mechanism is described accurately; software is given the same name; the biological property is then attributed to the software without a connecting experiment.

### Simulation laundering

A program behaves correctly under an ideal rule set; the result is presented as evidence that a physical system will behave correctly.

### Benchmark laundering

A model improves one metric under one budget; the result is expanded into a general architectural advantage.

### Proof laundering

A theorem is correct for a restricted baseline; prose quietly treats it as a lower bound for a broader model such as all Transformers or all neural networks.

### Version laundering

A later project reuses a name, and measurements from the earlier architecture are presented as evidence for the renamed one. The DOGMA/Hermon lineage in this research program makes this a concrete risk.

## 2.9 The public research contract

Because this book is developed in public, readers should be able to locate the boundary behind a sentence. Claims live in a ledger. Open gaps use explicit markers. Code examples have tests. Architecture comparisons record hidden dimensions as well as parameter counts. Corrections remain visible.

Public work can still be wrong. The promise is not infallibility; it is traceability. A reader should be able to discover what changed, why it changed, and which conclusions no longer follow.

## What this chapter established

- Molecular execution, digital simulation, differentiable models, and DNA-inspired architectures require different evidence.
- Exactness relative to a toy model is compatible with severe physical simplification.
- Differentiability and biological faithfulness are independent properties.
- Claim labels and precise verbs make evidence boundaries inspectable.
- Architecture names do not transfer evidence across implementations.

## What remains unverified

- The book has not yet selected a thermodynamic hybridization model.
- No DNA-specific neural mechanism has yet beaten a controlled generic baseline in this repository.
- The proposed future DOGMA/Hermon DNA naming remains a migration proposal.
- Independent scientific and editorial review of these evidence rules is still required.

