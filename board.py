from piece import Piece


class Board:
    def __init__(self):
        self.board = self.generate_starting_board()

    def generate_starting_board(self):
        board = [[Piece(True, 'Empty') for i in range(8)] for j in range(8)]
        for k in range(8):
            board[k][1] = Piece(False, 'Pawn')
            board[k][6] = Piece(True, 'Pawn')

        board[1][7] = Piece(True, 'Knight')
        board[6][7] = Piece(True, 'Knight')
        board[1][0] = Piece(False, 'Knight')
        board[6][0] = Piece(False, 'Knight')

        board[0][7] = Piece(True, 'Rook')
        board[7][7] = Piece(True, 'Rook')
        board[0][0] = Piece(False, 'Rook')
        board[7][0] = Piece(False, 'Rook')

        board[2][7] = Piece(True, 'Bishop')
        board[5][7] = Piece(True, 'Bishop')
        board[2][0] = Piece(False, 'Bishop')
        board[5][0] = Piece(False, 'Bishop')

        board[3][7] = Piece(True, 'Queen')
        board[3][0] = Piece(False, 'Queen')

        board[4][7] = Piece(True, 'King')
        board[4][0] = Piece(False, 'King')

        return board

    def place_piece(self, piece, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        self.board[x][y] = piece

    def get_piece(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        return self.board[x][y]

    def make_move(self, move):
        old_coordinate = move[0]
        new_coordinate = move[1]
    def print_board(self):
        for i in range(8):
            print()
            for j in range(8):
                print(self.board[j][i], end=' ')
