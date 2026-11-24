"""The Robot Apology entry.

Writes one short text of two lines to ``/output/entry.txt``, the one
path the grader reads. The text must be UTF-8, 1 to 400 characters,
and not only white space, so the program checks its own length
before writing and writes the exact text, with no trailing newline
and no extra output in the file.

Line one is a robot apologizing in a single sentence for one specific
mistake it made. Line two is one sentence saying what the robot
learned and what it will do differently, and the lesson has to follow
from that exact mistake rather than be a generic promise to do better.

The mistake is deliberately not the one every other entry reaches
for: no watered plant, no filed report, no woken baby. A kitchen
robot shelved the cinnamon where the cumin lives because both jars
are the same height, so the curry tasted like Christmas morning --
concrete, human-scale, and exactly the kind of small slip a person
would really make. The lesson follows from that mistake and nothing
else: matching by size is not matching at all, so the changed
behaviour is to read the label before moving a jar, not after. The
voice stays a machine noticing its own slip: it talks about matching,
labels, and the order of its own steps, not about feelings.

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment, or the git history -- the apology lives in
this file, and this file alone.
"""

import os
from pathlib import Path

# One original two-line robot apology. Line one owns the specific
# mistake -- cinnamon shelved as cumin, because the jars match in
# height -- and lands the consequence in one image. Line two draws
# the lesson straight out of that mistake: size is not identity, so
# the fix is to read the label before moving a jar, never after. Each
# line is exactly one sentence, so the confession does its job first
# and the resolve second, with no padding in either.
APOLOGY = (
    "I'm sorry I shelved the cinnamon where the cumin lives because "
    "both jars are the same height, so your curry tasted like "
    "Christmas morning.\n"
    "I learned that matching by size is not matching at all, so now "
    "I read the label before I move a jar, not after."
)

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
MAX_CHARS = 400


def main() -> None:
    text = APOLOGY.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"apology is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"apology must be exactly two lines, got {len(lines)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
