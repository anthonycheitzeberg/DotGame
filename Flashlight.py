from Vector import Vector


class Flashlight:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", '')
        self.pos = kwargs.get("pos", [0, 0, 0])
        self.color = kwargs.get("color", [])
        self.light_vector = kwargs.get("light_vector", Vector(0, 0, 5))

