class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def __str__(self):
        if self.type == 'Empty':
            return 'nE'
        c = 'w' if self.color else 'b'
        p = 'N' if self.type == 'Knight' else self.type[0]
        return c + p
