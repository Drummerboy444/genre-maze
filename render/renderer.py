from p5 import background, size, fill, ellipse

from .renderable_cell import RenderableCell


class Renderer:
    def __init__(self, maze, width, height):
        self.width = width
        self.height = height
        self.maze = maze
        self.cell_width = self.width / maze.width
        self.cell_height = self.height / maze.height

        self.rows = [[self._create_renderable_cell(cell) for cell in row] for row in maze.rows]

    def init(self):
        size(self.width, self.height)

    def render(self):
        background(100)
        self._render_maze()
        self._render_player()

    def _create_renderable_cell(self, cell):
        position = self._position_from_cell(cell)
        return RenderableCell(cell, position[0], position[1], 10)

    def _render_maze(self):
        for row in self.rows:
            for cell in row:
                cell.render()

    def _render_player(self):
        position = self._position_from_cell(self.maze.player_cell)
        fill(0, 255, 0)
        ellipse(position, 12, 12)
        fill(255, 255, 255)

    def _position_from_cell(self, cell):
        center_x = (cell.x * self.cell_width) + (self.cell_width / 2)
        center_y = (cell.y * self.cell_height) + (self.cell_height / 2)
        return center_x, center_y
