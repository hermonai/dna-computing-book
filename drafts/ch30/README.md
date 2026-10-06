# Chapter 30 — Genomic organization, regulation and development

Source candidate: dna-computing-ch30-r01.zip. Incoming metadata is retained under
research/integration/ch30/incoming; the manuscript, reference, tests and plates
were substantially strengthened rather than copied.

Move from molecular carriers and one-site occupancy to a nondimensional
mutual-repression circuit. Derive every fixed point, the symmetry-breaking
threshold and local Jacobian stability, then separate numerical positivity,
convergence, intervention and biological evidence. Recorded ancestry, supplied
pseudotime, molecule partition and population selection have distinct models.

Six editable TikZ/PGF plates have semantic TXT companions. Five complete tested
function listings and twenty worked exercises connect derivation, implementation,
trace and falsification. No calibrated organism, lineage reconstruction or
genomic evolution is implemented.

Run from this repository with Python 3.13. The verified local interpreter is
/Users/wenyan/.pyenv/versions/3.13.6/bin/python3:

    python3.13 -m pytest tests/test_ch30_reference.py -q -o addopts=''
    python3.13 drafts/ch30/build.py --render
    python3.13 drafts/ch30/build.py --check

55 tests include independent dense RK4 refinement, fixed-point/Jacobian arithmetic,
exhaustive three-molecule partition probabilities and a closed-form selection
trajectory. Output: output/pdf/dna-computing-ch30-review.pdf. Compiler diagnostics
and source/PDF hashes live in build/ch30; author review is recorded separately
after inspection. Independent and cumulative acceptance remain open.
Do not run PDF-mutating builds alongside repository preservation tests.

Next: dna-computing-ch31-r01.zip connects molecular-program refinement with
observational evidence; dna-computing-ch32-r01.zip supplies synthesis. Both remain
explicitly tracked for sequential integration, not silently replaced.
