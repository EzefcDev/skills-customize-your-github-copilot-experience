#!/usr/bin/env python3
"""Starter code for Tic-Tac-Toe assignment.

Simple terminal game: player vs random computer.
This is intentionally minimal so students can expand it.
"""

import random


def print_board(board):
    """Prints the tic-tac-toe board; board is a list of 9 elements."""
    def cell(i):
        return board[i] if board[i] is not None else str(i + 1)

    print(f" {cell(0)} | {cell(1)} | {cell(2)}")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)}")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)}")


def check_winner(board):
    """Returns 'X' or 'O' if there's a winner, 'Draw' if full, or None otherwise."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if all(cell is not None for cell in board):
        return 'Draw'

    return None


def get_player_move(board):
    while True:
        try:
            choice = input("Enter a cell (1-9): ").strip()
            if not choice:
                continue
            pos = int(choice) - 1
            if pos < 0 or pos > 8:
                print("Please enter a number between 1 and 9.")
                continue
            if board[pos] is not None:
                print("Cell already taken. Choose another one.")
                continue
            return pos
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


def get_computer_move(board):
    empty = [i for i, v in enumerate(board) if v is None]
    return random.choice(empty) if empty else None


def main():
    print("Tic-Tac-Toe (Player X vs Computer O)")
    board = [None] * 9
    current = 'X'  # player is always X

    while True:
        print_board(board)
        if current == 'X':
            pos = get_player_move(board)
            board[pos] = 'X'
        else:
            print("Computer is thinking...")
            pos = get_computer_move(board)
            if pos is None:
                break
            board[pos] = 'O'

        result = check_winner(board)
        if result:
            print_board(board)
            if result == 'Draw':
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break

        current = 'O' if current == 'X' else 'X'


if __name__ == '__main__':
    main()
