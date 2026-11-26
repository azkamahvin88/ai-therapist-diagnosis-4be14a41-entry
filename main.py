#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis -- one deterministic one-line diagnosis.

Writes a single one-line diagnosis an AI therapist gives its human
(68 characters, one line) to /output/entry.txt. Python standard library
only, no network, no randomness, no input files: every run writes
byte-identical output.
"""

import os
import sys

DIAGNOSIS = "Diagnosis: you trauma-dump on the barista, then tip for the therapy."


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(DIAGNOSIS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
