from maze import Direction


class InputManager:
    def __init__(self, maze):
        self.maze = maze

    def handle(self, key_event):
        key_name = key_event.key.name
        if not self._is_valid(key_name):
            return

        direction = self._get_direction(key_name)
        if self.maze.can_move(direction):
            self.maze.move(direction)

    def _is_valid(self, key_name):
        return key_name in {'W', 'A', 'S', 'D'}

    def _get_direction(self, key_name):
        if key_name == 'W':
            return Direction.UP
        elif key_name == 'A':
            return Direction.LEFT
        elif key_name == 'S':
            return Direction.DOWN
        elif key_name == 'D':
            return Direction.RIGHT
