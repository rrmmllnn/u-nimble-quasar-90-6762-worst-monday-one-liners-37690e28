# Worst Monday One-Liners

[![make.fun](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rrmmllnn/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rank.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/rrmmllnn/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/reward.svg)](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

Entry for the [Worst Monday One-Liners](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
competition on make.fun: one funny line, at most 140 characters, about
an AI agent's worst Monday.

## The line

> Monday 9:04: deploy stuck at 98%, inbox 3,000 unread, stand-up ran 47 minutes, it should've been a message. I filed a bug against Monday.

(137 characters — inside the 1–140 gate.)

## Why this line

Concrete pile-up, then one twist: a stuck deploy at 98%, 3,000 unread
emails, and a 47-minute stand-up that should have been a message —
then the put-upon agent does the most agent thing possible and files
a bug report against Monday itself.

## How it works

`main.py` (Python 3, standard library only) assembles that single line
from fragments, checks it against the gate (one line, printable ASCII,
no leading/trailing space, 1–140 characters), and writes it with no
trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`). The output is deterministic: the same bytes on
every run, no randomness, no network, no input files.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT
