from Pieces.Piece import Piece

class King(Piece):
    def get_valid_moves(self, board, row, col):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d in directions:
            r, c = row + d[0], col + d[1]
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] is None or board[r][c].color != self.color):
                moves.append(((row, col), (r, c)))
        return moves
