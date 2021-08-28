from board import Board
from piece import Piece
import move_generator
import re
import copy

b = Board()
b.print_board()
print(move_generator.generate_moves(b, True))
b.make_move([(6, 7), 'Nf3'])
b.print_board()
print(move_generator.generate_moves(b, False))
b.make_move([(0, 1), 'a6'])
b.print_board()
print(move_generator.generate_moves(b, True))
b.make_move([(3, 6), 'd3'])
b.print_board()
print(move_generator.generate_moves(b, False))
b.make_move([(0, 0), 'Ra7'])
b.print_board()
print(move_generator.generate_moves(b, True))

