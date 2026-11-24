"""Last Text at One Percent.

Writes the final text message a phone sends at 1% battery —
one line, in the phone's own voice, before the screen goes dark.
"""

import os

# The last text message, in the phone's own voice. One line, under 200 chars.
LAST_TEXT = (
    "1%. going dark. tell the charger it was never the cable, "
    "it was the distance. tell the apps i never liked them anyway. "
    "xoxo, your phone"
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LAST_TEXT + "\n")


if __name__ == "__main__":
    main()
