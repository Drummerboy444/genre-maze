import random

from .cell import Cell
from .direction import Direction


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = [[Cell(x, y) for x in range(width)] for y in range(height)]

        self._randomize()

    def print(self):
        for _ in self.rows[0]:
            print('__', end='')
        print()

        for row in self.rows:
            for cell in row:
                if cell.joined_left and not cell.joined_down:
                    print('__', end='')
                elif cell.joined_left and cell.joined_down:
                    print('  ', end='')
                elif not cell.joined_left and not cell.joined_down:
                    print('|_', end='')
                elif not cell.joined_left and cell.joined_down:
                    print('| ', end='')
            print('|', end='')
            print()

    def _randomize(self):
        stack = []

        # Make the initial cell the current cell and mark it as visited
        current_cell = self._random_cell()
        current_cell.visited = True

        # While there are unvisited cells:
        while self._has_unvisited_cells():

            # If the current cell has any neighbours which have not been visited
            unvisited_neighbours = self._get_unvisited_neighbours(current_cell)
            if unvisited_neighbours:

                # Choose randomly one of the unvisited neighbours
                unvisited_neighbour = random.choice(unvisited_neighbours)

                # Push the current cell to the stack if it has more than one unvisited neighbor
                if len(unvisited_neighbours) > 1:
                    stack.append(current_cell)

                # Remove the wall between the current cell and the chosen cell
                self._join(current_cell, unvisited_neighbour)

                # Make the chosen cell the current cell and mark it as visited
                current_cell = unvisited_neighbour
                unvisited_neighbour.visited = True

            # Else if stack is not empty
            elif stack:
                # pop a cell from the stack and make it the current cell
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
        neighbours = []
        if cell.x > 0:
            neighbours.append(self._get_cell(cell.x - 1, cell.y))
        if cell.x < self.width - 1:
            neighbours.append(self._get_cell(cell.x + 1, cell.y))
        if cell.y > 0:
            neighbours.append(self._get_cell(cell.x, cell.y - 1))
        if cell.y < self.height - 1:
            neighbours.append(self._get_cell(cell.x, cell.y + 1))

        return [cell for cell in neighbours if not cell.visited]

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
