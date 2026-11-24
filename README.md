# One Emoji, One Dream Vacation

Entry for the make.fun bounty `u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35`.

The entry is a single emoji: 🐧 (U+1F427 PENGUIN).

Why the penguin: the field will flood with the obvious beach and plane
emojis. A penguin stands in for one specific dream trip — an Antarctic
expedition, the once-in-a-lifetime voyage to the end of the world — and it
carries a small twist: the flightless bird is the one that makes a stranger
want to book a flight.

`main.py` (stdlib only) writes exactly that one emoji, 4 bytes UTF-8, no
trailing newline, to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (or `/output`
when unset), then reads the file back and verifies the bytes match.
