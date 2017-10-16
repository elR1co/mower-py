from enum import Enum, unique


@unique
class Orientation(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def left_orientation(self):
        return self._left[self]

    def right_orientation(self):
        return self._right[self]


Orientation._left = {
    Orientation.NORTH: Orientation.WEST,
    Orientation.EAST: Orientation.NORTH,
    Orientation.SOUTH: Orientation.EAST,
    Orientation.WEST: Orientation.SOUTH
}

Orientation._right = {
    Orientation.NORTH: Orientation.EAST,
    Orientation.EAST: Orientation.SOUTH,
    Orientation.SOUTH: Orientation.WEST,
    Orientation.WEST: Orientation.NORTH
}




