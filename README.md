# DNA Computing: Foundations, Models, and the Road to Genomic Computation

This repository is the source for an evidence-disciplined book about molecular DNA computing, its formal models, and the careful bridge from those ideas to digital sequence models.

The book keeps four layers distinct:

1. molecular execution in a laboratory;
2. exact digital simulation of a molecular or formal model;
3. differentiable approximation in PyTorch;
4. a DNA-inspired AI architecture.

Biological vocabulary is never evidence that a software mechanism is biologically faithful. Claims are classified in [the claims ledger](research/claims-ledger.md), and unresolved facts stay visibly unresolved.

## Research branches

The shared foundations feed two independent research lines:

```text
                         DNA / GENOMIC COMPUTATION
                                  |
                  +---------------+---------------+
                  |                               |
                  v                               v
          Transformer DNA line          Non-Transformer DNA line
          proposed name: DOGMA?         proposed name: Hermon DNA?
          attention / KV state          recurrence / state / GCS
```

Those proposed names do not rewrite history. The current local `dogma` engine is recurrent, while the current `hermon` engine is transformer-oriented. See [architecture lineage](research/architecture-lineage.md).

## Start here

- [Book plan](BOOK_PLAN.md)
- [Chapter 1 - What Counts as Computation?](book/chapters/01-what-counts-as-computation.md)
- [Chapter 2 - Four Evidence Layers](book/chapters/02-four-evidence-layers.md)
- [Roadmap](ROADMAP.md)
- [Source map](research/source-map.md)
- [Notation](book/NOTATION.md)
- [MiniDNA](code/minidna/README.md)

## Development

```bash
python3 -m pytest
```

PyTorch is the semantic reference layer. Optimized kernels and custom runtimes are intentionally out of scope until the algorithms and their tests are stable.

## Manuscript status

Chapters 1 and 2 have complete first drafts. Chapter 3 will turn the evidence policy into concrete experiment manifests and reproducibility records before the book enters the DNA biology sequence.

## Source policy

The source PDFs and unpublished Evolutor papers are referenced from their local locations during research; they are not copied into this repository. This repository currently has no open-source license.
