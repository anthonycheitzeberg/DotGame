class Player:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", '')
        self.pos = kwargs.get("pos", [])
        self.settings - kwargs.get("settings", PlayerSettings())
        self.stats = kwargs.get("stats", PlayerStats())

    def move(self, vector: Vector):
        self.pos = [self.pos[0] + vector.x * (vector.speed * stats.movement_speed),
                    self.pos[1] + vector.y * (vector.speed * stats.movement_speed)]


class PlayerSettings:
    def __init__(self, *args, **kwargs):
        self.username = kwargs.get("username", "Player")
        self.color = kwargs.get("color", [0, 0, 0])


class PlayerStats:
    def __init__(self, *args, **kwargs):
        self.movement_speed = kwargs.get("speed", 1)