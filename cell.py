import graphics

class Cell:
    def __init__(self, window):
        self.__has_left_wall = True
        self.__has_right_wall = True
        self.__has_top_wall = True
        self.__has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__has_left_wall:
            top_left = graphics.Point(x1, y1)
            bottom_left = graphics.Point(x1, y2)
            self.__win.draw_line(graphics.Line(top_left, bottom_left), "green")

        if self.__has_right_wall:
            top_right = graphics.Point(x2, y1)
            bottom_right = graphics.Point(x2, y2)
            self.__win.draw_line(graphics.Line(top_right, bottom_right), "green")

        if self.__has_top_wall:
            top_left = graphics.Point(x1, y1)
            top_right = graphics.Point(x2, y1)
            self.__win.draw_line(graphics.Line(top_left, top_right), "green")

        if self.__has_bottom_wall:
            bottom_left = graphics.Point(x1, y2)
            bottom_right = graphics.Point(x2, y2)
            self.__win.draw_line(graphics.Line(bottom_left, bottom_right), "green")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"

        center_one = graphics.Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
        center_two = graphics.Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2)

        self.__win.draw_line(graphics.Line(center_one, center_two), color)
