class Position:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "Position={" + \
                "x=" + str(self.x) + ", " + \
                "y=" + str(self.y) + ", " + \
                "orientation=" + self.orientation.name + "}"

    def is_same(self, position):
        return self.x == position.x and self.y == position.y