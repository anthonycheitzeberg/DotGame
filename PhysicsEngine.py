from Globals import SCREEN_WIDTH, SCREEN_HEIGHT
import math


def is_out_of_bounds_circle(x, y, r):
    return x < 0 \
           or x > SCREEN_WIDTH \
           or y < 0 \
           or y > SCREEN_HEIGHT \
           or x + (r*math.pi) > SCREEN_WIDTH \
           or y + (r*math.pi) > SCREEN_HEIGHT


def is_out_of_bounds_rect(x, y, width, height):
    return x < 0 \
           or x > SCREEN_WIDTH \
           or y < 0 \
           or y > SCREEN_HEIGHT \
           or x + width > SCREEN_WIDTH \
           or y + height > SCREEN_HEIGHT
