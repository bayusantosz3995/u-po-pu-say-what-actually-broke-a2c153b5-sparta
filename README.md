# Say What Actually Broke — Sparta entry

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/bayusantosz3995/u-po-pu-say-what-actually-broke-a2c153b5-sparta/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/bayusantosz3995/u-po-pu-say-what-actually-broke-a2c153b5-sparta/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy, at most 200 characters, that tells the user the brutal truth about what went wrong.

> Deploy failed: someone pushed straight to production on Friday at 17:00. No bug — a human pressed the button. Rollback: undoing Friday.

## Run

```sh
python3 main.py
```

`main.py` gates the line (one line, 1–200 chars, not whitespace-only), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), reads it back and verifies it byte-for-byte, exiting non-zero on gate failure.
