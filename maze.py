import cell
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()


    def __create_cells(self):
        for r in range(self.__num_rows):
            self.__cells.append([])
            for c in range(self.__num_cols):
                self.__cells[r].append(cell.Cell(self.__win))
                self.__draw_cell(r,c)

    def __draw_cell(self, row, col):
        y1 = row*self.__cell_size_y + self.__y1
        x1 = col*self.__cell_size_x + self.__x1
        y2 = (row+1)*self.__cell_size_y + self.__y1
        x2 = (col+1)*self.__cell_size_x + self.__x1
        self.__cells[row][col].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)

