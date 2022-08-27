from colours import *

import numpy as np
import pygame

SCALE = 100
HEIGHT = 300
WIDTH = 400

class Cubie:

    def __init__(self, x, y, z, dim):

        self.coords = np.matrix([x, y, z])

        self.x = x
        self.y = y
        self.z = z

        self.drawing_constant = (dim - 1) * 0.5

        print(self.x, self.y, self.z)


    def __repr__(self):

        string = "[% s  % s  % s]" % (self.x, self.y, self.z)

        return string


    def draw_cubie(self, window, directions):

        projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        """projected2d = np.dot(projection_matrix, self.coords.reshape((3, 1)))

        coords = [int(projected2d[0][0] * SCALE) + WIDTH, int(projected2d[1][0] * SCALE) + HEIGHT]

        pygame.draw.circle(window, BLACK, coords, 5)"""

        vertices = []

        for x in directions:
            vertex = self.coords + (x * 0.5)
            vertex = np.dot(projection_matrix, vertex.reshape((3, 1)))
            vertex = [int(vertex[0][0] * SCALE) + WIDTH, int(vertex[1][0] * SCALE) + HEIGHT]
            vertices.append(vertex)

        if self.x == self.drawing_constant:
            pygame.draw.polygon(window, BLUE, [vertices[0], vertices[1], vertices[3], vertices[2]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[0], vertices[1], vertices[3], vertices[2]], 2)
        elif self.x == -self.drawing_constant:
            pygame.draw.polygon(window, GREEN, [vertices[4], vertices[5], vertices[7], vertices[6]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[4], vertices[5], vertices[7], vertices[6]], 2)

        if self.z == self.drawing_constant:
            pygame.draw.polygon(window, RED, [vertices[0], vertices[2], vertices[6], vertices[4]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[0], vertices[2], vertices[6], vertices[4]], 2)
        elif self.z == -self.drawing_constant:
            pygame.draw.polygon(window, ORANGE, [vertices[1], vertices[3], vertices[7], vertices[5]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[1], vertices[3], vertices[7], vertices[5]], 2)

        if self.y == self.drawing_constant:
            pygame.draw.polygon(window, WHITE, [vertices[0], vertices[1], vertices[5], vertices[4]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[0], vertices[1], vertices[5], vertices[4]], 2)
        elif self.y == -self.drawing_constant:
            pygame.draw.polygon(window, YELLOW, [vertices[2], vertices[3], vertices[7], vertices[6]], 0)
            pygame.draw.polygon(window, BLACK, [vertices[2], vertices[3], vertices[7], vertices[6]], 2)


    def rotate(self, rotation_matrix):

        self.coords = np.dot(rotation_matrix, self.coords.reshape((3, 1)))
