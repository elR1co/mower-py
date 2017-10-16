from enum import Enum, unique


@unique
class Instruction(Enum):
    G = 1
    D = 2
    A = 3
