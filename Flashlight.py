from Vector import Vector
from math import cos, sin


class Flashlight:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", '')
        self.pos = kwargs.get("pos", [0, 0, 0])
        self.points = kwargs.get("points",[])
        self.color = kwargs.get("color", [])
        self.light_vector = kwargs.get("light_vector", Vector(0, 0, 1))
        self.angle = kwargs.get("light_angle", .4)

    def get_points(self):
        pos2 = self.add_angle_to_vector(self.angle)
        pos3 = self.add_angle_to_vector(-self.angle)
        self.points = [self.pos, pos2, pos3]

    def add_angle_to_vector(self, angle):
        newX = self.pos[0] + ((self.light_vector.x * cos(angle) - self.light_vector.y * sin(angle)) * 70)
        newY= self.pos[1] + ((self.light_vector.x * sin(angle) + self.light_vector.y * cos(angle)) * 70)
        return [newX, newY]
