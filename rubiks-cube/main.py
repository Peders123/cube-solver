from cube import Cube
from colours import *
from math import *

import pygame
import numpy as np

SCALE = 100
HEIGHT = 300
WIDTH = 400

angle = 0.05


pygame.display.set_caption("3D projection in pygame!")
window = pygame.display.set_mode((WIDTH*2, HEIGHT*2))


rotation_z = np.matrix([
    [cos(angle), -sin(angle), 0],
    [sin(angle), cos(angle), 0],
    [0, 0, 1],
])

rotation_x = np.matrix([
    [1, 0, 0],
    [0, cos(angle), -sin(angle)],
    [0, sin(angle), cos(angle)],
])

n_rotation_x = np.matrix([
    [1, 0, 0],
    [0, cos(-angle), -sin(-angle)],
    [0, sin(-angle), cos(-angle)],
])

rotation_y = np.matrix([
    [cos(angle), 0, sin(angle)],
    [0, 1, 0],
    [-sin(angle), 0, cos(angle)],
])

n_rotation_y = np.matrix([
    [cos(-angle), 0, sin(-angle)],
    [0, 1, 0],
    [-sin(-angle), 0, cos(-angle)],
])


def main():

    cube = Cube(3)

    clock = pygame.time.Clock()

    while True:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        window.fill(WHITE)

        cube.draw_cube(window)

        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_UP]:

            cube.rotate(rotation_x)

        if pygame.key.get_pressed()[pygame.K_DOWN]:

            cube.rotate(n_rotation_x)

        if pygame.key.get_pressed()[pygame.K_LEFT]:

            cube.rotate(n_rotation_y)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:

            cube.rotate(rotation_y)


if __name__ == '__main__':
    main()
