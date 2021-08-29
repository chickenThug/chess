from piece import Piece
import re


class Board:
    def __init__(self):
        self.board = self.generate_starting_board()
        self.en_passant = 0

        # The first bit regulates weather the white king has moved the second weather the black king has moved.
        # The third weather the white queen rook has moved the fourth weather the black queen rook has moved
        # The fifth weather the white king rook has moved and the sixth weather the black king rook has moved
        # Where zero is false and 1 is true
        self.castling_state = 0

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
        moving_piece = self.get_piece(old_coordinate)
        color = moving_piece.get_color()
        # Update castling states
        if old_coordinate == (4, 7):
            self.castling_state = self.castling_state | 1
        elif old_coordinate == (4, 0):
            self.castling_state = self.castling_state | 2
        elif old_coordinate == (0, 7):
            self.castling_state = self.castling_state | 4
        elif old_coordinate == (0, 0):
            self.castling_state = self.castling_state | 8
        elif old_coordinate == (7, 7):
            self.castling_state = self.castling_state | 16
        elif old_coordinate == (7, 0):
            self.castling_state = self.castling_state | 32

        if move[1] == 'O-O-O':
            self.place_piece(Piece(True, 'Empty'), old_coordinate)
            self.place_piece(Piece(True, 'Empty'), (0, old_coordinate[1]))
            self.place_piece(Piece(color, 'Rook'), (3, old_coordinate[1]))
            self.place_piece(Piece(color, 'King'), (2, old_coordinate[1]))
        elif move[1] == 'O-O':
            self.place_piece(Piece(True, 'Empty'), old_coordinate)
            self.place_piece(Piece(True, 'Empty'), (7, old_coordinate[1]))
            self.place_piece(Piece(color, 'Rook'), (5, old_coordinate[1]))
            self.place_piece(Piece(color, 'King'), (6, old_coordinate[1]))
        else:
            x = re.search(".*[a-h][1-8]", move[1])
            m = x.group()
            new_coordinate = (ord(m[-2])-97, 8-int(m[-1]))
            target_square = self.get_piece(new_coordinate)
            # Update en_passant state
            if moving_piece.get_type() == 'Pawn' and abs(old_coordinate[1]-new_coordinate[1]) == 2:
                self.en_passant = ord(move[1][0])-96
            else:
                self.en_passant = 0
            # Handling en_passant captures
            if target_square.get_type() == 'Empty' and 'x' in move[1]:
                dir = 1 if color else -1
                self.place_piece(Piece(True, 'Empty'), (new_coordinate[0], new_coordinate[1]+dir))

            self.place_piece(moving_piece, new_coordinate)
            self.place_piece(Piece(True, 'Empty'), old_coordinate)

    def get_en_passant(self):
        return self.en_passant

    def get_castling_states(self):
        return self.castling_state

    def print_board(self):
        print('-----------------------------------------')
        for i in range(8):
            for j in range(8):
                print('|', self.board[j][i], end=' ')
            print('|')
            print('-----------------------------------------')
