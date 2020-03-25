import curses
from Classes import Guifield, Game, Gamefield, _Round


def main():

    game = Game()
    while not game.won:

        _round = _Round()
        gamefield = Gamefield(3, 3, 2, 1)
        guifield = Guifield(game)
        while not _round.won:
            event = screen.getch()

            if event == curses.KEY_MOUSE:
                _, mouse_x, mouse_y, _, _ = curses.getmouse()

                for i in range(len(gamefield.cells)):

                    if gamefield.cells[i].x < mouse_x < (gamefield.cells[i].x + 4) and \
                            gamefield.cells[i].y < mouse_y < (gamefield.cells[i].y + 2):
                        gamefield.cells[i].storage = _round.current_char
                        gamefield.cells[i].fill()
                        _round.change_char()


screen = curses.initscr()
curses.cbreak()
screen.clear()
curses.curs_set(0)
screen.keypad(1)
curses.mousemask(1)
main()
