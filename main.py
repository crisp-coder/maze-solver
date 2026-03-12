import window
import graphics
import cell
import maze

def main():
    win = window.Window(500, 400, "gray")
    padding = 5
    maz = maze.Maze(padding, padding, 10, 10, 25, 25, win)
    win.wait_for_close()
    return 0


if __name__ == "__main__":
    main()
