from pathlib import Path


def test_required_bootstrap_ledgers_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    required = [
        "research/source-map.md",
        "research/claims-ledger.md",
        "research/terminology.md",
        "research/architecture-lineage.md",
        "research/dna-llm-branch-map.md",
        "book/NOTATION.md",
    ]
    assert all((root / path).is_file() for path in required)

