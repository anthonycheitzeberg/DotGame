class Bullet:
    def __init__(self, pos, vector, *args, **kwargs):
        self.pos = pos
        self.vector = vector
        self.size = kwargs.get("size", 3)
        self.color = kwargs.get("color", (255, 255, 255))

