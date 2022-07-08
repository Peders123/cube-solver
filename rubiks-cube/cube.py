from cubie import Cubie

class Cube:

    def __init__(self, dim):

        self.dim = dim
        self.state = []

        self.make()


    def __repr__(self):

        string = ""

        for x in self.state:
            for i in range(self.dim):
                for k in range(self.dim):
                    string += str(x[(i * 2) + k])
                string += "\n"
            string += "\n"

        return string

    
    def make(self):

        if self.dim % 2 == 1:
            lower = -(self.dim // 2)
            upper = (self.dim // 2)
        else:
            lower = -((self.dim / 2) - 0.5)
            upper = (self.dim / 2) - 0.5

        i = lower

        while i <= upper:
            layer = []
            j = lower
            while j <= upper:
                k = lower
                while k <= upper:
                    layer.append(Cubie(i, j, k))
                    k += 1
                j += 1
            self.state.append(layer)
            i += 1


    def draw_cube(self, window):

        for x in self.state:
            for y in x:
                y.draw_cubie(window)


    def rotate(self, rotation_matrix):

        for x in self.state:
            for y in x:
                y.rotate(rotation_matrix)
