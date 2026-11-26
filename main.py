"""Cat voicemail greeting entry for make.fun.

The grader runs this file with python3 -P -s and expects one short
text at /output/entry.txt (1 to 120 characters). The program is
deterministic: it always writes the same greeting, using only the
standard library, with no network, clock, or randomness involved.
"""

import os

GREETING = (
    "You've reached Waffles. I'm napping in a box that doesn't fit. "
    "Leave a message; I'll answer at 3 a.m. zoomies."
)

MAX_CHARS = 120


def output_path():
    """Return where the entry text belongs in the grader sandbox."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_greeting(text):
    """Refuse anything the gate would reject before writing it."""
    if not text.strip():
        raise ValueError("greeting must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("greeting exceeds 120 characters")
    return text


def main():
    text = check_greeting(GREETING)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
