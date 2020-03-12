import curses
from Classes import Game, Field


# ====== Field settings ====== #
Width = 7
Height = 7
BorderChars = {
    "X": "X",
    "Y": "|"
}
Layout = """
+----+----+----+
|     |     |     |
+----+----+----+
|     |     |     |
+----+----+----+
|     |     |     |
+----+----+----+
"""
# ======================== #


def main():
    game = Game()
    mainfield = Field(10, 50, 0, 0)
    mainfield.border(BorderChars['Y'], BorderChars['X'])
    gamefield = Field(Width, Height, 3, 3)

    mainfield.window.refresh()
    mainfield.window.getch()


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(0)
screen.clear()
main()
