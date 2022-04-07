import pygame, sys
from pygame.locals import *

import TileMap
from Player import Player
from Flashlight import Flashlight
import math

from Tile import Tile
from Vector import Vector
from Bullet import Bullet
import PhysicsEngine
from Globals import SCREEN_WIDTH, SCREEN_HEIGHT
from assets.scripts.core_funcs import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("My Pygame Window")

WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player1: Player = Player(pos=[400, 400])

bullets: [Bullet] = []

tile_size = 8

water = pygame.Surface((tile_size, tile_size))
water.fill((79, 76, 176))

grass = pygame.Surface((tile_size, tile_size))
grass.fill((0, 175, 0))

tiles = [water, grass]

tile_map = TileMap.TileMap()
mapping = tile_map.map


def load_map(grid, tiles):
    y = 0
    for tile in grid:
        x = 0
        for cell in tile:
            if cell.type == "0":
                screen.blit(tiles[0], (x * tile_size, y * tile_size))
            if cell.type == "1":
                screen.blit(tiles[1], (x * tile_size, y * tile_size))
            x += 1
        y += 1


def main_loop():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        calculate_objects(mouse_pos)
        draw_objects()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            check_player_movement(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot_bullet()

        clock.tick(60)


def draw_objects():
    cover_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    cover_surf.set_colorkey((255, 255, 255))
    cover_surf.fill(0)
    draw_flashlight(cover_surf)
    draw_player(cover_surf)
    screen.fill(0)
    load_map(mapping, tiles)
    draw_bullet()
    screen.blit(cover_surf, (0, 0))
    pygame.display.flip()


def calculate_objects(mouse_pos):
    check_player_rotation(mouse_pos)
    player1.move(player1.movement_vector)
    player1.flashLight.get_points()
    for bullet in bullets:
        bullet.vector.speed = 5
        bullet.pos[0] += bullet.vector.x * bullet.vector.speed
        bullet.pos[1] += bullet.vector.y * bullet.vector.speed
        if PhysicsEngine.is_out_of_bounds_circle(bullet.pos[0], bullet.pos[1], bullet.size):
            bullets.remove(bullet)


def draw_player(surface):
    pygame.draw.circle(surface, player1.settings.color, player1.pos, player1.dimen)


def draw_flashlight(surface):
    pygame.draw.polygon(surface, (255, 255, 255), points=player1.flashLight.points)


def draw_bullet():
    for bullet in bullets:
        pygame.draw.circle(screen, bullet.color, bullet.pos, bullet.size)


def check_player_movement(event: pygame.event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            player1.movement_vector.x -= 1
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            player1.movement_vector.x += 1
        if event.key == pygame.K_UP or event.key == ord('w'):
            player1.movement_vector.y -= 1
        if event.key == pygame.K_UP or event.key == ord('s'):
            player1.movement_vector.y += 1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            player1.movement_vector.x += 1
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            player1.movement_vector.x -= 1
        if event.key == pygame.K_UP or event.key == ord('w'):
            player1.movement_vector.y += 1
        if event.key == pygame.K_UP or event.key == ord('s'):
            player1.movement_vector.y -= 1


def check_player_rotation(mouse_pos):
    x, y = mouse_pos
    if [x, y] != player1.pos:
        player1.flashLight.light_vector = get_normalized_vector([x, y], player1.flashLight.pos)


def get_normalized_vector(pos1, pos2):
    x, y = pos1[0] - pos2[0], pos1[1] - pos2[1]
    length = math.sqrt(pow(x, 2) + pow(y, 2))
    return Vector(x / length, y / length, 5)


def shoot_bullet():
    bullets.append(Bullet(player1.pos, player1.flashLight.light_vector))


main_loop()
