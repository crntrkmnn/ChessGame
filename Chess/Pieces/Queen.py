from Pieces.Piece import Piece

class Queen(Piece):
    def get_valid_moves(self, board, row, col):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d in directions:
            for i in range(1, 8):
                r, c = row + d[0] * i, col + d[1] * i
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] is None:
                        moves.append(((row, col), (r, c)))
                    elif board[r][c].color != self.color:
                        moves.append(((row, col), (r, c)))
                        break
                    else:
                        break
                else:
                    break
        return moves
