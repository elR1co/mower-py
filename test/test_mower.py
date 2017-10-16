import unittest
from unittest.mock import MagicMock

from mower.mower import Mower
from mower.orientation import Orientation
from mower.position import Position


class MowerTestCase(unittest.TestCase):
    def setUp(self):
        self.mower = Mower(1, 1, Orientation.SOUTH)

    def test_move(self):
        next_position = Position(1, 7, Orientation.NORTH)
        self.mower.should_move = MagicMock(return_value=next_position)
        result = self.mower.move()
        self.mower.should_move.assert_called_once()
        self.assertEqual(result, next_position)

    def test_should_move(self):
        next_position = Position(1, 7, Orientation.NORTH)
        self.mower.mower_strategy.should_move = MagicMock(return_value=next_position)
        result = self.mower.should_move()
        self.mower.mower_strategy.should_move.assert_called_once_with(Position(1, 1, Orientation.SOUTH))
        # self.assertEquals(self.mower.mower_strategy.should_move.call_count, 1)
        self.assertEquals(result, next_position)

    def test_should_turn_right(self):
        next_position = Position(1, 7, Orientation.NORTH)
        self.mower.mower_strategy.turn_right = MagicMock(return_value=next_position)
        result = self.mower.turn_right()
        self.mower.mower_strategy.turn_right.assert_called_once_with(Position(1, 1, Orientation.SOUTH))
        self.assertEquals(result, next_position)

    def test_should_turn_left(self):
        next_position = Position(1, 7, Orientation.NORTH)
        self.mower.mower_strategy.turn_left = MagicMock(return_value=next_position)
        result = self.mower.turn_left()
        self.mower.mower_strategy.turn_left.assert_called_once_with(Position(1, 1, Orientation.SOUTH))
        self.assertEquals(result, next_position)

    def test_should_str(self):
        position_str = "my_position_str"
        self.mower.position.__str__ = MagicMock(return_value=position_str)
        result = self.mower.__str__()
        self.mower.position.__str__.assert_called_once()
        self.assertEqual(result, "Mower={position=my_position_str}")

