# ai.py

import random

class AI:
    def __init__(self, board):
        self.board = board

    def make_move(self):
        empty_squares = [(r, c) for r in range(8) for c in range(8) if self.board.board[r][c] is None]
        if not empty_squares:
            return
        start = random.choice(empty_squares)
        end = random.choice(empty_squares)
        self.board.move_piece(start, end)
