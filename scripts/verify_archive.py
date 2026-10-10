"""Verify the byte-preserving relocation, without rewriting historical records."""

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT, require_local_pdfs=False):
    manifest = json.loads((root / "archive/manifest.json").read_text())
    legacy = root / manifest["legacy_root"]
    checked = 0
    absent_local_pdfs = 0
    for field in ("legacy_tracked_files", "legacy_pdf_hashes"):
        for relative, digest in manifest[field].items():
            path = legacy / relative
            if (
                field == "legacy_pdf_hashes"
                and relative not in manifest["legacy_tracked_files"]
                and not path.exists()
                and not require_local_pdfs
            ):
                absent_local_pdfs += 1
                continue
            if (
                not path.is_file()
                or hashlib.sha256(path.read_bytes()).hexdigest() != digest
            ):
                raise ValueError("Archived bytes changed or missing: " + relative)
            checked += 1
    return {
        "verified_entries": checked,
        "unavailable_local_only_pdfs": absent_local_pdfs,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-local-pdfs", action="store_true")
    args = parser.parse_args()
    print(json.dumps(verify(require_local_pdfs=args.require_local_pdfs)))
