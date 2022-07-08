from colours import *

import numpy as np
import pygame

SCALE = 100
HEIGHT = 300
WIDTH = 400

class Cubie:

    def __init__(self, x, y, z):

        self.coords = np.matrix([x, y, z])

        self.x = x
        self.y = y
        self.z = z


    def __repr__(self):

        string = "[% s  % s  % s]" % (self.x, self.y, self.z)

        return string


    def draw_cubie(self, window):

        projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        projected2d = np.dot(projection_matrix, self.coords.reshape((3, 1)))

        coords = [int(projected2d[0][0] * SCALE) + WIDTH, int(projected2d[1][0] * SCALE) + HEIGHT]

        pygame.draw.circle(window, BLACK, coords, 5)


    def rotate(self, rotation_matrix):

        self.coords = np.dot(rotation_matrix, self.coords.reshape((3, 1)))
