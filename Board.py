import curses
from Cell import Cell
from Round import _Round


class Board:

    def __init__(self, cols, rows):
        self.screen = curses.initscr()
        self.cols = cols
        self.rows = rows
        self.window = curses.newwin(3*2+3, 3*5*2+2, 5, 150)
        self.grid = None

    def create(self):
        self.grid = []
        for y in range(1, (3 * 2) + 1, 2):
            for x in range(2, 3 * 4, 4):
                cell = Cell(x, y, self.window)
                self.grid.append(cell)

    def draw_edge(self):
        self.window.box("|", "-")

    def refresh_window(self):
        self.window.refresh()

    def draw_grid(self):
        for i in range(len(self.grid)):
            self.grid[i].print()

    def draw_scores(self):
        pass

    def draw(self):
        self.draw_edge()
        self.refresh_window()
        self.draw_grid()
        self.draw_scores()

    def clear(self):
        for i in range(len(self.grid)):
            self.grid[i].clear()
        self.refresh_window()

    def click_monitor(self):
        while True:
            event = self.window.getch()
            if event == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                for i in range(len(self.grid)):
                    x, y = self.grid[i].get_min_xy()
                    if x < mx < x+4 and my == y+1:
                        if not self.grid[i].is_filled():
                            return self.grid[i]

    def change_cell_storage(self, char, cell):
        cell.fill(char)
