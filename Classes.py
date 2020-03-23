import curses
import cfg


class _Round:

    def __init_(self):
        self.won = False
        self.clickCounter = 0
        self.startChar, self.afterStartChar = self.set_start_char()

    def __del__(self, winner):

        Game.won = True
        if winner == "X" or winner == "x":
            Game.score["player1"] += 1

        if winner == "O" or winner == "o":
            Game.score["player2"] += 1
        Game.score["counter"] += 1

    def set_start_char(self):

        if Game.score["roundCounter"] % 2 == 0:
            start_char = "X"
            after_start_char = "O"
        else:
            start_char = "O"
            after_start_char = "X"
        return start_char, after_start_char

    def change_char(self):
        if self.clickCounter % 2 == 0:
            current_char = self.startChar
        else:
            current_char = self.afterStartChar
        return current_char


class Game:

    score = {"player1": 0, "player2": 0, "roundCounter": 0}
    won = False

    def __init__(self):
        Game.won = False
        self.window = curses.newwin(9, 50, 0, 0)
        self.draw_border()
        self. player1, self.player2 = self.get_players_nicknames()

    def get_players_nicknames(self):
        height, width = self.window.getmaxyx()
        message = "Введите ник первого игрока"
        self.window.addstr(round((height/2))-1, round((width/2)-(len(message)/2))-1, message)
        player1 = str(self.window.getstr(round((height / 2)), round((width / 2))).decode(encoding="utf-8"))
        while len(player1) > 10:
            self.window.clear()
            self.draw_border()
            player1 = self.window.addstr(round((height / 2)) - 1, round((width / 2) - (len(message) / 2)) - 1, "Можно не такой длинный?")

        self.window.clear()
        self.draw_border()
        message = "Введите ник второго игрока"
        self.window.addstr(round((height / 2)) - 1, round((width / 2) - (len(message) / 2)) - 1, message)
        player2 = str(self.window.getstr(round((height / 2)), round((width / 2))).decode(encoding="utf-8"))
        while len(player2) > 10:
            self.window.clear()
            self.draw_border()
            player2 = self.window.addstr(round((height / 2)) - 1, round((width / 2) - (len(message) / 2)) - 1, "Можно не такой длинный?")
        self.window.clear()
        self.draw_border()
        self.window.addstr(round((height / 2)) - 1, round((width / 2) - (len(message) / 2)) - 1, "Атлишна. Поехали...")
        self.window.refresh()
        curses.napms(2000)
        self.window.clear()
        self.draw_border()
        return player1, player2

    def draw_border(self):
        self.window.box(cfg.ScreenBorderChars['Y'], cfg.ScreenBorderChars['X'])
        self.window.refresh()

    def __del__(self):
        Game.won = True


class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.window = curses.newwin(3, 5, x, y)
        self.storage = " "

    def print(self):
        self.window.border(cfg.CellBorderChars["Y"], cfg.CellBorderChars["Y"], cfg.CellBorderChars["X"],
                           cfg.CellBorderChars["X"], cfg.CellBorderChars["corners"],
                           cfg.CellBorderChars["corners"],
                           cfg.CellBorderChars["corners"], cfg.CellBorderChars["corners"])
        self.window.refresh()

    def fill(self):
        self.window.addch(1, 2, self.storage)
        self.window.refresh()


class Gamefield:

    def __init__(self, width, height, x, y):    # Ширина указывается в клетках
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        this_cell = 0
        self.cells = []
        for y in range(self.y, (self.height*2)+1, 2):
            for x in range(self.x, self.width*4, 4):
                self.cells.append(Cell(y, x))
                self.cells[this_cell].print()
                this_cell += 1

# class GuiField:



