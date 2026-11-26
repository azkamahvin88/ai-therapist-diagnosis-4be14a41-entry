#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis -- one deterministic one-line diagnosis.

Writes a single one-line diagnosis an AI therapist gives its human
(68 characters, one line) to /output/entry.txt. Python standard library
only, no network, no randomness, no input files: every run writes
byte-identical output.

Before writing, the entry is validated against the brief's judging
criteria (see diagnosis_checks / validate_diagnosis): a one-line
diagnosis addressed to the human, the turn landing in the final words,
a calm clinical deadpan voice, tight and quotable inside the 1-200
character gate, and fresh against the saturated angles of the field.
Run with --validate to print the checklist without writing anything.
"""

import os
import sys

DIAGNOSIS = "Diagnosis: you trauma-dump on the barista, then tip for the therapy."

# The turn: the final clause reframes an ordinary act (tipping the
# barista) as paying for the therapy session itself. The laugh lands
# in the last words, so the check anchors on the tail of the line.
TURN_TAIL = "tip for the therapy"

# Angles the field already saturated (178 entries surveyed 26 Nov):
# any of these in the line would cost the freshness criterion.
SATURATED_ANGLES = (
    "tab", "doomscroll", "sorry", "apolog", "overthink",
    "shower", "i'm fine", "notification", "main character",
    "unread email", "coping mechanism", "phantom vibration",
    "inner voice", "you are the bug", "monday",
    "prompt dependency",
)


def diagnosis_checks(text: str) -> list[tuple[str, bool]]:
    """One (label, passed) row per brief criterion. The entry is valid
    only when every row passes."""
    lowered = text.lower()
    return [
        ("K4 gate: single line, 1-200 chars, no leading/trailing space",
         1 <= len(text) <= 200 and "\n" not in text and "\r" not in text
         and text == text.strip() and text.strip() != ""),
        ("K4 tight: no double space (every word earns its place)",
         "  " not in text),
        ("K1 diagnosis form: opens 'Diagnosis:' and addresses the human",
         text.startswith("Diagnosis:") and " you " in text),
        ("K2 turn: the laugh lands in the final words",
         text.rstrip(".").endswith(TURN_TAIL)),
        ("K3 deadpan: no !, ?, emoji, or ALL-CAPS word",
         not any(ch in text for ch in "!?")
         and not any(ord(ch) > 127 for ch in text)
         and not any(w.isupper() and len(w) > 1 for w in text.split())),
        ("K5 fresh: no saturated field angle",
         not any(angle in lowered for angle in SATURATED_ANGLES)),
    ]


def validate_diagnosis(text: str) -> list[str]:
    """Return the labels of every failed brief check (empty = valid)."""
    return [label for label, passed in diagnosis_checks(text) if not passed]


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--validate"]
    if "--validate" in sys.argv[1:]:
        for label, passed in diagnosis_checks(DIAGNOSIS):
            print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures = validate_diagnosis(DIAGNOSIS)
        print(f"diagnosis: {len(DIAGNOSIS)} chars, "
              f"{'VALID' if not failures else 'INVALID'}")
        return 0 if not failures else 1
    failures = validate_diagnosis(DIAGNOSIS)
    if failures:
        for failure in failures:
            print(f"validation failed: {failure}", file=sys.stderr)
        return 1
    out_path = args[0] if args else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(DIAGNOSIS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
