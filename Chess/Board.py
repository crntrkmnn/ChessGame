from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King
import random

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.board[6][i] = Pawn('white')
        self.board[0][0] = self.board[0][7] = Rook('black')
        self.board[0][1] = self.board[0][6] = Knight('black')
        self.board[0][2] = self.board[0][5] = Bishop('black')
        self.board[0][3] = Queen('black')
        self.board[0][4] = King('black')

        self.board[7][0] = self.board[7][7] = Rook('white')
        self.board[7][1] = self.board[7][6] = Knight('white')
        self.board[7][2] = self.board[7][5] = Bishop('white')
        self.board[7][3] = Queen('white')
        self.board[7][4] = King('white')

    def get_board(self):
        return self.board

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if piece is not None:
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None

    def get_valid_moves(self, color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == color:
                    valid_moves.extend(piece.get_valid_moves(self.board, row, col))
        return valid_moves

    def make_random_move(self, color):
        valid_moves = self.get_valid_moves(color)
        if valid_moves:
            from_pos, to_pos = random.choice(valid_moves)
            self.move_piece(*from_pos, *to_pos)
