from input import InputManager
from maze import Maze
from render import Renderer


class SketchManager:
    maze_width = 20
    maze_height = 20
    render_width = 500
    render_height = 500

    def __init__(self):
        self.maze = Maze(self.maze_width, self.maze_height)
        self.renderer = Renderer(self.maze, self.render_width, self.render_height)
        self.input_manager = InputManager(self.maze)

    def setup(self):
        self.renderer.init()

    def draw(self):
        self.renderer.render()

    def key_pressed(self, key_event):
        self.input_manager.handle(key_event)
