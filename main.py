#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to entry.txt: the penguin, standing in for a
dream trip to Antarctica -- the flightless bird that makes a stranger
want to book a flight.

Stdlib only. The output path is MAKEFUN_OUTPUT_DIR when set, otherwise
/output. The written bytes are read back and verified before exit.
"""

import os
import sys

EMOJI = "\U0001F427"  # PENGUIN -- one code point, 4 bytes in UTF-8.


def is_single_emoji(text):
    if len(text) != 1:
        return False
    code = ord(text)
    return 0x1F000 <= code <= 0x1FAFF or 0x2600 <= code <= 0x27BF


def main():
    if not is_single_emoji(EMOJI):
        print("error: entry is not exactly one emoji", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = EMOJI.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    # Gate rule: entry must be 1-8 characters, no newline. Verify the
    # artifact itself: exactly 4 bytes that decode to exactly 1 char.
    assert len(written) == 4, "entry must be exactly 4 bytes"
    assert len(written.decode("utf-8")) == 1, "entry must decode to 1 character"

    print("wrote %d byte(s) to %s" % (len(written), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
