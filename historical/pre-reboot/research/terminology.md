# Terminology standard

## Biological terms

- **Base**: nucleobase identity (A, C, G, T); do not use interchangeably with nucleotide.
- **Nucleotide**: base plus sugar and phosphate.
- **Strand**: ordered polymer with directionality; sequences default to 5-prime-to-3-prime notation.
- **Complement**: basewise mapping without changing written order.
- **Reverse complement**: complement followed by reversal; the operation normally needed when both strands are written 5-prime-to-3-prime.
- **Hybridization**: physical association of complementary nucleic-acid strands. A software score is called a *hybridization toy score*, not hybridization itself.
- **Gene regulation**: biological control of gene expression. “Regulation” in software is qualified as *formal* or *architecture-inspired*.

## Computation terms

- **Molecular execution**: reactions physically performed by molecules.
- **Digital simulation**: software execution of a declared molecular/formal model.
- **Differentiable model**: tensor computation with gradients; it may approximate or borrow structure from another model.
- **DNA-inspired architecture**: a software design motivated by biology; no claim of molecular faithfulness follows.
- **State**: sufficient data needed to continue a declared computation.
- **Operator**: transformation with explicit input, output, and applicability conditions.
- **Parallelism**: simultaneous physical or logical operations; always state the resource and cost model.

## Research program names

- **Evolutor / GCS**: umbrella theory of persistent genome, regulation, expression, trace, and verified evolution. It is not automatically a neural architecture.
- **DOGMA (historical/current)**: recurrent non-transformer research architecture and engine in the inspected local corpus.
- **Hermon (historical/current)**: transformer-oriented inference/runtime system with paged KV in the inspected local corpus.
- **DOGMA (target, proposed)**: transformer DNA-LLM research line. Use “target DOGMA” until migration is approved.
- **Hermon DNA (target, proposed)**: non-transformer DNA-LLM research line. Use the full qualifier to avoid collision.

## Evidence verbs

- **defines / proposes** for a source theory;
- **implements** for executable code;
- **passes** for a named test;
- **measures** only with an artifact and protocol;
- **demonstrates** only within the measured scope;
- **proves** only with a reviewed formal proof and explicit assumptions.

