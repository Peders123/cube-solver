class Square:

    def __init__(self, type):

        if type == 'W':
            # White
            self.type = type
        elif type == 'G':
            # Green
            self.type = type
        elif type == 'O':
            # Orange
            self.type = type
        elif type == 'B':
            # Blue
            self.type = type
        elif type == 'R':
            # Red
            self.type = type
        elif type == 'Y':
            # Yellow
            self.type = type
        else:
            # Error
            self.type = None
            print("Error creating square")
            print("Type unknown")
            print("Type: " + type)
            exit(1)

    def __str__(self):

        return self.type

    
    def __repr__(self):

        return self.type
