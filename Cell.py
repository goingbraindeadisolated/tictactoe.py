import curses

'''
Нужен для отрисовки клеток поля. Размеры клетки: 3х5
'''


class Cell:

    CellBorderChars = {
        "X": "-",
        "Y": "|",
        "corners": "+"
    }

    def __init__(self, x, y, window):
        window_y0, window_x0 = window.getbegyx()
        self.x = x+window_x0
        self.y = y+window_y0
        self.window = curses.newwin(3, 5, self.y, self.x)
        self.storage = None

    def print(self):
        self.window.border(self.CellBorderChars["Y"], self.CellBorderChars["Y"], self.CellBorderChars["X"],
                           self.CellBorderChars["X"], self.CellBorderChars["corners"],
                           self.CellBorderChars["corners"],
                           self.CellBorderChars["corners"], self.CellBorderChars["corners"])
        self.window.refresh()

    def fill(self, char):
        self.window.addch(1, 2, char)
        self.window.refresh()
        self.storage = char

    def is_filled(self):
        if self.storage is not None:
            return True
        else:
            return False

    def clear(self):
        self.window.delch(1, 2)
        self.window.refresh()

    def get_min_xy(self):
        return self.x, self.y
