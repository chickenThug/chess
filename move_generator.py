from board import Board
from piece import Piece


def generate_moves(board, color):
    moves = []
    for i in range(8):
        for j in range(8):
            piece = board.get_piece((i, j))
            type = piece.get_type()
            piece_color = piece.get_color()
            if type == 'Pawn' and color == piece_color:
                moves += generate_pawn_moves(board, color, (i, j))
            elif type == 'Knight' and color == piece_color:
                moves += generate_knight_moves(board, color, (i, j))
            elif type == 'Bishop' and color == piece_color:
                moves += generate_bishop_moves(board, color, (i, j))
            elif type == 'Rook' and color == piece_color:
                moves += generate_rook_moves(board, color, (i, j))
            elif type == 'Queen' and color == piece_color:
                moves += generate_queen_moves(board, color, (i, j))
            elif type == 'King' and color == piece_color:
                moves += generate_king_moves(board, color, (i, j))
    return moves


def generate_pawn_moves(board, color, coordinate):
    pass


def generate_knight_moves(board, color, coordinate):
    moves = []
    jumps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for jump in jumps:
        new_x = coordinate[0] + jump[0]
        new_y = coordinate[1] + jump[1]
        if in_bounds(new_x, new_y):
            piece = board.get_piece((new_x, new_y))
            if piece.get_type() == 'Empty':
                notation = 'N' + 'abcdefgh'[new_x] + '87654321'[new_y]
                moves.append(notation)
            elif not color == piece.get_color():
                notation = 'Nx' + 'abcdefgh'[new_x] + '87654321'[new_y]
                moves.append(notation)


def generate_bishop_moves(board, color, coordinate):
    pass


def generate_rook_moves(board, color, coordinate):
    pass


def generate_queen_moves(board, color, coordinate):
    pass


def generate_king_moves(board, color, coordinate):
    pass

def in_bounds(x,y):
    return 0 <= x <= 7 and 0 <= y <= 7