# Book plan

## Working title

**DNA Computing: Foundations, Models, and the Road to Genomic Computation**

The title foregrounds established DNA computing. The final parts form a bridge to two AI research programs without implying that digital models execute molecular biology.

## Reader contract

Every mechanism follows the same explanatory ladder:

```text
biological phenomenon
        |
        v
computational intuition
        |
        v
formal abstraction
        |
        v
mathematical model
        |
        v
algorithm
        |
        v
Python / PyTorch experiment
        |
        v
limitations and evidence boundary
        |
        v
possible genomic-AI interpretation
```

## Proposed macro table of contents

### Part I - Information, computation, and evidence

1. What counts as computation?
2. Four evidence layers: molecule, simulation, differentiable model, architecture
3. Experimental claims and reproducible records

### Part II - DNA from first principles

4. Nucleotides, polarity, and strands
5. Complementarity and the reverse complement
6. Replication, transcription, translation, and regulation
7. Mutation, recombination, repair, and selection

### Part III - Molecular operations as algorithms

8. Hybridization, annealing, and melting
9. Cutting, ligation, PCR, separation, and sequencing
10. State, operators, stochasticity, and error

### Part IV - Classical DNA computing

11. Adleman's Hamiltonian-path experiment
12. Lipton-style parallel search and its resource accounting
13. Sticker, splicing, and insertion-deletion systems
14. Restriction-enzyme automata and Watson-Crick automata

### Part V - Molecular programming

15. Strand-displacement systems
16. Chemical reaction networks
17. DNA circuits and finite-state machines
18. Tile assembly and algorithmic self-assembly

### Part VI - Formal models and complexity

19. Languages, automata, rewrite systems, and graphs
20. Parallelism versus material volume
21. Time, space, energy, yield, error, and laboratory work
22. Universality claims and their assumptions

### Part VII - Regulation and expression

23. Gene regulation as conditional dynamics
24. Regulatory networks, feedback, and persistent state
25. When the program and the machine cannot be separated cleanly

### Part VIII - Exact digital simulation with MiniDNA

26. Sequence algebra and invariants
27. A transparent hybridization model
28. Cutting, ligation, and rewrite systems
29. Reaction and regulatory toy systems

### Part IX - Differentiable models in PyTorch

30. One-hot sequence tensors
31. Exact complement as a permutation matrix
32. Soft matching and differentiable hybridization
33. Trainable regulation without biological overclaiming

### Part X - From DNA computing to sequence learning

34. Tokenization, objectives, splits, and leakage
35. Reverse-complement symmetry and strand-aware representations
36. What transfers from molecular computing - and what does not

### Part XI - Transformer DNA research line

37. A standard causal Transformer baseline
38. DNA-specific inductive biases as testable hypotheses
39. Attention, retrieval, KV state, and long context

### Part XII - Non-Transformer DNA research line

40. GRU and state-space baselines
41. Regulation, expression, and structured state
42. Recurrent inference and its limits

### Part XIII - Controlled comparisons

43. Causality by intervention
44. Parameter-, width-, state-, and compute-matched comparisons
45. Negative results, correction records, and replication

### Part XIV - Toward genomic computation

46. Shared foundations, distinct machines
47. Evolutor and Genomic Computation Systems
48. Open problems and falsifiable research programs

## Dependency graph

```text
evidence discipline
      |
      +--> DNA structure --> sequence algebra --> complementarity
      |                                            |
      |                                            v
      |                                      hybridization
      |                                            |
      +--> molecular operations ------------------+
      |                |
      |                +--> search / separation / amplification
      |                +--> rewrite systems / automata
      |                +--> strand displacement / CRNs
      |                                   |
      |                                   v
      +---------------------------- formal complexity
                                           |
DNA regulation --> state / feedback -------+
      |                                    |
      v                                    v
regulated expression                  MiniDNA simulation
      |                                    |
      +----------------------+-------------+
                             v
                    differentiable bridge
                             |
                    shared evaluation rules
                             |
                 +-----------+-----------+
                 |                       |
                 v                       v
         Transformer DNA line    Non-Transformer DNA line
                 |                       |
                 +-----------+-----------+
                             v
                    genomic computation
```

## Diagram inventory

Text diagrams are canonical during bootstrap. Planned diagrams include strand polarity and antiparallel pairing; the molecular-operation pipeline; Adleman filtering; splicing semantics; strand-displacement state transitions; CRN species/reaction flow; tile growth; regulation and feedback; the four evidence layers; symbolic-to-tensor complement; training versus inference for each model family; long-context capability map; architecture lineage; and the common comparison harness.

## Chapter completion gate

A chapter is not complete until its terms are in the terminology file, nontrivial claims are classified, equations use the notation standard, code is tested where applicable, references point to primary sources, and the closing sections state both what was established and what remains unverified.

