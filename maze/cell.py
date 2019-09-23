from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Cell:
    def __init__(self):
        self.up_join = False
        self.down_join = False
        self.left_join = False
        self.right_join = False

    def join(self, direction):
        if direction == Direction.UP:
            self.up_join = True
        elif direction == Direction.DOWN:
            self.down_join = True
        elif direction == Direction.LEFT:
            self.left_join = True
        elif direction == Direction.RIGHT:
            self.right_join = True
