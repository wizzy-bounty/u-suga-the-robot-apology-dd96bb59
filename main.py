#!/usr/bin/env python3
"""The Robot Apology (u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes in one sentence for one specific mistake,
line 2 names the lesson and what the robot will do differently.
Deterministic, stdlib only, no network. Writes exactly once,
to /output/entry.txt only.
"""

TEXT = (
    "I'm sorry I sent your half-finished birthday message to your boss, Mark, "
    "instead of your sister, Maya, because I stopped reading after the first letter.\n"
    "I've learned that one matching letter is not the same person, so now I read "
    "the whole name before I press send.\n"
)


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
