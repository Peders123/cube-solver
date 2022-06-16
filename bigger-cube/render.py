from colours import *
from face import *
from square import *

import pygame
import numpy as np
from math import *

pygame.display.set_caption("3D projection in pygame!")
window = pygame.display.set_mode((WIDTH*2, HEIGHT*2))

SIZE = 5

angle = 0.01

camera = np.matrix([0.5, 0.5, -20])

points = []

points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, 1, -1]))
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([-1, -1, -1]))


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

faces = []

faces.append(Face([np.matrix([1, 1, 1]), np.matrix([1, -1, 1]), np.matrix([-1, -1, 1]), np.matrix([-1, 1, 1])], RED, SIZE, camera, 0))
faces.append(Face([np.matrix([1, 1, -1]), np.matrix([1, -1, -1]), np.matrix([-1, -1, -1]), np.matrix([-1, 1, -1])], ORANGE, SIZE, camera, 0))
faces.append(Face([np.matrix([1, 1, 1]), np.matrix([1, 1, -1]), np.matrix([1, -1, -1]), np.matrix([1, -1, 1])], BLUE, SIZE, camera, 2))
faces.append(Face([np.matrix([-1, 1, 1]), np.matrix([-1, 1, -1]), np.matrix([-1, -1, -1]), np.matrix([-1, -1, 1])], GREEN, SIZE, camera, 2))
faces.append(Face([np.matrix([1, 1, 1]), np.matrix([1, 1, -1]), np.matrix([-1, 1, -1]), np.matrix([-1, 1, 1])], YELLOW, SIZE, camera, 1))
faces.append(Face([np.matrix([1, -1, 1]), np.matrix([1, -1, -1]), np.matrix([-1, -1, -1]), np.matrix([-1, -1, 1])], WHITE, SIZE, camera, 1))

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

    faces.sort()

    for f in faces:
        f.draw_face(window)

    pygame.display.update()

    if pygame.mouse.get_pressed()[0] == True:

        for f in faces:
            f.transform(rotation_x, camera)
            f.transform(rotation_y, camera)