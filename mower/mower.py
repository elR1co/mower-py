from mower.default_mower_strategy import DefaultMowerStrategy
from mower.position import Position


class Mower:
    def __init__(self, x, y, orientation):
        self.position = Position(x, y, orientation)
        self.mower_strategy = DefaultMowerStrategy()

    def __str__(self):
        return "Mower={" + \
                "position=" + self.position.__str__() + \
                "}"

    def should_move(self):
        return self.mower_strategy.should_move(self.position)

    def move(self):
        self.position = self.should_move()
        return self.position

    def turn_right(self):
        self.position = self.mower_strategy.turn_right(self.position)
        return self.position

    def turn_left(self):
        self.position = self.mower_strategy.turn_left(self.position)
        return self.position
