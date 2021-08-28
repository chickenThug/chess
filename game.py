from board import Board
from piece import Piece
import move_generator
import re
import copy

b = Board()
b.make_move([(4, 6), 'e3'])
b.make_move([(0, 1), 'a5'])
b.make_move([(5, 7), 'Bb5'])
b.print_board()
print()
print(move_generator.temp_name(b, False))
