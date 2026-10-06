# DNAD-25: DNA storage and error-correcting design

This integration replaces the r01 sketch with an auditable unordered-pool decoder
and a separate exact constrained-code construction. It continues Chapter 24's
resource denominators; Chapter 26 owns laboratory provenance.

The archive retains length, addresses, layout, CRCs and a trusted SHA-256 manifest.
One located shard erasure per XOR group is recoverable. Conflicting valid reads,
inconsistent parity and insufficient evidence fail explicitly. The raw archive
is intentionally NOT GC/run constrained; the counterexample motivates the second
implementation. Exact suffix counts and lexical rank/unrank enforce the declared
GC/run bounds, not all biochemical constraints.

Run with Python 3.13 and pytest:
- python3 -m pytest -q -o addopts='' tests/test_ch25_reference.py
- python3 drafts/ch25/build.py --assets-only
- python3 drafts/ch25/build.py --check
- python3 drafts/ch25/build.py --render

33 independent/domain/failure tests, seven complete function listings, six original
editable TikZ plates with semantic TXT companions, and twenty worked questions.
Computed traces are not wet-lab measurements. Primary-source inspection depths
are recorded in research/integration/ch25/source-verification.json. Build success
and local visual review do not imply independent scientific acceptance.
