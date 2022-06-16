from colours import *

import pygame
import numpy as np

SCALE = 100
HEIGHT = 300
WIDTH = 400

class Square:

    def __init__(self, coordinates, colour, camera):

        self.coordinates = coordinates
        self.colour = colour
        self.center = 0
        self.distance = 0

        self.set_center()
        self.distance = self.get_distance(camera)


    def __eq__(self, other):

        return self.distance == other.distance

    
    def __lt__(self, other):

        return self.distance < other.distance

    
    def set_center(self):

        x = get_average(self.coordinates, 0)
        y = get_average(self.coordinates, 1)
        z = get_average(self.coordinates, 2)

        self.center = np.matrix([x, y, z])


    def get_distance(self, camera):

        return np.linalg.norm(self.center - camera)


    def draw_shape(self, window):

        projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0]
        ])

        drawing_coordinates = []

        for x in self.coordinates:

            projected2d = np.dot(projection_matrix, x.reshape((3, 1)))

            coords = [int(projected2d[0][0] * SCALE) + WIDTH, int(projected2d[1][0] * SCALE) + HEIGHT]

            drawing_coordinates.append(coords)

        pygame.draw.polygon(window, self.colour, drawing_coordinates)
        pygame.draw.polygon(window, BLACK, drawing_coordinates, 5)

        """projected2d = np.dot(projection_matrix, self.center.reshape((3, 1)))
        coords = [int(projected2d[0][0] * SCALE) + WIDTH, int(projected2d[1][0] * SCALE) + HEIGHT]
        pygame.draw.circle(window, BLACK, coords, 5)"""


    
    def update(self, c, camera):

        self.coordinates = [c[self.indexes[0]], c[self.indexes[1]], c[self.indexes[2]], c[self.indexes[3]]]
        self.set_center()
        self.distance = self.get_distance(camera)


    def transform(self, transformation_matrix):

        for i in range(len(self.coordinates)):
            self.coordinates[i] = np.dot(transformation_matrix, self.coordinates[i].reshape((3, 1)))


def get_average(coords, dim):

    minimum = float(min(coords[0][(0),(dim)], coords[1][(0),(dim)], coords[2][(0),(dim)], coords[3][(0),(dim)]))
    maximum = float(max(coords[0][(0),(dim)], coords[1][(0),(dim)], coords[2][(0),(dim)], coords[3][(0),(dim)]))

    return (minimum + maximum) / 2
