# Claims ledger

Allowed classes: `ESTABLISHED BIOLOGY`, `ESTABLISHED COMPUTER SCIENCE`, `ESTABLISHED DNA-COMPUTING RESULT`, `SOURCE-DERIVED CLAIM`, `OUR INTERPRETATION`, `ENGINEERING ANALOGY`, `HYPOTHESIS`, `CONJECTURE`, `OPEN QUESTION`.

| ID | Claim | Class | Evidence / next action | Book status |
| --- | --- | --- | --- | --- |
| C001 | Canonical DNA uses the alphabet A, C, G, T and complementary pairing A-T, C-G. | ESTABLISHED BIOLOGY | standard molecular biology; add primary/authoritative biology reference | usable with citation |
| C002 | For a 5-prime-to-3-prime string, reverse complement reverses order after base complementation. | ESTABLISHED COMPUTER SCIENCE | formal definition and MiniDNA parity tests | implemented |
| C003 | Adleman's 1994 experiment used molecular biology operations to solve a directed Hamiltonian-path instance. | ESTABLISHED DNA-COMPUTING RESULT | DOI 10.1126/science.7973651 | verified bibliographically |
| C004 | DNA implementations can approximate specified coupled chemical-reaction kinetics using strand displacement under construction-specific assumptions. | ESTABLISHED DNA-COMPUTING RESULT | DOI 10.1073/pnas.0909380107 | use scoped wording |
| C005 | Algorithmic DNA tile self-assembly is Turing universal in an abstract model. | ESTABLISHED DNA-COMPUTING RESULT | Winfree thesis DOI 10.7907/HBBV-PF79 | distinguish theory and wet-lab demonstration |
| C006 | Molecular parallelism does not imply polynomial total physical resources. | ESTABLISHED COMPUTER SCIENCE | derive per algorithm with material-volume accounting | chapter 20 |
| C007 | PyTorch tensors are useful for digital simulations of sequence rules. | ENGINEERING ANALOGY | MiniDNA implementation | demonstrated narrowly |
| C008 | A complement permutation matrix exactly matches symbolic complementation for one-hot bases. | ESTABLISHED COMPUTER SCIENCE | `test_tensor_complement_matches_symbolic` | implemented |
| C009 | A soft hybridization score is a differentiable approximation, not molecular thermodynamics. | OUR INTERPRETATION | document assumptions and compare only to declared toy model | explicit boundary |
| C010 | Reverse-complement equivariance may improve sample efficiency on appropriate genomic tasks. | HYPOTHESIS | preregister task, baseline, transform, metrics, seeds | untested |
| C011 | Regulation-inspired conditional routing may improve compute-quality tradeoffs. | HYPOTHESIS | compare to generic routing controls | untested |
| C012 | The historical/current DOGMA engine is recurrent and non-transformer. | SOURCE-DERIVED CLAIM | local `dogma/docs/ARCHITECTURE.md` | current naming fact |
| C013 | The historical/current Hermon runtime contains transformer-oriented paged-KV machinery. | SOURCE-DERIVED CLAIM | `hermon` commit `472a44cdb511...` | current naming fact |
| C014 | DOGMA should become the target name for the transformer DNA line. | OUR INTERPRETATION | user-provided target taxonomy; naming decision still reversible | proposed, not historical |
| C015 | Hermon DNA should become the target name for the non-transformer DNA line. | OUR INTERPRETATION | user-provided target taxonomy; collision with current Hermon must be managed | proposed, not historical |
| C016 | One DNA-LLM family is generally superior for long context. | OPEN QUESTION | decompose retrieval, streaming, counting, motif, and regulation tasks | do not claim |
| C017 | A biological name makes a neural operator biologically faithful. | CONJECTURE | rejected as an invalid inference without experimental validation | prohibited claim |
| C018 | Enzyme-free nucleic-acid logic circuits have been constructed experimentally using strand-displacement principles. | ESTABLISHED DNA-COMPUTING RESULT | DOI 10.1126/science.1132493; preserve the paper's actual scale and conditions | verified bibliographically |

New claims must be added before publication. Quantitative entries must include source revision, dataset/split, checkpoint, evaluation code, budget, seeds, and uncertainty.
