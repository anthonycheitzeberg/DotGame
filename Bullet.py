class Bullet:
    def __init__(self, pos, vector, *args, **kwargs):
        self.pos = pos
        self.vector = vector
        self.size = kwargs.get("size", 5)
        self.color = kwargs.get("color", (255, 223, 0))

