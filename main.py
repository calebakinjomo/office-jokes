"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one original one-line office joke to /output/entry.txt.
Deterministic: no network, no clock, no randomness, no environment reads.

The joke: a setup everyone in an office recognises ("drowning in work"),
then a turn nobody sees coming — the boss takes the metaphor literally
and answers the only way a manager knows how: with a calendar invite.
"""

import os

# One line, 85 characters: setup, then the punch lands on "Swimming Lessons."
JOKE = "I told my boss I was drowning in work. He sent a calendar invite: 'Swimming Lessons.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
