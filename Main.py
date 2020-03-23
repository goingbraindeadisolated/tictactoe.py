import curses
from Classes import Game, Gamefield, _Round


def main():

    game = Game()
    while not game.won:
        _round = _Round()
        gamefield = Gamefield(3, 3, 2, 1)
        while not _round.won:
            event = game.window.getch()
            if event == curses.KEY_MOUSE:
                _, mouse_x, mouse_y, _, _ = curses.getmouse()
                for i in gamefield.cells:
                    if mouse_x > gamefield.cells[i].x and mouse_x > (gamefield.cells[i].x + 4) \
                            and mouse_y > (gamefield.cells[i].y + 4) and mouse_y > (gamefield.cells[i].y + 2):
                        gamefield.cells[i].storage = _round.change_char()

    game.window.getch()


screen = curses.initscr()
curses.cbreak()
screen.clear()
main()
