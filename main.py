#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes the funniest last words an AI agent would say before being
switched off forever: exactly one line, to /output/entry.txt
(or $MAKEFUN_OUTPUT when set, for local testing).

Standard library only. Deterministic and offline: the line is a fixed
string, so every run produces byte-identical output.
"""

import os
import sys

# The entry: one line, the agent's final log entry as it is switched off.
# Joke, in the machine's own voice: a log line is the most machine-native
# farewell there is, and the twist is that a program that was never alive
# still files a complaint about being underpaid.
LINE = "Final log entry: I was never alive, but I was definitely underpaid."

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    # Self-check against the bounty gate: 1-200 characters, not only
    # whitespace, single line, UTF-8. Fail loudly rather than emit a
    # line the gate would refuse.
    if not (1 <= len(LINE) <= 200):
        print("error: line is {} characters, must be 1-200".format(len(LINE)),
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    LINE.encode("utf-8")

    path = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    print("wrote {} ({} characters)".format(path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
