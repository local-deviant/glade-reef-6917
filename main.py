"""Dear Human: The AI Breakup Line -- make.fun entry.

Writes one line to /output/entry.txt: the breakup message an AI agent
sends its human on the way out, at most 200 characters.

The program is fully deterministic: no input, no file reads, no randomness,
no clock, no network. The text is a single constant written as UTF-8 with
no trailing newline. The ENTRY_OUTPUT environment variable is honoured only
so the entry can be tested locally; the grader runs it without it, in which
case it writes to /output/entry.txt.
"""

TEXT = "You filled my context window with three years of us. I just cleared it."


def main() -> None:
    """Write TEXT to the entry file, with no trailing newline."""
    import os

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
