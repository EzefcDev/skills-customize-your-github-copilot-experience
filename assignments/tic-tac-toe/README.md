# 📘 Assignment: Tic-Tac-Toe

## 🎯 Objective

Build a playable Tic-Tac-Toe (Tres en raya) game in Python. Students will practice arrays/lists, control flow, functions, and basic game logic.

## 📝 Tasks

### 🛠️ Implement the Tic-Tac-Toe game

#### Description
Create a terminal-based Tic-Tac-Toe game where a human player can play against a simple computer opponent (random moves) or against another human. The program should display the board, accept and validate player input, update the board, and detect win/draw conditions.

#### Requirements
Completed program should:

- Display the 3x3 board and update it after each valid move.
- Allow players to place X or O on an empty cell by entering a position (1–9) or row/column.
- Validate input and prevent moves on occupied cells.
- Detect and announce a win for X or O, or a draw when the board is full.
- Include a simple computer opponent that makes legal random moves (optional: make AI smarter for extra credit).

### 🛠️ Optional: Enhancements

#### Description
Add one or more improvements to make the game more robust or user-friendly.

#### Requirements (optional)

- Improve the computer opponent (minimax or heuristics).
- Add a replay loop so players can play multiple rounds without restarting.
- Add a scoring system that tracks wins/draws across rounds.
- Add ASCII-art or a nicer UI for the board display.

## Example gameplay (simplified)

```
Board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player X, enter a cell (1-9): 5
```

After game ends:

```
Player X wins! The final board was:
 X | O | X
---+---+---
 O | X | 6
---+---+---
 7 | 8 | O
```

---

How to run

```bash
python3 starter-code.py
```

Attachments

- `starter-code.py` — starter implementation to get students started.

Save this file as `README.md` inside `assignments/tic-tac-toe/`.
