from board import Board
from piece import Piece
import move_generator

b = Board()
b.print_board()
print(move_generator.generate_moves(b, True))
