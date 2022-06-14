import pygame
import numpy as np
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D projection in pygame!")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

curr_pos = (400, 33)

scale = 100

circle_pos = [WIDTH/2, HEIGHT/2]  # x, y

angle = 0

points = []

# all the cube vertices
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])


projected_points = [
    [n, n] for n in range(len(points))
]


angle = 5

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

for i in range(len(points)):

        # rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        # rotated2d = np.dot(rotation_y, rotated2d)
        # rotated2d = np.dot(rotation_x, rotated2d)

    points[i] = np.dot(rotation_y, points[i].reshape((3, 1)))

    points[i] = np.dot(rotation_x, points[i].reshape((3, 1)))


def connect_points(i, j, points):
    pygame.draw.line(
        screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


for i in points:

    projected2d = np.dot(projection_matrix, i.reshape((3, 1)))

    x = int(projected2d[0][0] * scale) + circle_pos[0]
    y = int(projected2d[1][0] * scale) + circle_pos[1]

    print(x, y)



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

    # update stuff

    

    screen.fill(WHITE)
    # drawining stuff

    i = 0
    for i in range(len(points)):

        # rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        # rotated2d = np.dot(rotation_y, rotated2d)
        # rotated2d = np.dot(rotation_x, rotated2d)

        if pygame.mouse.get_pressed()[0] == True:
            """if pygame.mouse.get_pos()[0] < WIDTH // 2:
                points[i] = np.dot(rotation_y, points[i].reshape((3, 1)))
            else:
                points[i] = np.dot(n_rotation_y, points[i].reshape((3, 1)))

            if pygame.mouse.get_pos()[1] >= HEIGHT // 2:
                points[i] = np.dot(rotation_x, points[i].reshape((3, 1)))
            else:
                points[i] = np.dot(n_rotation_x, points[i].reshape((3, 1)))"""
            print(pygame.mouse.get_pos())

        else:
            points[i] = points[i].reshape((3, 1))

        curr_pos = pygame.mouse.get_pos()

        projected2d = np.dot(projection_matrix, points[i])

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, RED, (x, y), 5)
        i += 1

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    pygame.display.update()