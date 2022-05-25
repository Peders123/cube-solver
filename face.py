from square import Square


class Face:

    def __init__(self, type):

        self.type = type
        self.state = []

        self.create_face(type)


    def create_test(self):

        self.state = [1,2,3,8,4,7,6,5]


    def __str__(self):

        string = ""
        string += " ----- \n"
        string += "|% s % s % s|\n" % (self.state[0], self.state[1], self.state[2])
        string += "|% s % s % s|\n" % (self.state[3], self.type, self.state[4])
        string += "|% s % s % s|\n" % (self.state[5], self.state[6], self.state[7])
        string += " ----- \n"

        return string


    def create_face(self, type):

        for _ in range(8):
            self.state.append(Square(type))


    def cw_rotation(self):

        state = self.state[:]

        self.state[1] = state[0]
        self.state[2] = state[1]
        self.state[4] = state[2]
        self.state[7] = state[4]
        self.state[6] = state[7]
        self.state[5] = state[6]
        self.state[3] = state[5]
        self.state[0] = state[3]


    def acw_rotation(self):

        state = self.state[:]

        self.state[0] = state[1]
        self.state[1] = state[2]
        self.state[2] = state[4]
        self.state[4] = state[7]
        self.state[7] = state[6]
        self.state[6] = state[5]
        self.state[5] = state[3]
        self.state[3] = state[0]


s = Face('W')
s.create_test()
print(s)
s.cw_rotation()
print(s)
s.acw_rotation()
print(s)
