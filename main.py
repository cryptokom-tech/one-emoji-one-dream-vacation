"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji, U+1F30B VOLCANO, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): a volcano at dawn, the dream trip of a sunrise hike up a
faraway peak. One Unicode character, four UTF-8 bytes, no trailing newline.
"""

import os

EMOJI = "\U0001F30B"  # VOLCANO


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == EMOJI, f"entry.txt holds {written!r}, expected exactly one emoji"
    assert len(written) == 1 and len(written.encode("utf-8")) == 4


if __name__ == "__main__":
    main()
