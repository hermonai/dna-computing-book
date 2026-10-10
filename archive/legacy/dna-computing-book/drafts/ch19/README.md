# Chapter 19: Toehold-mediated strand displacement

Standalone authored-LaTeX review candidate; earlier accepted editions remain unchanged.

Polarity-correct strand exchange, strand-inventory invariants, first-passage probabilities and times, finite-pool depletion, leakage windows, and composition contracts.

Five original editable TikZ figures have semantic TXT companions. Twelve exercises
include worked answers. Tables, plots and code listings come from reference.py;
sources.tex records primary-source access and separates published research from
the proposed teaching models.

## Reproduce

Run from the repository root with the project Python environment:

```sh
python3 drafts/ch19/build.py --assets-only
python3 -m pytest tests/test_ch19_reference.py
python3 drafts/ch19/build.py --render
python3 drafts/ch19/build.py --check
```

Dependencies: NumPy, pytest, Pillow, XeLaTeX/latexmk and Poppler.
The chapter does not require SciPy. Build intermediates stay in build/ch19/.
The readable PDF is output/pdf/dna-computing-ch19-review.pdf.
PDFs and page previews are generated and ignored by Git; authored sources,
numerical results, tests and the author-review manifest are versioned.

The review record is artifacts/deep/ch19-review.json. Technical and visual
author review is not independent scientific acceptance. Specialist review,
reader feedback and cumulative integration remain open. Next topic: chemical reaction networks.

