import unittest

from mower.grid import Grid
from mower.instruction import Instruction
from mower.mediator import Mediator
from mower.mower import Mower
from mower.orientation import Orientation
from mower.position import Position


class SequentialMainTestCase(unittest.TestCase):

    def test_sequential_main(self):
        # Given
        grid = Grid(0, 0, 5, 5)
        mower1 = Mower(1, 2, Orientation.NORTH)
        mower2 = Mower(3, 3, Orientation.EAST)
        mediator = Mediator(grid)
        mediator.register(mower1)
        mediator.register(mower2)

        def to_instruction(string):
            return Instruction[string]

        mower1_instructions = map(to_instruction, list("GAGAGAGAA"))
        mower2_instructions = map(to_instruction, list("AADAADADDA"))

        # When
        for instruction1 in mower1_instructions:
            mediator.send_instruction(instruction1, mower1)
        for instruction2 in mower2_instructions:
            mediator.send_instruction(instruction2, mower2)

        # Then
        self.assertEqual(mower1.position, Position(1, 3, Orientation.NORTH))
        self.assertEqual(mower2.position, Position(5, 1, Orientation.EAST))
