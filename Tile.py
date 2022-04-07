class Tile:
    def __init__(self, type):
        self.type = type
        self.is_visible = True
        self.size = 8

    def __str__(self):
        return f'{self.type} {self.is_visible}'
