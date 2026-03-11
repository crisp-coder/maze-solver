import window
import graphics

def main():
    w = window.Window(500, 400)
    w.draw_line(graphics.Line(graphics.Point(0, 0), graphics.Point(50, 50)), "green")
    w.wait_for_close()
    return 0


if __name__ == "__main__":
    main()
