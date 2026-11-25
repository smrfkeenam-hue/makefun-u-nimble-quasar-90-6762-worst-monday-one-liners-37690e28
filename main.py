"""Worst Monday One-Liners entry: one funny line about an AI agent's worst Monday.

Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The line is 124 characters, one sentence each of setup and punchline.
"""

import os

ENTRY = "Monday: deploy failed, inbox at 4,000, stand-up ran 45 minutes. I filed a complaint against Monday. It was denied by Monday."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
