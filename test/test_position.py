import unittest

from mower.orientation import Orientation
from mower.position import Position


class PositionTestCase(unittest.TestCase):
    def setUp(self):
        self.position = Position(1, 1, Orientation.NORTH)

    def test_should_be_equal(self):
        other_position = Position(1, 1, Orientation.NORTH)
        result = self.position.__eq__(other_position)
        self.assertTrue(result)

    def test_should_not_be_equal_when_orientation_is_different(self):
        other_position = Position(1, 1, Orientation.SOUTH)
        result = self.position.__eq__(other_position)
        self.assertFalse(result)

    def test_should_not_be_equal_when_x_is_different(self):
        other_position = Position(2, 1, Orientation.NORTH)
        result = self.position.__eq__(other_position)
        self.assertFalse(result)

    def test_should_not_be_equal_when_y_is_different(self):
        other_position = Position(1, 2, Orientation.NORTH)
        result = self.position.__eq__(other_position)
        self.assertFalse(result)

    def test_should_be_same_when_is_equal(self):
        other_position = Position(1, 1, Orientation.NORTH)
        result = self.position.is_same(other_position)
        self.assertTrue(result)

    def test_should_be_same_when_orientation_is_different(self):
        other_position = Position(1, 1, Orientation.EAST)
        result = self.position.is_same(other_position)
        self.assertTrue(result)

    def test_should_not_be_same_when_x_is_different(self):
        other_position = Position(2, 1, Orientation.NORTH)
        result = self.position.is_same(other_position)
        self.assertFalse(result)

    def test_should_not_be_same_when_y_is_different(self):
        other_position = Position(1, 2, Orientation.NORTH)
        result = self.position.is_same(other_position)
        self.assertFalse(result)

    def test_should_stringify(self):
        result = self.position.__str__()
        self.assertEqual(result, "Position={x=1, y=1, orientation=NORTH}")

