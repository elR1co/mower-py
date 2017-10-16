from mower.mower_strategy import MowerStrategy
from mower.orientation import Orientation
from mower.position import Position


class DefaultMowerStrategy(MowerStrategy):

    def turn_right(self, current_position):
        return Position(current_position.x, current_position.y, current_position.orientation.right_orientation())

    def turn_left(self, current_position):
        return Position(current_position.x, current_position.y, current_position.orientation.left_orientation())

    def should_move(self, current_position):
        orientation = current_position.orientation
        if orientation is Orientation.NORTH:
            return Position(current_position.x, current_position.y + 1, orientation)
        elif orientation is Orientation.SOUTH:
            return Position(current_position.x, current_position.y - 1, orientation)
        elif orientation is Orientation.EAST:
            return Position(current_position.x + 1, current_position.y, orientation)
        elif orientation is Orientation.WEST:
            return Position(current_position.x - 1, current_position.y, orientation)
        else:
            raise ValueError("Orientation unknown %s", orientation)
