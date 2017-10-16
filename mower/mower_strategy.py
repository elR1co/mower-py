from abc import ABC, abstractmethod


class MowerStrategy(ABC):

    @abstractmethod
    def should_move(self, current_position):
        pass

    @abstractmethod
    def turn_right(self, current_position):
        pass

    @abstractmethod
    def turn_left(self, current_position):
        pass
