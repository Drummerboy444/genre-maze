from p5 import ellipse

from maze import Direction


class RenderableCell:
    def __init__(self, cell, center_x, center_y, size):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.wall_directions = [direction for direction in Direction if not cell.joined(direction)]

    def render(self):
        ellipse((self.center_x, self.center_y), 20, 20)
