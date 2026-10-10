# Historical material — not active edition

Original public commit: `fd41e8c360d8d8698bcf8bfc90bef4314b2dd384`.

Snapshot including unfinished earlier-request work: `3e10fc84bd81e733351da539e28b729eb1f007cf` on `archive/pre-reboot-20260905`.

`pre-reboot/book/` and `pre-reboot/research/` preserve the old files byte-for-byte. Their statuses are historical statements, not endorsements by the new edition. Their relative links may point to the original layout; use the snapshot branch for the fully reconstructable old working tree. No source text was destroyed.

Existing `code/` remains in its original location so tests and package imports continue to work. Its classification and limitations are in [the code audit](../REFERENCE_IMPLEMENTATION.md). Historical JSON records and their tests validate structure only, not scientific truth. In particular, the old DOGMA provenance record overgeneralizes a configuration: optional attention/scan in evo-trainer cannot be summarized as a universal recurrent-only lineage.

Restore for inspection in a separate worktree with `git worktree add ../dna-computing-book-historical archive/pre-reboot-20260905`. Do not reset the current development tree.
