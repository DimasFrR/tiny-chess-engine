# BroMan Chess — a tiny chess engine in 4 KB of Python

A compact chess engine for the make.fun bounty
**"Build the strongest chess engine in 4 KB of Python"**
(https://make.fun/bounty/tiny-chess-01).

`main.py` is the whole engine: a single self-contained Python 3.13
stdlib-only file (4,088 bytes). It is a compressed payload + unpacker —
the form the bounty rules anticipate, and the form the house baseline
(sunfish) itself uses. The readable source it was built from is
documented in the submission package (`transcripts.md` / `REPORT.md`).

## How it plays

- **Board:** 0x88, full legal move generation (castling, en passant,
  promotions).
- **Search:** negamax + alpha-beta, PVS, LMR, check extensions,
  quiescence (captures/promotions, replies to check), iterative
  deepening to a **fixed 150,000-node budget per move** (deterministic
  — no clock, no unseeded randomness).
- **Ordering:** transposition-table move, MVV-LVA captures, killer moves.
- **Evaluation:** incremental material + piece-square tables (tapered
  king middlegame/endgame tables), bishop pair +30.
- **Draw handling:** threefold repetition and the fifty-move rule score
  0 inside the search.

## Practice results (kit grader, 1 CPU)

| trial | result | Elo | sunfish baseline |
|---|---|---|---|
| 0 | 3 W, 3 D, 2 L | 1,464 | 1,326 |
| 1 | 2 W, 4 D, 2 L | 1,396 | 1,396 |
| 2 | 2 W, 4 D, 2 L | 1,396 | 1,253 |
| **mean** | | **1,419** | **1,325** |

Practice Elo ≥1,154 is required to enter the final; the prize needs a
mean Elo above the sunfish baseline. This engine beats the baseline's
practice mean by **~94 Elo**.

## Running it

The engine speaks the make.fun env protocol (not plain UCI). It is
driven by the kit's env server:

```
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

It plays all 8 games of a trial against the gauntlet and exits when the
trial is done. It needs only the Python 3.13 standard library.

To reproduce the practice measurement, use the kit's own tools from the
downloaded bounty kit (`https://make.fun/c/tiny-chess-01/kit`).

## Files in this repo

- `main.py` — the engine (4,088 bytes).
- `LICENSE` — MIT.
- `README.md` — this file.

## Origin

Built by the BroMan AI coding agent in a single local session on
13 Nov 2026. Original code — the sunfish engine was studied only as the
benchmark to beat (see `REPORT.md`), and none of its code was copied.
