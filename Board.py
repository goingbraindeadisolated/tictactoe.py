import curses
import cfg
"""
Класс нужен для отрисовки всего что только можно на игровом поле
"""


class Board:

    def __init__(self):
        self.screen = curses.initscr()
        screen_height, screen_width = self.screen.getmaxyx()
        self.height = cfg.GRID_SCALE*2+3
        self.width = cfg.GRID_SCALE*5*2+2
        self.x = screen_width // 2 - self.width // 2
        self.y = screen_height // 2 - self.height // 2
        self.window = curses.newwin(self.height, self.width, self.y, self.x)

    def draw(self):              # Рисует границы основного окна
        self.window.box("|", "-")
        self.window.refresh()

    def clear(self):         # Очишает окно полсностью, затем отрисовывает его границу.
        self.window.erase()
        self.draw()



