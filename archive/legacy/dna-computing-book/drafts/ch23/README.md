# DNAD-23 — Noise, crosstalk and molecular fault models

Locally integrated r01 candidate, expanded to the canonical scope. The reference
derives correlated finite-size yield, IID and correlated repetition, calibrated
observation channels, Wilson intervals and a conditional amplification-bias model.
All numerical tables and the yield plot are generated from reference.py.

Run Python 3.13: `python drafts/ch23/build.py --render`; verify reproducible assets
with `--check`. Tests include independent uniform-beta, closed-form binomial and
Monte Carlo oracles, domain rejection and extreme numerical cases. Six original
editable TikZ figures have matching semantic TXT specifications; seventeen worked
questions connect the calculation to experimental design.

Primary-source checks and scope corrections are recorded under
research/integration/ch23. Computations are model outputs, not measurements.
Local technical/visual review does not promote the candidate to independent
scientific acceptance. Chapter 24 addresses scaling; Chapter 26 owns laboratory
workflow rather than repeating it here.
