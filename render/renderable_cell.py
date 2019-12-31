from p5 import line

from maze import Direction


class RenderableCell:
    def __init__(self, cell, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.wall_directions = {direction for direction in Direction if not cell.joined(direction)}

    def render(self):
        if Direction.UP in self.wall_directions:
            line(
                (self.center_x - self.width / 2, self.center_y - self.height / 2),
                (self.center_x + self.width / 2, self.center_y - self.height / 2)
            )

        if Direction.DOWN in self.wall_directions:
            line(
                (self.center_x - self.width / 2, self.center_y + self.height / 2),
                (self.center_x + self.width / 2, self.center_y + self.height / 2)
            )

        if Direction.LEFT in self.wall_directions:
            line(
                (self.center_x - self.width / 2, self.center_y - self.height / 2),
                (self.center_x - self.width / 2, self.center_y + self.height / 2)
            )

        if Direction.RIGHT in self.wall_directions:
            line(
                (self.center_x + self.width / 2, self.center_y - self.height / 2),
                (self.center_x + self.width / 2, self.center_y + self.height / 2)
            )
