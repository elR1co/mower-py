from unittest import TestCase
from unittest.mock import MagicMock

from mower.grid import Grid
from mower.instruction import Instruction
from mower.mediator import Mediator
from mower.mower import Mower
from mower.orientation import Orientation
from mower.position import Position


class MediatorTestCase(TestCase):
    def setUp(self):
        self.grid = Grid(0, 0, 5, 5)
        self.mediator = Mediator(self.grid)
        self.mower = Mower(1, 2, Orientation.NORTH)

    def test_register_should_raise_when_position_is_not_valid(self):
        self.mediator.is_position_valid = MagicMock(return_value=False)
        with self.assertRaises(ValueError):
            self.mediator.register(self.mower)

    def test_register_should_wait_once_when_position_is_locked_once(self):
        self.mediator.is_position_valid = MagicMock(return_value=True)
        self.mediator.is_position_locked = MagicMock(side_effect=[True, False])
        self.mediator.lock.wait = MagicMock(return_value=True)
        self.mediator.lock.notify_all = MagicMock(return_value=True)
        self.mediator.register(self.mower)
        self.mediator.is_position_valid.assert_called_once_with(self.mower.position)
        self.assertEqual(self.mediator.is_position_locked.call_count, 2)
        self.mediator.lock.wait.assert_called_once_with(self.mediator.DEFAULT_WAITING_TIME)
        self.mediator.lock.notify_all.assert_called_once_with()
        self.assertEqual(self.mediator.mower_list.__len__(), 1)

    def test_register_should_not_work_when_position_is_always_locked(self):
        self.mediator.is_position_valid = MagicMock(return_value=True)
        self.mediator.is_position_locked = MagicMock(return_value=True)
        self.mediator.lock.wait = MagicMock(return_value=True)
        self.mediator.lock.notify_all = MagicMock(return_value=True)
        self.mediator.register(self.mower)
        self.mediator.is_position_valid.assert_called_once_with(self.mower.position)
        self.assertEqual(self.mediator.is_position_locked.call_count, 2)
        self.assertEqual(self.mediator.lock.wait.call_count, 2)
        self.mediator.lock.notify_all.assert_called_once_with()
        self.assertEqual(self.mediator.mower_list.__len__(), 0)

    def test_register_should_not_wait_when_position_is_not_locked(self):
        self.mediator.is_position_valid = MagicMock(return_value=True)
        self.mediator.is_position_locked = MagicMock(return_value=False)
        self.mediator.lock.wait = MagicMock(return_value=True)
        self.mediator.lock.notify_all = MagicMock(return_value=True)
        self.mediator.register(self.mower)
        self.mediator.is_position_valid.assert_called_once_with(self.mower.position)
        self.mediator.is_position_locked.assert_called_once_with(self.mower.position)
        self.mediator.lock.wait.assert_not_called()
        self.mediator.lock.notify_all.assert_called_once_with()
        self.assertEqual(self.mediator.mower_list.__len__(), 1)

    def test_should_send_turn_left_instruction(self):
        expected_position = Position(1, 2, Orientation.WEST)
        self.mower.turn_left = MagicMock(return_value=expected_position)
        result = self.mediator.send_instruction(Instruction.G, self.mower)
        self.mower.turn_left.assert_called_once_with()
        self.assertEqual(result, expected_position)

    def test_should_send_turn_right_instruction(self):
        expected_position = Position(1, 2, Orientation.EAST)
        self.mower.turn_right = MagicMock(return_value=expected_position)
        result = self.mediator.send_instruction(Instruction.D, self.mower)
        self.mower.turn_right.assert_called_once_with()
        self.assertEqual(result, expected_position)

    def test_should_send_move_instruction(self):
        expected_position = Position(1, 2, Orientation.EAST)
        self.mediator.handle_move = MagicMock(return_value=expected_position)
        result = self.mediator.send_instruction(Instruction.A, self.mower)
        self.mediator.handle_move.assert_called_once_with(self.mower)
        self.assertEqual(result, expected_position)

    def test_send_instruction_should_raise_exception_when_instruction_is_unknown(self):
        with self.assertRaises(ValueError):
            self.mediator.send_instruction(None, self.mower)

    def test_position_is_locked_when_another_mower_owns_position(self):
        self.mediator.mower_list.append(self.mower)
        result = self.mediator.is_position_locked(Position(1, 2, Orientation.SOUTH))
        self.assertTrue(result)

    def test_position_is_locked_when_no_other_mower_owns_position(self):
        self.mediator.mower_list.append(self.mower)
        result = self.mediator.is_position_locked(Position(1, 3, Orientation.SOUTH))
        self.assertFalse(result)

    def test_position_is_valid_grid_check_it_is_valid(self):
        position = Position(-1, 6, Orientation.NORTH)
        self.mediator.grid.is_position_valid = MagicMock(return_value=True)
        result = self.mediator.is_position_valid(position)
        self.mediator.grid.is_position_valid.assert_called_once_with(position)
        self.assertTrue(result)

    def test_position_is_not_valid_grid_check_it_is_not_valid(self):
        position = Position(-1, 6, Orientation.NORTH)
        self.mediator.grid.is_position_valid = MagicMock(return_value=False)
        result = self.mediator.is_position_valid(position)
        self.mediator.grid.is_position_valid.assert_called_once_with(position)
        self.assertFalse(result)

    def test_should_not_move_when_position_is_not_valid(self):
        expected_next_position = Position(5, 7, Orientation.NORTH)
        self.mower.should_move = MagicMock(return_value=expected_next_position)
        self.mower.move = MagicMock(return_value=expected_next_position)
        self.mediator.is_position_valid = MagicMock(return_value=False)
        result = self.mediator.handle_move(self.mower)
        self.mower.should_move.assert_called_once_with()
        self.mediator.is_position_valid.assert_called_once_with(expected_next_position)
        self.mower.move.assert_not_called()
        self.assertEqual(result, self.mower.position)

    def test_should_wait_once_when_position_is_locked_once(self):
        expected_next_position = Position(5, 7, Orientation.NORTH)
        self.mower.should_move = MagicMock(return_value=expected_next_position)
        self.mower.move = MagicMock(return_value=expected_next_position)
        self.mediator.is_position_valid = MagicMock(return_value=True)
        self.mediator.is_position_locked = MagicMock(side_effect=[True, False])
        self.mediator.lock.wait = MagicMock(return_value=True)
        self.mediator.lock.notify_all = MagicMock(return_value=True)
        result = self.mediator.handle_move(self.mower)
        self.mower.should_move.assert_called_once_with()
        self.mower.move.assert_called_once_with()
        self.mediator.is_position_valid.assert_called_once_with(expected_next_position)
        self.assertEqual(self.mediator.is_position_locked.call_count, 2)
        self.mediator.lock.wait.assert_called_once_with(self.mediator.DEFAULT_WAITING_TIME)
        self.mediator.lock.notify_all.assert_called_once_with()
        self.assertEqual(result, expected_next_position)

    def test_should_not_move_when_position_is_always_locked(self):
        current_position = self.mower.position
        expected_next_position = Position(5, 7, Orientation.NORTH)
        self.mower.should_move = MagicMock(return_value=expected_next_position)
        self.mower.move = MagicMock(return_value=expected_next_position)
        self.mediator.is_position_valid = MagicMock(return_value=True)
        self.mediator.is_position_locked = MagicMock(return_value=True)
        self.mediator.lock.wait = MagicMock(return_value=True)
        self.mediator.lock.notify_all = MagicMock(return_value=True)
        result = self.mediator.handle_move(self.mower)
        self.mower.should_move.assert_called_once_with()
        self.mower.move.assert_not_called()
        self.mediator.is_position_valid.assert_called_once_with(expected_next_position)
        self.assertEqual(self.mediator.is_position_locked.call_count, 2)
        self.assertEqual(self.mediator.lock.wait.call_count, 2)
        self.mediator.lock.notify_all.assert_called_once_with()
        self.assertEqual(result, current_position)



