from face import *
from colours import *

import pygame
import numpy as np
from math import *

pygame.display.set_caption("3D projection in pygame!")
window = pygame.display.set_mode((WIDTH*2, HEIGHT*2))

angle = 0.05

camera = np.matrix([0.5, 0.5, -10])

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

faces.append(Face([0, 2, 6, 4], points, RED, camera))
faces.append(Face([0, 1, 3, 2], points, BLUE, camera))
faces.append(Face([1, 3, 7, 5], points, ORANGE, camera))
faces.append(Face([4, 5, 7, 6], points, GREEN, camera))
faces.append(Face([0, 1, 5, 4], points, YELLOW, camera))
faces.append(Face([2, 3, 7, 6], points, WHITE, camera))


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
        f.draw_shape(window)

    pygame.display.update()

    if pygame.key.get_pressed()[pygame.K_UP]:
        for i in range(len(points)):
            points[i] = np.dot(rotation_x, points[i].reshape((3, 1)))

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        for i in range(len(points)):
            points[i] = np.dot(n_rotation_x, points[i].reshape((3, 1)))
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        for i in range(len(points)):
            points[i] = np.dot(n_rotation_y, points[i].reshape((3, 1)))

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        for i in range(len(points)):
            points[i] = np.dot(rotation_y, points[i].reshape((3, 1)))

    for i in range(len(points)):
        points[i] = points[i].reshape((1, 3))

    for f in faces:
            f.update(points, camera)
