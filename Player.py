from Vector import Vector
from Flashlight import Flashlight


class Player:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", '')
        self.pos = kwargs.get("pos", [])
        self.dimen = kwargs.get("dimen", 7)
        self.settings = kwargs.get("settings", PlayerSettings())
        self.stats = kwargs.get("stats", PlayerStats())
        self.movement_vector = kwargs.get("movement_vector", Vector(0, 0, 3))
        self.flashLight = kwargs.get("flashlight", Flashlight(pos=self.pos))

    def move(self, vector: Vector):
        self.pos = [self.pos[0] + vector.x * (vector.speed * self.stats.movement_speed),
                    self.pos[1] + vector.y * (vector.speed * self.stats.movement_speed)]
        self.update_flashlight_pos()

    def update_flashlight_pos(self):
        self.flashLight.pos = self.pos


class PlayerSettings:
    def __init__(self, *args, **kwargs):
        self.username = kwargs.get("username", "Player")
        self.color = kwargs.get("color", [255, 0, 0])


class PlayerStats:
    def __init__(self, *args, **kwargs):
        self.movement_speed = kwargs.get("movement_speed", 1)
        self.player_size = kwargs.get("player_size", 1)
