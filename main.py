#!/usr/bin/env python3
"""Fortune in a Pot — variant C (succulent plotting world domination).

Writes one original fortune for a succulent on the windowsill to
/output/entry.txt (first) and to entry.txt next to this file (best effort,
read-only safe). Deterministic: no randomness, no network.
"""

import os

FORTUNE = "Soon you will rule this sunny windowsill, then the house, then the world — your tiny leaves already have a plan."


def main() -> None:
    line = FORTUNE
    assert 1 <= len(line) <= 120, f"length {len(line)} out of range"
    assert line.strip(), "fortune must not be only whitespace"
    assert "\n" not in line, "fortune must be a single line"
    assert line == line.strip(), "no leading/trailing whitespace allowed"
    assert "  " not in line, "no double spaces allowed"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass
    print(f"{len(line)} chars: {line}")


if __name__ == "__main__":
    main()
