from board import Board
from piece import Piece
import move_generator
import re
import copy

turn = True
b = Board()
b.print_board()
while True:
    requested_move = input('move: ')
    for move in move_generator.generate_moves(b, turn):
        if requested_move == move[1]:
            b.make_move(move)
            turn = not turn
            b.print_board()
            break



