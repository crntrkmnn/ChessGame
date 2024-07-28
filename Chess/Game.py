class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "White"
        self.ai = AI("Black")

    def play(self):
        while True:
            self.board.print_board()
            if self.current_player == "White":
                print("White's turn")
                self.player_move()
            else:
                print("Black's turn")
                self.ai_move()

            if self.check_winner():
                print(f"{self.current_player} wins!")
                self.board.print_board()
                break

            self.current_player = "Black" if self.current_player == "White" else "White"

    def player_move(self):
        start_row = int(input("Enter start row: "))
        start_col = int(input("Enter start column: "))
        end_row = int(input("Enter end row: "))
        end_col = int(input("Enter end column: "))
        self.board.move_piece((start_row, start_col), (end_row, end_col))

    def ai_move(self):
        move = self.ai.choose_move(self.board)
        if move:
            (start_pos, end_pos) = move
            self.board.move_piece(start_pos, end_pos)
            print(f"AI moved from {start_pos} to {end_pos}")

    def check_winner(self):
        # Basit bir kontrol; kazananı kontrol etme fonksiyonu eksik
        return False
