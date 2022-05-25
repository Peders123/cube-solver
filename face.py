from square import Square


class Face:

    def __init__(self, type):

        self.type = type
        self.state = []

        self.create_face(type)


    def __str__(self):

        string = ""
        string += "% s % s % s\n" % (self.state[0], self.state[1], self.state[2])
        string += "% s % s % s\n" % (self.state[3], self.type, self.state[4])
        string += "% s % s % s" % (self.state[5], self.state[6], self.state[7])

        return string


    def create_face(self, type):

        for _ in range(8):
            self.state.append(Square(type))
