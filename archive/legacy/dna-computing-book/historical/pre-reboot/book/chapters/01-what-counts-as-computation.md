# Chapter 1 - What Counts as Computation?

After this chapter, you will be able to describe a physical or digital process as a computation without relying on metaphor. You will be able to identify its state, operators, schedule, readout, and cost model, and to explain why “many things happened at once” is not yet a complexity result.

## 1.1 The question beneath the machinery

A laptop adds numbers by moving charge through transistors. A cell copies DNA through a coordinated collection of enzymes, molecular recognition events, and chemical reactions. A test tube can contain an enormous population of DNA strands that bind, separate, are copied, or are filtered. These systems are physically different. Calling all of them *computers* is useful only if the word identifies a common structure rather than a visual resemblance.

The common structure is an interpretable state transition. At some moment a system occupies a state. A permitted operation changes that state. Repeated operations form a run. A readout maps the final or observed state to an answer.

One compact abstraction is a transition system

\[
\mathcal{C}=(X,\;\rightarrow,\;I,\;O),
\]

where:

- \(X\) is the state space;
- \(\rightarrow\subseteq X\times X\) is the transition relation;
- \(I\) maps problem instances to initial states;
- \(O\) maps observable states to outputs.

A run is a sequence

\[
x_0\rightarrow x_1\rightarrow \cdots \rightarrow x_T,
\qquad x_0=I(u),
\]

and its answer is \(O(x_T)\) when a declared halting or observation condition is met.

This definition is intentionally broad. It includes deterministic programs, nondeterministic rewrite systems, stochastic chemical processes, cellular automata, neural networks, and laboratory protocols. Breadth is not looseness: each instance must still say exactly what the state and transitions are.

## 1.2 Five questions that turn analogy into a model

When someone says that a biological process “computes,” ask five questions.

### What is the state?

State is the information required to predict or define what may happen next under the model. In a string-rewrite system it may be a word over an alphabet. In a chemical-reaction network it may be a vector of molecular counts or concentrations. In a wet-lab DNA algorithm it may include a population of strands, tube membership, reagent conditions, and the experimenter's current protocol step.

Leaving the experimenter out of the state can hide the real controller. If a human repeatedly moves material between tubes according to intermediate measurements, then the human and protocol participate in the computation. The molecules alone are not executing the whole algorithm.

### What are the operators?

An operator is not merely the name of a laboratory technique. It needs an input condition and a state change. “PCR” may denote a physical protocol with denaturation, primer annealing, and extension. In an idealized algorithm it may be modeled as an amplification operator on all strands matching primer constraints. Those two operators have different error, time, and resource behavior.

### What determines applicability?

Some transitions are selected by a program counter. Others are enabled when complementary domains meet, when a restriction site is present, or when concentrations cross a threshold. Applicability may be deterministic, nondeterministic, or stochastic.

### How is an answer read?

Molecular states do not arrive with a Python `return` statement. A result may require electrophoresis, fluorescence, affinity separation, sequencing, or another assay. Readout has cost and error. A model that counts molecular generation but ignores a difficult readout may move the hard part outside its accounting boundary.

### Which resources are counted?

Time and digital memory are not enough. A DNA computation may consume strand diversity, total molecules, reaction volume, temperature cycles, enzymes, manual operations, measurement steps, and error-correction overhead. Any asymptotic claim must name both the input-size convention and the resource being measured.

## 1.3 A first sequence computation

Let the canonical DNA alphabet be

\[
\Sigma_{\mathrm{DNA}}=\{A,C,G,T\}.
\]

Define the complement map

\[
c(A)=T,\quad c(T)=A,\quad c(C)=G,\quad c(G)=C.
\]

For a strand written 5-prime to 3-prime,

\[
s=s_1s_2\cdots s_n,
\]

its reverse complement is

\[
RC(s)=c(s_n)c(s_{n-1})\cdots c(s_1).
\]

This is already a complete digital computation. The state is a finite string. The operator reverses and substitutes symbols. The process is deterministic. The output is another string. Under an ordinary random-access representation it takes \(O(n)\) time and \(O(n)\) output space.

The same notation is also connected to a biological fact: paired DNA strands are antiparallel and canonical Watson-Crick pairing relates A with T and C with G. But the digital function `reverse_complement` does not simulate helix formation, salt concentration, secondary structure, mismatches, or temperature. It computes a sequence transform.

MiniDNA makes that boundary executable:

```python
from minidna import Strand

s = Strand("AACG")
assert s.reverse_complement().sequence == "CGTT"
```

The test establishes a software invariant. It does not establish a molecular binding result.

## 1.4 From transforms to molecular computation

The modern DNA-computing field is often dated to Leonard Adleman's 1994 experiment, which used DNA molecules and laboratory operations to solve a small directed Hamiltonian-path instance. The important conceptual move was not that DNA resembled a graph. Candidate paths were represented by molecular strands; molecular operations generated and filtered a population; the surviving material encoded an answer. The primary report is [Adleman, 1994](https://doi.org/10.1126/science.7973651).

At a high level, the computation had a generate-filter-read shape. [D04 — Adleman generate–filter–read pipeline](../diagrams/d04-adleman-generate-filter-read.txt) separates the graph encoding, molecular candidate population, filter cascade, depletion paths, assay, and resource ledger.

The graph is not a laboratory recipe. It identifies algorithmic roles and the physical costs hidden by a purely logical account. Each material-flow edge expands into steps with finite yield and possible error. The experiment demonstrated that molecular biology operations could realize a computation. It did not demonstrate that DNA is an efficient general replacement for electronic computers.

## 1.5 Deterministic, nondeterministic, and stochastic transitions

These words answer different questions.

A deterministic model gives at most one next state for each current state. A nondeterministic model permits several next states without assigning probabilities. It is often used to specify all possible molecular assemblies or rewrites. A stochastic model assigns rates or probabilities to events and therefore predicts distributions over runs.

Physical chemistry is stochastic at molecular scales, but a formal DNA-computing model need not be. Conversely, adding `torch.rand` to software does not make it a molecular model. The transition semantics determine the category.

For a chemical reaction

\[
A+B\xrightarrow{k}C,
\]

a count-based stochastic model might take the state to be \((n_A,n_B,n_C)\) and assign a propensity derived from \(k\), volume, and counts. A deterministic concentration model might instead use differential equations. A symbolic rewrite model may record only that `A + B -> C` is permitted. These models share a reaction diagram but answer different questions.

## 1.6 Parallelism is not free computation

DNA algorithms can act on very many molecules in one laboratory step. This is real physical parallelism. Its computational meaning depends on how many distinct molecules were synthesized, how much material and volume were required, how errors scale, and how the desired answer is isolated.

Suppose an algorithm materializes one molecular candidate for every member of an exponentially large search space. The number of sequential laboratory rounds may be small while molecular material grows exponentially. Reporting only rounds would make the computation appear cheap by omitting its dominant resource.

There is no single correct cost metric. There is a correct discipline: report the metrics that could change the conclusion.

## 1.7 Computation, simulation, and implementation

Three relationships are easy to conflate. [D15 — Model, simulation, and physical implementation](../diagrams/d15-model-simulation-implementation.txt) shows two realization mappings, the observation model, and the separate conformance and empirical-adequacy obligations.

A simulator is valuable because it makes assumptions inspectable and produces reproducible traces. It may simulate the abstract rules exactly while poorly predicting wet-lab kinetics. A physical implementation may approximate the abstract rules with leakage reactions and measurement noise. Agreement between the simulator and the abstraction is not automatically agreement between either one and chemistry.

This book will repeatedly build the simplest correct digital model first, then state what would be needed to connect it to a richer physical model.

## 1.8 A reusable analysis template

For every DNA-computing model in later chapters, we will record:

1. objects and representation;
2. complete state;
3. permitted operators;
4. transition and scheduling semantics;
5. input encoding and output readout;
6. sources of parallelism and stochasticity;
7. computational power under named assumptions;
8. time, space, material, energy, and error costs;
9. digital simulation contract;
10. physical failure modes;
11. present-day relevance;
12. any genomic-AI analogy, labeled as analogy or hypothesis.

The template prevents a common rhetorical shortcut: moving from “biology performs a transformation” to “a biologically named AI component inherits the transformation's capabilities.” It does not.

## What this chapter established

- Computation can be described through state, transitions, initialization, and readout.
- A serious model also declares applicability, schedule, and resource accounting.
- Reverse complement is both a biologically motivated relation and a precise digital string transform; the two levels remain distinct.
- Molecular parallelism is meaningful only beside material and error costs.
- Simulation of an abstract rule and physical implementation of that rule are separate evidence claims.

## What remains unverified

- No comprehensive physical cost model for DNA computation has been selected.
- MiniDNA's current hybridization score has not been connected to thermodynamic measurements.
- The later genomic-AI branches have not earned performance or biological-faithfulness claims.
- Historical priority and mechanism details beyond the cited primary sources still require chapter-specific review.
