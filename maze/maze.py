import random

from .cell import Cell
from .direction import Direction


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = [[Cell(x, y) for x in range(width)] for y in range(height)]
        self.player_position = self._get_cell(0, 0)

        self._randomise()

    def can_move(self, direction):
        return self.player_position.joined(direction)

    def move(self, direction):
        if not self.can_move(direction):
            return

        if direction == Direction.UP:
            self.player_position = self._get_cell(
                self.player_position.x,
                self.player_position.y - 1
            )
        elif direction == Direction.DOWN:
            self.player_position = self._get_cell(
                self.player_position.x,
                self.player_position.y + 1
            )
        elif direction == Direction.LEFT:
            self.player_position = self._get_cell(
                self.player_position.x - 1,
                self.player_position.y
            )
        elif direction == Direction.RIGHT:
            self.player_position = self._get_cell(
                self.player_position.x + 1,
                self.player_position.y
            )

    def print(self):
        for _ in self.rows[0]:
            print('__', end='')
        print()

        for row in self.rows:
            for cell in row:
                if cell == self.player_position:
                    print('XX', end='')
                elif cell.joined(Direction.LEFT) and not cell.joined(Direction.DOWN):
                    print('__', end='')
                elif cell.joined(Direction.LEFT) and cell.joined(Direction.DOWN):
                    print('  ', end='')
                elif not cell.joined(Direction.LEFT) and not cell.joined(Direction.DOWN):
                    print('|_', end='')
                elif not cell.joined(Direction.LEFT) and cell.joined(Direction.DOWN):
                    print('| ', end='')
            print('|', end='')
            print()

    # Uses a recursive backtracking algorithm to generate the maze, the process is:
    # 1. Choose a starting cell and set it as the current cell.
    # 2. Randomly choose a neighboring cell that has not been visited and join it to
    #    the current cell, this then becomes the new current cell.
    # 3. If all neighboring cells have been visited, back up to the last cell that has
    #    unvisited neighbors and set it as the current cell.
    # 4. Repeat step 2 until all cells have been visited.
    def _randomise(self):
        stack = []
        current_cell = self._random_cell()
        current_cell.visited = True

        while self._has_unvisited_cells():
            unvisited_neighbours = self._get_unvisited_neighbours(current_cell)
            if unvisited_neighbours:
                stack.append(current_cell)

                unvisited_neighbour = random.choice(unvisited_neighbours)
                self._join(current_cell, unvisited_neighbour)
                current_cell = unvisited_neighbour
                unvisited_neighbour.visited = True

            elif stack:
                current_cell = stack.pop()

    def _random_cell(self):
        random_row = random.choice(self.rows)
        return random.choice(random_row)

    def _has_unvisited_cells(self):
        for row in self.rows:
            for cell in row:
                if not cell.visited:
                    return True
        return False

    def _get_unvisited_neighbours(self, cell):
        neighbours = self._get_neighbours(cell)
        return [cell for cell in neighbours if not cell.visited]

    def _get_neighbours(self, cell):
        neighbours = []
        if cell.x > 0:
            neighbours.append(self._get_cell(cell.x - 1, cell.y))
        if cell.x < self.width - 1:
            neighbours.append(self._get_cell(cell.x + 1, cell.y))
        if cell.y > 0:
            neighbours.append(self._get_cell(cell.x, cell.y - 1))
        if cell.y < self.height - 1:
            neighbours.append(self._get_cell(cell.x, cell.y + 1))
        return neighbours

    def _get_cell(self, x, y):
        return self.rows[y][x]

    def _join(self, cell_1, cell_2):
        if cell_1.x < cell_2.x:
            cell_1.join(Direction.RIGHT)
            cell_2.join(Direction.LEFT)
        elif cell_1.x > cell_2.x:
            cell_1.join(Direction.LEFT)
            cell_2.join(Direction.RIGHT)
        elif cell_1.y < cell_2.y:
            cell_1.join(Direction.DOWN)
            cell_2.join(Direction.UP)
        else:
            cell_1.join(Direction.UP)
            cell_2.join(Direction.DOWN)
