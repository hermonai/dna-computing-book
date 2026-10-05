# Chapter 21: Digital and analog DNA circuits

Standalone authored-LaTeX review candidate; earlier sources and accepted
publications are preserved.

Derive concentration logic contracts, restoration and leakage windows, staged
composition, capture-versus-release races, fan-out loading, analog error
propagation and autocatalytic feedback.

Five original editable vector figures have semantic TXT companions. Twelve
worked exercises connect proofs, implementations and counterexamples.
Computed tables and plot coordinates come from reference.py. Primary-source
access boundaries are recorded in sources.tex; these are teaching references,
not laboratory measurements or trained genomic results.

## Reproduce

Run at the repository root in the project Python environment:

~~~sh
python3 drafts/ch21/build.py --assets-only
python3 -m pytest tests/test_ch21_reference.py
python3 drafts/ch21/build.py --render
python3 drafts/ch21/build.py --check
~~~

Dependencies: NumPy, pytest, Pillow, XeLaTeX/latexmk and Poppler.
Compiler output stays in build/ch21/.
Readable PDF: output/pdf/dna-computing-ch21-review.pdf.
Author review manifest: artifacts/deep/ch21-review.json.
PDFs and page renders are generated and ignored by Git.

Independent specialist review, reader feedback and cumulative integration
remain open. Author review does not certify industrial readiness.

