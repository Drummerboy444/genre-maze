from p5 import size, background

from input import InputManager
from maze import Maze


class SketchManager:
    def __init__(self):
        self.maze = Maze(10, 10)
        self.input_manager = InputManager(self.maze)

    def setup(self):
        size(400, 400)
        self.maze.print()

    def draw(self):
        background(100)

    def key_pressed(self, key):
        self.input_manager.handle(key)
