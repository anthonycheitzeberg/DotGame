import pygame, sys
from pygame.locals import *
from Player import Player
from Flashlight import Flashlight
import math
from Vector import Vector

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("My Pygame Window")

WINDOW_SIZE = (800, 800)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player1: Player = Player(pos=[400, 400])


def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            check_player_movement(event)
        screen.fill((0, 0, 0))
        check_player_rotation()
        draw_player()
        pygame.display.update()
        clock.tick(60)


def draw_player():
    player1.move(player1.movement_vector)
    player1.flashLight.get_points()
    pygame.draw.polygon(screen, (255, 255, 0), points=player1.flashLight.points)
    pygame.draw.circle(screen, player1.settings.color, player1.pos, player1.dimen)


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


def check_player_rotation():
    x, y = pygame.mouse.get_pos()
    player1.flashLight.light_vector = get_normalized_vector([x, y], player1.flashLight.pos)


def get_normalized_vector(pos1, pos2):
    x, y = pos1[0] - pos2[0], pos1[1] - pos2[1]
    length = math.sqrt(pow(x, 2) + pow(y, 2))
    return Vector(x/length, y/length, 5)

main_loop()