class Piece:
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, board, row, col):
        raise NotImplementedError("This method should be implemented by subclasses")
