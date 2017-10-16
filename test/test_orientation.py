import unittest

from mower.orientation import Orientation


class OrientationTestCase(unittest.TestCase):

    def test_north_should_have_west_as_left_orientation(self):
        orientation = Orientation.NORTH
        result = orientation.left_orientation()
        self.assertEqual(result, Orientation.WEST)

    def test_north_should_have_east_as_right_orientation(self):
        orientation = Orientation.NORTH
        result = orientation.right_orientation()
        self.assertEqual(result, Orientation.EAST)

    def test_south_should_have_east_as_left_orientation(self):
        orientation = Orientation.SOUTH
        result = orientation.left_orientation()
        self.assertEqual(result, Orientation.EAST)

    def test_south_should_have_west_as_right_orientation(self):
        orientation = Orientation.SOUTH
        result = orientation.right_orientation()
        self.assertEqual(result, Orientation.WEST)

    def test_east_should_have_north_as_left_orientation(self):
        orientation = Orientation.EAST
        result = orientation.left_orientation()
        self.assertEqual(result, Orientation.NORTH)

    def test_east_should_have_south_as_right_orientation(self):
        orientation = Orientation.EAST
        result = orientation.right_orientation()
        self.assertEqual(result, Orientation.SOUTH)

    def test_west_should_have_south_as_left_orientation(self):
        orientation = Orientation.WEST
        result = orientation.left_orientation()
        self.assertEqual(result, Orientation.SOUTH)

    def test_west_should_have_north_as_right_orientation(self):
        orientation = Orientation.WEST
        result = orientation.right_orientation()
        self.assertEqual(result, Orientation.NORTH)
