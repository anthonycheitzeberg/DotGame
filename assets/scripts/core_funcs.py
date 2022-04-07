import pygame, math, os
import random


def read_f(path):
    f = open(path, 'r')
    dat = f.read()
    f.close()
    return dat


def write_f(path, dat):
    f = open(path, 'w')
    f.write(dat)
    f.close()


def load_image_dir(path, colorkey=(0, 0, 0)):
    images = {}
    for img_name in os.listdir(path):
        img = pygame.image.load(path + '/' + img_name).convert()
        img.set_colorkey(colorkey)
        images[img_name.split('.')[0]] = img.copy()
    return images


def warp_surf(surface, mask, loc, shift):
    offset = [mask.get_width() // 2, mask.get_height() // 2]
    loc = [loc[0] - offset[0], loc[1] - offset[1]]
    subsurf = clip(surface, loc[0], loc[1], mask.get_width(), mask.get_height())
    mask.set_colorkey((255, 255, 255))
    subsurf.blit(mask, (0, 0))
    subsurf.set_colorkey((0, 0, 0))
    surface.blit(subsurf, (loc[0] + shift[0], loc[1] + shift[1]))


def swap_color(img, old_c, new_c):
    global e_colorkey
    img.set_colorkey(old_c)
    surf = img.copy()
    surf.fill(new_c)
    surf.blit(img, (0, 0))
    return surf


def clip(surf, x, y, x_size, y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x, y, x_size, y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def rect_corners(points):
    point_1 = points[0]
    point_2 = points[1]
    out_1 = [min(point_1[0], point_2[0]), min(point_1[1], point_2[1])]
    out_2 = [max(point_1[0], point_2[0]), max(point_1[1], point_2[1])]
    return [out_1, out_2]


def corner_rect(points):
    points = rect_corners(points)
    r = pygame.Rect(points[0][0], points[0][1], points[1][0] - points[0][0], points[1][1] - points[0][1])
    return r


def points_between_2d(points):
    points = rect_corners(points)
    width = points[1][0] - points[0][0] + 1
    height = points[1][1] - points[0][1] + 1
    point_list = []
    for y in range(height):
        for x in range(width):
            point_list.append([points[0][0] + x, points[0][1] + y])
    return point_list


def angle_to(points):
    return math.atan2(points[1][1] - points[0][1], points[1][0] - points[0][0])


def horizontal_crop(loc_x, width, img):
    loc_x = int(loc_x)
    loc_x = loc_x % img.get_width()
    if loc_x + width <= img.get_width():
        return img.copy()
    else:
        left_sec = img.get_width() - loc_x
        right_sec = width - left_sec
        output_surf = pygame.Surface((width, img.get_height()))
        output_surf.blit(clip(img, loc_x, 0, left_sec, img.get_height()), (0, 0))
        output_surf.blit(clip(img, 0, 0, right_sec, img.get_height()), (left_sec, 0))
        colorkey = img.get_colorkey()
        output_surf.set_colorkey(colorkey)
        return output_surf


def blit_center(surf, surf2, pos):
    x = int(surf2.get_width() / 2)
    y = int(surf2.get_height() / 2)
    surf.blit(surf2, (pos[0] - x, pos[1] - y))


def get_center_pos(surf):
    return [surf.get_width() / 2, surf.get_height() / 2]


def normalize(num, amt):
    if num > amt:
        num -= amt
    elif num < -amt:
        num += amt
    else:
        num = 0
    return num


def generate_noise(width, height):
    noise_map = []
    # Populate a noise map with 0s
    for y in range(height):
        new_row = []
        for x in range(width):
            new_row.append(0)
        noise_map.append(new_row)

    # Progressively apply variation to the noise map but changing values + or -
    # 5 from the previous entry in the same list, or the average of the
    # previous entry and the entry directly above
    new_value = 0
    top_of_range = 0
    bottom_of_range = 0
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue
            if y == 0:  # If the current position is in the first row
                new_value = noise_map[y][x - 1] + random.randint(-1000, +1000)
            elif x == 0:  # If the current position is in the first column
                new_value = noise_map[y - 1][x] + random.randint(-1000, +1000)
            else:
                minimum = min(noise_map[y][x - 1], noise_map[y - 1][x])
                maximum = max(noise_map[y][x - 1], noise_map[y - 1][x])
                average_value = minimum + ((maximum - minimum) / 2.0)
                new_value = average_value + random.randint(-1000, +1000)
            noise_map[y][x] = new_value
            # check whether value of current position is new top or bottom
            # of range
            if new_value < bottom_of_range:
                bottom_of_range = new_value
            elif new_value > top_of_range:
                top_of_range = new_value
    # Normalises the range, making minimum = 0 and maximum = 1
    difference = float(top_of_range - bottom_of_range)
    for y in range(height):
        for x in range(width):
            noise_map[y][x] = (noise_map[y][x] - bottom_of_range) / difference
    return noise_map
