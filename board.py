class Board:
    def __init__(self):
        self.board = self.generate_starting_board()

    def generate_starting_board(self):
        board = [[0 for i in range(8)] for j in range(8)]
        for k in range(8):
            board[1][k] = 1
            board[6][k] = 7
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