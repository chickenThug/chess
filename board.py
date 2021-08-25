class Board:
    def __init__(self):
        self.board = self.generate_starting_board()

    def generate_starting_board(self):
        board = [[0 for i in range(8)] for j in range(8)]
        # Place pawns where 1 corresponds to white pawn and 7 to black pawn
        for k in range(8):
            board[k][1] = 7
            board[k][6] = 1
        return board

    def place_piece(self, piece, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        self.board[x][y] = piece

    def get_piece(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        return self.board[x][y]

    def print_board(self):
        for i in range(8):
            print()
            for j in range(8):
                print(self.board[i][j], end=' ')