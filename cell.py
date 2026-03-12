import graphics

class Cell:
    def __init__(self, window=None, wall_color=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

        if wall_color != None:
            self.__wall_color_present = wall_color
        else:
            self.__wall_color_present = 'blue'

        if self.__win != None:
            self.__wall_color_absent = self.__win.background
        else:
            self.__wall_color_absent = 'gray'

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        top_left = graphics.Point(x1, y1)
        bottom_left = graphics.Point(x1, y2)
        if self.has_left_wall:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_left, bottom_left), self.__wall_color_present)
        else:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_left, bottom_left), self.__wall_color_absent)

        top_right = graphics.Point(x2, y1)
        bottom_right = graphics.Point(x2, y2)
        if self.has_right_wall:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_right, bottom_right), self.__wall_color_present)
        else:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_right, bottom_right), self.__wall_color_absent)

        top_left = graphics.Point(x1, y1)
        top_right = graphics.Point(x2, y1)
        if self.has_top_wall:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_left, top_right), self.__wall_color_present)
        else:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(top_left, top_right), self.__wall_color_absent)

        bottom_left = graphics.Point(x1, y2)
        bottom_right = graphics.Point(x2, y2)
        if self.has_bottom_wall:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(bottom_left, bottom_right), self.__wall_color_present)
        else:
            if self.__win != None:
                self.__win.draw_line(graphics.Line(bottom_left, bottom_right), self.__wall_color_absent)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = self,__win.background
        else:
            color = "red"

        center_one = graphics.Point((self.__x1 + self.__x2)/2, (self.__y1 + self.__y2)/2)
        center_two = graphics.Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2)

        if self.__win != None:
            self.__win.draw_line(graphics.Line(center_one, center_two), color)







