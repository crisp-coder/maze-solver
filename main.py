from window import Window
from graphics import Point, Line
from cell import Cell
from maze import Maze
from config import Config

def main():
    config = Config()
    config.load("maze_options")
    config_map = config.getMap()
    win = Window(config_map['win_width'], config_map['win_height'], config_map['win_background'])
    maz = Maze(config_map['padding'], config_map['padding'], config_map['maze_rows'], config_map['maze_cols'], config_map['cell_size_x'], config_map['cell_size_y'], win, config_map['wall_color'])
    win.wait_for_close()

if __name__ == "__main__":
    main()
