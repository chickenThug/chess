class Piece:
    def __init__(self, color, piece):
        self.color = color
        self.piece = piece

    def get_piece(self):
        return self.piece

    def get_color(self):
        return self.color

    def __str__(self):
        if self.piece == 'Empty':
            return 'nE'
        c = 'w' if self.color else 'b'
        p = 'N' if self.piece == 'Knight' else self.piece[0]
        return c + p


