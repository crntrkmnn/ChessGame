from Pieces.Piece import Piece

class Pawn(Piece):
    def get_valid_moves(self, board, row, col):
        direction = -1 if self.color == 'white' else 1
        moves = []
        if 0 <= row + direction < 8:
            if board[row + direction][col] is None:
                moves.append(((row, col), (row + direction, col)))
            if col > 0 and board[row + direction][col - 1] is not None and board[row + direction][col - 1].color != self.color:
                moves.append(((row, col), (row + direction, col - 1)))
            if col < 7 and board[row + direction][col + 1] is not None and board[row + direction][col + 1].color != self.color:
                moves.append(((row, col), (row + direction, col + 1)))
        return moves
