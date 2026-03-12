import window
import graphics
import cell
import maze

def main():
    padding = 5
    win = window.Window(500+padding, 400+padding)
    maz = maze.Maze(padding, padding, 10, 10, 25, 25, win)
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    main()
