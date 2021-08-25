from board import Board


class Game:
    def __init__(self):
        # game states
        self.game_states = 0

        # game board
        self.board = Board()

        # moves
        self.moves = []
        self.update_moves()

    def generate_pawn_moves(self, color, coordinate):
        moves = []
        if color:
            dir = -1
            start_row = 6
            next_to_last_row = 1
            min = 6
            max = 13
        else:
            dir = 1
            start_row = 1
            next_to_last_row = 6
            min = 0
            max = 7
        if coordinate[1] == next_to_last_row:
            promotion = True
        else:
            promotion = False

        piece_infront = self.board.get_piece((coordinate[0], coordinate[1]+1*dir))
        # Check if the pawn can move one space forward
        if piece_infront == 0:
            if promotion:
                for p in 'QRBN':
                    notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1] + 1 * dir] + '=' + p
                    moves.append(notation)
            else:
                notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1]+1*dir]
                moves.append(notation)
            # Check if the pawn is on its starting square
            if start_row == coordinate[1]:
                piece_two_infront = self.board.get_piece((coordinate[0], coordinate[1] + 2 * dir))
                # Check if the pawn can move two spaces forward
                if piece_two_infront == 0:
                    notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1] + 2 * dir]
                    moves.append(notation)
        # Check if captures are available
        if coordinate[0] > 0:
            piece_left_ahead = self.board.get_piece((coordinate[0]-1, coordinate[1]+1*dir))
            if min < piece_left_ahead < max:
                if promotion:
                    for p in 'QRBN':
                        notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0]-1] + '87654321'[coordinate[1] + 1 * dir] + '=' + p
                        moves.append(notation)
                else:
                    notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0] - 1] + '87654321'[coordinate[1] + 1 * dir]
                    moves.append(notation)
        if coordinate[0] < 7:
            piece_right_ahead = self.board.get_piece((coordinate[0]+1, coordinate[1]+1*dir))
            if min < piece_right_ahead < max:
                if promotion:
                    for p in 'QRBN':
                        notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0]+1] + '87654321'[coordinate[1] + 1 * dir] + '=' + p
                        moves.append(notation)
                else:
                    notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0] + 1] + '87654321'[coordinate[1] + 1 * dir]
                    moves.append(notation)
        return moves

    def update_moves(self):
        # reset moves
        self.moves = []
        # iterate over the board and add avaialable moves for all pieces
        for i in range(8):
            for j in range(8):
                piece = self.board.get_piece((i, j))
                if piece == 1:
                    self.moves += self.generate_pawn_moves(True, (i, j))
                elif piece == 7:
                    self.moves += self.generate_pawn_moves(False, (i, j))