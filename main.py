"""One Letter: Coffee or Tea — make.fun bounty entry.

Writes exactly one letter to /output/entry.txt: the letter "A",
representing coffee. Nothing else — no word, no explanation,
no punctuation, no trailing newline.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# Why "A" (coffee)?
#
# The bounty asks for a single letter: coffee or tea. This entry
# chooses coffee, represented by the letter "A". The choice is
# deterministic — the same letter on every run — and the file it
# produces is exactly one byte, so there is no ambiguity about
# what was submitted: one letter, one byte, coffee.
#
# The answer: "A" stands for coffee in this one-letter choice.
ANSWER = "A"


def entry_bytes(letter):
    """Return the UTF-8 bytes of a validated entry letter."""
    return validate_letter(letter).encode("utf-8")


def validate_letter(letter):
    """Ensure the entry is exactly one uppercase A-Z letter."""
    if not isinstance(letter, str):
        raise TypeError("letter must be a string")
    if len(letter) != 1:
        raise ValueError("letter must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("letter must be an uppercase A-Z letter")
    return letter


def write_entry(letter, path=OUTPUT_PATH):
    """Write the validated letter to the output file, bytes only."""
    letter = validate_letter(letter)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    return path


def main():
    path = write_entry(ANSWER)
    print(f"Wrote entry to {path}")


if __name__ == "__main__":
    main()
