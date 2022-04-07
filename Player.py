from Vector import Vector
from Flashlight import Flashlight
import PhysicsEngine

class Player:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", '')
        self.pos = kwargs.get("pos", [])
        self.dimen = kwargs.get("dimen", 9)
        self.settings = kwargs.get("settings", PlayerSettings())
        self.stats = kwargs.get("stats", PlayerStats())
        self.movement_vector = kwargs.get("movement_vector", Vector(0, 0, 3))
        self.flashLight = kwargs.get("flashlight", Flashlight(pos=self.pos))

    def move(self, vector: Vector):
        new_pos = [self.pos[0] + vector.x * (vector.speed * self.stats.movement_speed),
                    self.pos[1] + vector.y * (vector.speed * self.stats.movement_speed)]
        if PhysicsEngine.is_out_of_bounds_circle(new_pos[0], new_pos[1], self.dimen):
            pass
        else:
            self.pos = new_pos
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
