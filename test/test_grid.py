import unittest

from mower.grid import Grid
from mower.orientation import Orientation
from mower.position import Position


class GridTestCase(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(0, 0, 5, 5)

    def test_position_is_valid(self):
        position = Position(2, 3, Orientation.NORTH)
        result = self.grid.is_position_valid(position)
        self.assertIs(result, True)

    def test_position_is_not_valid(self):
        position = Position(6, 3, Orientation.NORTH)
        result = self.grid.is_position_valid(position)
        self.assertIs(result, False)

