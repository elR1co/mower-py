from unittest import TestCase

from mower.default_mower_strategy import DefaultMowerStrategy
from mower.orientation import Orientation
from mower.position import Position


class DefaultMowerStrategyTestCase(TestCase):
    def setUp(self):
        self.mower_strategy = DefaultMowerStrategy()

    def test_should_turn_right(self):
        current_position = Position(1, 1, Orientation.NORTH)
        result = self.mower_strategy.turn_right(current_position)
        self.assertEqual(result, Position(1, 1, Orientation.EAST))

    def test_should_turn_left(self):
        current_position = Position(1, 1, Orientation.NORTH)
        result = self.mower_strategy.turn_left(current_position)
        self.assertEqual(result, Position(1, 1, Orientation.WEST))

    def test_should_move_to_north(self):
        current_position = Position(1, 1, Orientation.NORTH)
        result = self.mower_strategy.should_move(current_position)
        self.assertEqual(result, Position(1, 2, Orientation.NORTH))

    def test_should_move_to_south(self):
        current_position = Position(1, 1, Orientation.SOUTH)
        result = self.mower_strategy.should_move(current_position)
        self.assertEqual(result, Position(1, 0, Orientation.SOUTH))

    def test_should_move_to_west(self):
        current_position = Position(1, 1, Orientation.WEST)
        result = self.mower_strategy.should_move(current_position)
        self.assertEqual(result, Position(0, 1, Orientation.WEST))

    def test_should_move_to_east(self):
        current_position = Position(1, 1, Orientation.EAST)
        result = self.mower_strategy.should_move(current_position)
        self.assertEqual(result, Position(2, 1, Orientation.EAST))

    def test_should_raise_when_orientation_is_none(self):
        current_position = Position(1, 1, None)
        with self.assertRaises(ValueError):
            self.mower_strategy.should_move(current_position)
