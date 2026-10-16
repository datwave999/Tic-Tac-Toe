# Tic-Tac-Toe 🎮

A Python-based command-line Tic-Tac-Toe game supporting both single-player (vs. AI) and two-player modes. Available in two versions: a classic text-only build and an emoji-enhanced build.

---

## Features

- **Two game modes** — play against a random-move AI or challenge a friend locally
- **Two display styles** — plain text for maximum compatibility, or emoji-decorated for a more expressive terminal experience
- **Tie detection** — the board resets automatically on a draw so you can keep playing
- **Motivational messages** — a random encouraging message is shown after every move
- **Cross-platform** — console clearing works on Windows, macOS, and Linux

---

## Files

| File | Version | Description |
|---|---|---|
| `tictactoe_text.py` | 3.1.2 | Text-only display using `X` and `O` |
| `tictactoe_emoji.py` | 3.2.1 | Emoji display using ⭕ and ❌ |

---

## Requirements

- Python 3.x
- No external libraries — uses only the Python standard library (`random`, `time`, `sys`, `subprocess`)

---

## Getting Started

**Clone the repository:**
```bash
git clone https://https://github.com/datwave999/Tic-Tac-Toe
cd your-repo-name
```

**Run the text version:**
```bash
python tictactoe_text.py
```

**Run the emoji version:**
```bash
python tictactoe_emoji.py
```

---

## How to Play

1. On launch, select a mode:
   - `1` — Single player (you vs. AI)
   - `2` — Two player (local)
2. Players take turns entering a position number from 1–9, corresponding to the board layout below:

```
~~~~~~~~~~~~~
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
~~~~~~~~~~~~~
```

3. The first player to align three marks in a row, column, or diagonal wins.
4. If all 9 cells are filled with no winner, the game declares a tie and resets the board.

---

## Notes

- The AI opponent selects moves randomly — it does not use a strategy algorithm.
- Console clearing uses `subprocess.run` with `sys.platform` detection, so it works correctly on Windows (`cls`), macOS, and Linux (`clear`) without any manual changes.

---

## License

This project is open source. Feel free to fork, modify, and share.
