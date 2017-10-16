from threading import Condition

from mower.instruction import Instruction


class Mediator:

    DEFAULT_WAITING_TIME = 5

    def __init__(self, grid):
        self.grid = grid
        self.mower_list = []
        self.lock = Condition()

    def register(self, mower):
        if not self.is_position_valid(mower.position):
            raise ValueError("Mower has invalid position : " + str(mower.position))
        with self.lock:
            times = 0
            while self.is_position_locked(mower.position):
                self.lock.wait(self.DEFAULT_WAITING_TIME)
                times += 1
                if times == 2:
                    self.lock.notify_all()
                    return self
            self.mower_list.append(mower)
            self.lock.notify_all()

    def send_instruction(self, instruction, mower):
        if instruction is Instruction.G:
            return mower.turn_left()
        elif instruction is Instruction.D:
            return mower.turn_right()
        elif instruction is Instruction.A:
            return self.handle_move(mower)
        else:
            raise ValueError("Unknown Instruction : " + str(instruction))

    def handle_move(self, mower):
        potential_new_position = mower.should_move()
        if not self.is_position_valid(potential_new_position):
            return mower.position
        with self.lock:
            times = 0
            while self.is_position_locked(potential_new_position):
                self.lock.wait(self.DEFAULT_WAITING_TIME)
                times += 1
                if times == 2:
                    self.lock.notify_all()
                    return mower.position
            self.lock.notify_all()
            return mower.move()

    def is_position_locked(self, position):
        return any(elem.position.is_same(position) for elem in self.mower_list)

    def is_position_valid(self, position):
        return self.grid.is_position_valid(position)
