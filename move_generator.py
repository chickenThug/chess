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
                moves += generate_pawn_moves(board, (i, j))
            elif type == 'Knight' and color == piece_color:
                moves += generate_knight_moves(board, (i, j))
            elif type == 'Bishop' and color == piece_color:
                moves += generate_bishop_moves(board, (i, j))
            elif type == 'Rook' and color == piece_color:
                moves += generate_rook_moves(board, (i, j))
            elif type == 'Queen' and color == piece_color:
                moves += generate_queen_moves(board, (i, j))
            elif type == 'King' and color == piece_color:
                moves += generate_king_moves(board, (i, j))
    return moves


def generate_pawn_moves(board, coordinate):
    moves = []
    color = board.get_piece(coordinate).get_color()
    dir = -1 if color else 1
    start_row = 6 if color else 1
    next_to_last_row = 1 if color else 6
    promotion = True if next_to_last_row == coordinate[1] else False

    piece_one_square_ahead = board.get_piece((coordinate[0], coordinate[1] + dir)).get_type()
    if piece_one_square_ahead == 'Empty':
        if promotion:
            for p in 'NBRQ':
                notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1] + dir] + '=' + p
                moves.append(notation)
        else:
            notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1] + dir]
            moves.append(notation)
        if start_row == coordinate[1]:
            piece_two_squares_ahead = board.get_piece((coordinate[0], coordinate[1] + 2 * dir)).get_type()
            if piece_two_squares_ahead == 'Empty':
                notation = 'abcdefgh'[coordinate[0]] + '87654321'[coordinate[1] + 2 * dir]
                moves.append(notation)

    if coordinate[0] > 0:
        piece = board.get_piece((coordinate[0]-1, coordinate[1]+dir))
        if not piece.get_type() == 'Empty' and not piece.get_color() == color:
            if promotion:
                for p in 'NBRQ':
                    notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0]-1] + '87654321'[coordinate[1] + dir] + '=' + p
                    moves.append(notation)
            else:
                notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0] - 1] + '87654321'[coordinate[1] + dir]
                moves.append(notation)

    if coordinate[0] < 7:
        piece = board.get_piece((coordinate[0]+1, coordinate[1]+dir))
        if not piece.get_type() == 'Empty' and not piece.get_color() == color:
            if promotion:
                for p in 'NBRQ':
                    notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0]+1] + '87654321'[coordinate[1]+dir] + '=' + p
                    moves.append(notation)
            else:
                notation = 'abcdefgh'[coordinate[0]] + 'x' + 'abcdefgh'[coordinate[0]+1] + '87654321'[coordinate[1]+dir]
                moves.append(notation)
    return moves


def generate_knight_moves(board, coordinate):
    moves = []
    color = board.get_piece(coordinate).get_color()
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
    return moves


def generate_bishop_moves(board, coordinate):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return moves_helper(board, coordinate, directions)


def generate_rook_moves(board, coordinate):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return moves_helper(board, coordinate, directions)


def generate_queen_moves(board, coordinate):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, -1), (-1, 0), (0, 1)]
    return moves_helper(board, coordinate, directions)


def generate_king_moves(board, coordinate):
    moves = []
    color = board.get_piece(coordinate).get_color()
    for i in range(3):
        for j in range(3):
            x = coordinate[0] + i - 1
            y = coordinate[1] + j - 1
            if in_bounds(x, y):
                piece = board.get_piece((x,y))
                if piece.get_type() == 'Empty':
                    notation = 'K' + 'abcdefgh'[x] + '87654321'[y]
                    moves.append(notation)
                elif not piece.get_color() == color:
                    notation = 'Kx' + 'abcdefgh'[x] + '87654321'[y]
                    moves.append(notation)
    return moves


# Helper function for the generation of bishop, rook and queen moves
def moves_helper(board, coordinate, directions):
    moves = []
    color = board.get_piece(coordinate).get_color()
    type = board.get_piece(coordinate).get_type()[0]
    for dir in directions:
        x = coordinate[0] + dir[0]
        y = coordinate[1] + dir[1]
        while in_bounds(x, y):
            if board.get_piece((x, y)).get_type() == 'Empty':
                notation = type + 'abcdefgh'[x] + '87654321'[y]
                moves.append(notation)
                x += dir[0]
                y += dir[1]
            elif board.get_piece((x, y)).get_color() == color:
                break
            else:
                notation = type + "x" + 'abcdefgh'[x] + '87654321'[y]
                moves.append(notation)
                break
    return moves


def in_bounds(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7
