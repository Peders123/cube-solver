from face import Face


class Cube:

    def __init__(self):

        self.sides = [Face('W'), Face('G'), Face('O'), Face('B'), Face('R'), Face('Y')]


    def __str__(self):

        string = ""
        for i in range(5,-1,-1):
            string += self.sides[i].__str__()

        return string


print(Cube())
