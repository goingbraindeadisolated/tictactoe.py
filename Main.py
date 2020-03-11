import curses
from Classes import Game, Field


# ====== Field settings ====== #
Width = 7
Height = 7
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
    mainfield = Field(15, 15, 1, 1)
    # gamefield = Field(Width, Height, 3, 3)                       # Создаем игровое поле                    # Игровой цикл
    mainfield.window.box('#', "#")

    screen. refresh()
    screen.getch()


screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(0)
screen.clear()
main()
