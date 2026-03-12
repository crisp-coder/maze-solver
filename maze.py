import cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, wall_color=None, win=None, seed=None):
        self.__seed = seed
        if self.__seed != None:
            random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__wall_color = wall_color
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for r in range(self.__num_rows):
            self.__cells.append([])
            for c in range(self.__num_cols):
                self.__cells[r].append(cell.Cell(self.__win, self.__wall_color))
                self.__draw_cell(r,c)

    def __draw_cell(self, row, col):
        y1 = row*self.__cell_size_y + self.__y1
        x1 = col*self.__cell_size_x + self.__x1
        y2 = (row+1)*self.__cell_size_y + self.__y1
        x2 = (col+1)*self.__cell_size_x + self.__x1
        self.__cells[row][col].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win != None:
            self.__win.redraw()

        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        self.__break_wall(0,0, 'top')
        self.__break_wall(self.__num_rows-1, self.__num_cols-1, 'bottom')

    def __break_wall(self, row, col, wall='left'):
        if wall == 'left':
            self.__cells[row][col].has_left_wall = False
        elif wall == 'right':
            self.__cells[row][col].has_right_wall = False
        elif wall == 'top':
            self.__cells[row][col].has_top_wall = False
        elif wall == 'bottom':
            self.__cells[row][col].has_bottom_wall = False

        self.__draw_cell(row, col)

    def __within_bounds(self, row, col):
        return row >= 0 and row < self.__num_rows and col >= 0 and col < self.__num_cols

    def __break_walls_r(self, row, col):
        while True:
            possible_cells = []
            if self.__within_bounds(row-1, col) and not self.__cells[row-1][col].visited:
                possible_cells.append([row-1, col, 'top'])
            if self.__within_bounds(row, col-1) and not self.__cells[row][col-1].visited:
                possible_cells.append([row, col-1, 'left'])
            if self.__within_bounds(row+1, col) and not self.__cells[row+1][col].visited:
                possible_cells.append([row+1, col, 'bottom'])
            if self.__within_bounds(row, col+1) and not self.__cells[row][col+1].visited:
                possible_cells.append([row, col+1, 'right'])
            if len(possible_cells) == 0:
                self.__draw_cell(row, col)
                return
            else:
                direction = random.randint(0, len(possible_cells)-1)
                target = possible_cells[direction]
                if target[2] == 'top':
                    self.__break_wall(target[0], target[1], 'bottom')
                    self.__break_wall(row, col, 'top')
                elif target[2] == 'right':
                    self.__break_wall(target[0], target[1], 'left')
                    self.__break_wall(row, col, 'right')
                elif target[2] == 'bottom':
                    self.__break_wall(target[0], target[1], 'top')
                    self.__break_wall(row, col, 'bottom')
                elif target[2] == 'left':
                    self.__break_wall(target[0], target[1], 'right')
                    self.__break_wall(row, col, 'left')

                self.__cells[target[0]][target[1]].visited = True
                self.__break_walls_r(target[0], target[1])



