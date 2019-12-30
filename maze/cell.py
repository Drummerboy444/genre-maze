from .direction import Direction


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

        self.joined_up = False
        self.joined_down = False
        self.joined_left = False
        self.joined_right = False

    def join(self, direction):
        if direction == Direction.UP:
            self.joined_up = True
        elif direction == Direction.DOWN:
            self.joined_down = True
        elif direction == Direction.LEFT:
            self.joined_left = True
        elif direction == Direction.RIGHT:
            self.joined_right = True

    def joined(self, direction):
        if direction == Direction.UP:
            return self.joined_up
        elif direction == Direction.DOWN:
            return self.joined_down
        elif direction == Direction.LEFT:
            return self.joined_left
        elif direction == Direction.RIGHT:
            return self.joined_right
