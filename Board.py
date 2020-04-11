import curses
from Cell import Cell
"""
Класс нужен для отрисовки всего что только можно на игровом поле
"""


class Board:

    def __init__(self, cols, rows):
        self.screen = curses.initscr()
        self.cols = cols
        self.rows = rows
        self.window = curses.newwin(self.rows*2+3, self.cols*5*2+2, 5, 150)
        self.grid = None
        self.height, self.width = self.get_window_hw()

    def create(self):           # Создает поле из клеток 3х3. Не рисует его
        self.grid = []
        for y in range(1, (self.rows * 2) + 1, 2):
            for x in range(2, self.cols * 4, 4):
                cell = Cell(x, y, self.window)
                self.grid.append(cell)

    def draw_edge(self):              # Рисует границы основного окна
        self.window.box("|", "-")
        self.refresh_window()

    def clear_inside(self):         # Очишает окно полсностью, затем отрисовывает его границу.
        self.window.erase()
        self.draw_edge()

    def refresh_window(self):       # Лол, кто это написа вообще.
        self.window.refresh()

    def draw_grid(self):           # Отрисовывает поле из клеток
        for i in range(len(self.grid)):
            self.grid[i].print()

    def draw_scores(self, player1, player2):        # Отрисовывает поле со счетом
        player1 = player1.name + ":" + str(player1.score)
        player2 = player2.name + ":" + str(player2.score)
        self.window.addstr(4, self.width-13, "Счёт")
        self.window.addstr(5, self.width-13, player1)
        self.window.addstr(6, self.width-13, player2)

    def draw_current_move(self, current_player):
        self.window.addstr(2, self.width-13, "Ход: ")
        self.window.addstr(3, self.width-13, current_player.name)

    def get_window_hw(self):
        height, width = self.window.getmaxyx()
        return height, width

    def clear_grid(self):              # Очищает внутренности поля из клеток.
        for i in range(len(self.grid)):
            self.grid[i].clear()
        self.refresh_window()

    def click_monitor(self):
        """
        Отслеживает нажатие на ПКМ,
        затем сравнивает координаты курсора в момент нажатия с координатами углов каждой клетки.
        Возвращает клетку.
        """
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
