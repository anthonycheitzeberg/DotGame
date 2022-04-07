import pygame
import numpy as np

from Tile import Tile
from assets.scripts.core_funcs import *


class TileMap:
    border = 160
    count = 10


    def __init__(self, rect=None):
        self.map = self.apply_automation(self.make_map(), self.count, self.border)

    def make_map(self):
        grid = []

        for i in range(self.border + 1):
            row = []
            grid.append(row)

            for m in range(self.border + 1):
                chance = random.randrange(0, 10)
                if chance <= 4:
                    row.append(Tile(type="0"))
                if chance >= 5:
                    row.append(Tile(type="1"))

        return grid

    def apply_automation(self, grid, count, border):
        i = 0
        while i < count:
            y = 0
            for y in range(border):
                x = 0
                for x in range(border):
                    one = 0
                    zero = 0
                    surrounding = [grid[y - 1][x], grid[y + 1][x], grid[y][x - 1],
                                   grid[y][x + 1], grid[y + 1][x + 1], grid[y + 1][x - 1],
                                   grid[y - 1][x + 1], grid[y - 1][x - 1]]

                    for m in surrounding:
                        match m.type:
                            case "0":
                                zero += 1
                            case "1":
                                one += 1

                    if zero > 4:
                        grid[y][x] = Tile(type="0")
                    if one > 4:
                        grid[y][x] = Tile(type="1")

                x += 1
            y += 1
            i += 1

        return grid

    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j * 32, i * 32))

    def set_zero(self):
        self.map = np.zeros(self.size, dtype=int)
        print(self.map)
        print(self.map.shape)
        self.render()

    def set_random(self):
        n = len(self.tileset.tiles)
        self.map = np.random.randint(n, size=self.size)
        print(self.map)
        self.render()

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
