import logging
import unittest

import time
from random import randrange
from threading import Thread


from mower.grid import Grid
from mower.instruction import Instruction
from mower.mediator import Mediator
from mower.mower import Mower
from mower.orientation import Orientation
from mower.position import Position


class ConcurrentMainTestCase(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,
                        format='(%(threadName)-6s) %(message)s')

    def test_concurrent_main(self):
        # Given
        grid = Grid(0, 0, 5, 5)
        mower1 = Mower(1, 2, Orientation.NORTH)
        mower2 = Mower(3, 3, Orientation.EAST)
        mediator = Mediator(grid)

        def to_instruction(string):
            return Instruction[string]

        mower1_instructions = map(to_instruction, list("GAGAGAGAA"))
        mower2_instructions = map(to_instruction, list("AADAADADDA"))

        # When
        thread1 = Thread(name="mower1", target=self.thread_mower, args=(mediator, mower1_instructions, mower1))
        thread2 = Thread(name="mower2", target=self.thread_mower, args=(mediator, mower2_instructions, mower2))

        thread1.start()
        thread2.start()

        thread1.join(30)
        thread2.join(30)

        # Then
        self.assertEqual(mower1.position, Position(1, 3, Orientation.NORTH))
        self.assertEqual(mower2.position, Position(5, 1, Orientation.EAST))

    @staticmethod
    def thread_mower(mediator, mower_instructions, mower):
        logging.info("Starting")
        time.sleep(randrange(2))
        mediator.register(mower)
        for instruction in mower_instructions:
            time.sleep(randrange(2))
            mediator.send_instruction(instruction, mower)
        logging.info("Exiting")
