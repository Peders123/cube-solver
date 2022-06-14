from face import Face


class Cube:

    def __init__(self):

        self.sides = [Face('W'), Face('G'), Face('O'), Face('B'), Face('R'), Face('Y')]


    def __str__(self):

        string = ""
        string += "     --- \n"
        string += "    |%s %s|\n" % (self.sides[5].state[0], self.sides[5].state[1])
        string += "    |%s %s|\n" % (self.sides[5].state[2], self.sides[5].state[3])
        string += " --- --- --- --- \n"
        string += "|%s %s|%s %s|%s %s|%s %s|\n" % (self.sides[1].state[0], self.sides[1].state[1], \
            self.sides[2].state[0], self.sides[2].state[1], \
            self.sides[3].state[0], self.sides[3].state[1], \
            self.sides[4].state[0], self.sides[4].state[1])
        string += "|%s %s|%s %s|%s %s|%s %s|\n" % (self.sides[1].state[2], self.sides[1].state[3], \
            self.sides[2].state[2], self.sides[2].state[3], \
            self.sides[3].state[2], self.sides[3].state[3], \
            self.sides[4].state[2], self.sides[4].state[3])
        string += " --- --- --- --- \n"
        string += "    |%s %s|\n" % (self.sides[0].state[0], self.sides[0].state[1])
        string += "    |%s %s|\n" % (self.sides[0].state[2], self.sides[0].state[3])
        string += "     --- "
        

        return string

    
    def up(self, prime=False):

        if not prime:
            self.sides[5].rotate()
            self.sides[1].state[0], self.sides[2].state[0], self.sides[3].state[0], self.sides[4].state[0] = \
                self.sides[2].state[0], self.sides[3].state[0], self.sides[4].state[0], self.sides[1].state[0]
            self.sides[1].state[1], self.sides[2].state[1], self.sides[3].state[1], self.sides[4].state[1] = \
                self.sides[2].state[1], self.sides[3].state[1], self.sides[4].state[1], self.sides[1].state[1]
        else:
            self.sides[5].rotate(True)
            self.sides[1].state[0], self.sides[2].state[0], self.sides[3].state[0], self.sides[4].state[0] = \
                self.sides[4].state[0], self.sides[1].state[0], self.sides[2].state[0], self.sides[3].state[0]
            self.sides[1].state[1], self.sides[2].state[1], self.sides[3].state[1], self.sides[4].state[1] = \
                self.sides[4].state[1], self.sides[1].state[1], self.sides[2].state[1], self.sides[3].state[1]


    def down(self, prime=False):

        if not prime:
            self.sides[0].rotate()
            self.sides[1].state[2], self.sides[2].state[2], self.sides[3].state[2], self.sides[4].state[2] = \
                 self.sides[4].state[2], self.sides[1].state[2], self.sides[2].state[2], self.sides[3].state[2]
            self.sides[1].state[3], self.sides[2].state[3], self.sides[3].state[3], self.sides[4].state[3] = \
                 self.sides[4].state[3], self.sides[1].state[3], self.sides[2].state[3], self.sides[3].state[3]
        else:
            self.sides[0].rotate(True)
            self.sides[1].state[2], self.sides[2].state[2], self.sides[3].state[2], self.sides[4].state[2] = \
                self.sides[2].state[2], self.sides[3].state[2], self.sides[4].state[2], self.sides[1].state[2]
            self.sides[1].state[3], self.sides[2].state[3], self.sides[3].state[3], self.sides[4].state[3] = \
                self.sides[2].state[3], self.sides[3].state[3], self.sides[4].state[3], self.sides[1].state[3]


    def right(self, prime=False):

        pass



c = Cube()
print(c)
c.down()
print(c)
c.down(True)
print(c)
