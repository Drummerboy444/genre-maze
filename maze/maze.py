from .cell import Cell


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = [[Cell() for _ in range(width)] for _ in range(height)]
        print(self.rows)

    def get_cell(self, x, y):
        return self.rows[y][x]
