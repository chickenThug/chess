from board import Board
from piece import Piece


def generate_moves(board):
    moves = []
    for i in range(8):
        for j in range(8):
            piece = board.get_piece((i, j))
            type = piece.get_type()
            color = piece.get_color()
            if type == 'Pawn':
                moves += generate_pawn_moves(color, (i, j))
            elif type == 'Knight':
                moves += generate_knight_moves(color, (i, j))
            elif type == 'Bishop':
                moves += generate_bishop_moves(color, (i, j))
            elif type == 'Rook':
                moves += generate_rook_moves(color, (i, j))
            elif type == 'Queen':
                moves += generate_queen_moves(color, (i, j))
            elif type == 'King':
                moves += generate_king_moves(color, (i, j))
    return moves


def generate_pawn_moves(color, coordinate):
    pass


def generate_knight_moves(color, coordinate):
    pass


def generate_bishop_moves(color, coordinate):
    pass


def generate_rook_moves(color, coordinate):
    pass


def generate_queen_moves(color, coordinate):
    pass


def generate_king_moves(color, coordinate):
    pass
