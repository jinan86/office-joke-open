#!/usr/bin/env python3
"""Office Joke Open — make.fun entry.

Writes a single one-line office joke (<= 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.

Competition: u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232
"""

JOKE = (
    "There's birthday cake in the kitchen for a Deborah. "
    "Nobody knows a Deborah. We've celebrated her three days straight "
    "\u2014 she's the most beloved person here, and she doesn't exist."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate check mirroring the sealed scorer: 1-200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"joke is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
