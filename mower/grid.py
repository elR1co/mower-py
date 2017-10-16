class Grid:
    def __init__(self, x_min, y_min, x_max, y_max):
        assert x_max > x_min
        assert y_max > y_min
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def is_position_valid(self, position):
        return self.x_min <= position.x <= self.x_max and self.y_min <= position.y <= self.y_max
