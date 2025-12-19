import pygame
from colors import Colors


class Grid:
    """
    A class to represent a grid of cells
    """
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] # матриця полотна
        self.colors = Colors.get_cell_colors()

    def is_inside(self, row, column):
        """
        Check if a cell is inside
        :param row:
        :param column:
        :return:
        """
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        """
        Check if a cell is
        :param row:
        :param column:
        :return:
        """
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        """
        Check if a cell is full
        :param row:
        :return:
        """
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        """
        Clear a row of the grid without removing the cells from the grid
        :param row:
        :return:
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Move a row of the grid down by the specified number of
        :param row:
        :param num_rows:
        :return:
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Clear all rows of the
        :return:
        """
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """
        Reset the grid to its initial
        :return:
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0


    def draw(self, screen):
        """
        Draw the grid on the screen
        :param screen:
        :return:
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)