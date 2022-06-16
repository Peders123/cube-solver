from colours import *
from square import *

import numpy as np

class Face:

    def __init__(self, coordinates, colour, size, camera):

        self.coordinates = coordinates
        self.colour = colour
        self.size = size
        self.center = self.get_center()
        self.distance = self.get_distance(camera)
        self.squares = []
        self.make_squares()


    def __eq__(self, other):

        return self.distance == other.distance

    
    def __lt__(self, other):

        return self.distance < other.distance


    def get_center(self):

        x = get_average(self.coordinates, 0)
        y = get_average(self.coordinates, 1)
        z = get_average(self.coordinates, 2)

        return np.matrix([x, y, z])

    
    def get_distance(self, camera):

        return np.linalg.norm(self.center - camera)

    
    def make_squares(self):

        # self.squares.append(Square(self.coordinates, RED, np.matrix([0.5, 0.5, -10])))

        print(self.coordinates)

        base_x = float(self.coordinates[0][(0),(0)])
        base_y = float(self.coordinates[0][(0),(1)])
        base_z = float(self.coordinates[0][(0),(2)])

        x = float(self.coordinates[1][(0),(0)] + self.coordinates[0][(0),(0)]) / self.size
        y = float(self.coordinates[3][(0),(1)] + self.coordinates[0][(0),(1)]) / self.size

        print(x)

        for i in range(self.size):
            for j in range(self.size):
                coords = [
                    np.matrix([base_x - (x * j), base_y - (y * i), base_z]),
                    np.matrix([base_x - (x * (j+1)), base_y - (y * i), base_z]),
                    np.matrix([base_x - (x * (j+1)), base_y - (y * (i+1)), base_z]),
                    np.matrix([base_x - (x * j), base_y - (y * (i+1)), base_z])
                ]

                self.squares.append(Square(coords, self.colour, np.matrix([0.5, 0.5, -10])))


    def draw_face(self, window):

        for s in self.squares:
            s.draw_shape(window)


    def transform(self, transformation_matrix, camera):

        self.center = np.dot(transformation_matrix, self.center.reshape((3, 1)))
        self.distance = self.get_distance(camera)
        
        for s in self.squares:
            s.transform(transformation_matrix)


def get_average(coords, dim):

    minimum = float(min(coords[0][(0),(dim)], coords[1][(0),(dim)], coords[2][(0),(dim)], coords[3][(0),(dim)]))
    maximum = float(max(coords[0][(0),(dim)], coords[1][(0),(dim)], coords[2][(0),(dim)], coords[3][(0),(dim)]))

    return (minimum + maximum) / 2
