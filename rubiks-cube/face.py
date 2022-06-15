from square import Square


class Face:

    def __init__(self, type):

        self.type = type
        self.state = []

        self.create_face(type)


    def create_test(self):

        self.state = [1,2,4,3]


    def __str__(self):

        string = ""
        string += " --- \n"
        string += "|% s % s|\n" % (self.state[0], self.state[1])
        string += "|% s % s|\n" % (self.state[2], self.state[3])
        string += " --- \n"

        return string


    def create_face(self, type):

        for _ in range(4):
            self.state.append(Square(type))

    def rotate(self, prime=False):

        if not prime:
            self.state[0], self.state[1], self.state[2], self.state[3] = \
                self.state[2], self.state[0], self.state[3], self.state[1]
        else:
            self.state[0], self.state[1], self.state[2], self.state[3] = \
                self.state[1], self.state[3], self.state[0], self.state[2]
