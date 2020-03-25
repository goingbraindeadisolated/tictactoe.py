import curses
import cfg


class _Round:

    def __init__(self):
        self.won = False
        self.clickCounter = 0
        self.startChar, self.afterStartChar = self.set_start_char()
        self.current_char = self.startChar

    def __del__(self):

        self.won = True
        winner = self.current_char
        if winner == cfg.Cross:
            Game.score["player1"] += 1

        if winner == cfg.Nought:
            Game.score["player2"] += 1
        Game.score["roundCounter"] += 1

    def set_start_char(self):

        if Game.score["roundCounter"] % 2 == 0:
            start_char = cfg.Cross
            after_start_char = cfg.Nought
        else:
            start_char = cfg.Nought
            after_start_char = cfg.Cross
        return start_char, after_start_char

    def change_char(self):
        if self.clickCounter % 2 == 0:
            self.current_char = self.startChar
        else:
            self.current_char = self.afterStartChar
        self.clickCounter += 1


class Game:

    score = {"player1": 0, "player2": 0, "roundCounter": 0}
    won = False

    def __init__(self):
        Game.won = False
        self.window = curses.newwin(9, 35, 0, 0)
        self.draw_border()
        self. player1, self.player2 = "аa"   # self.get_players_nicknames()

    def get_players_nicknames(self):
        curses.echo()
        curses.curs_set(1)

        height, width = self.window.getmaxyx()
        message = "Введите ник первого игрока"
        self.window.addstr(round((height/2))-1, round((width/2)-(len(message)/2))-1, message)
        player1 = self.window.getstr(round(height / 2), round(width / 2)-4).decode()
        while len(player1) > 10:
            self.window.clear()
            self.draw_border()
            self.window.addstr(round((height / 2)) - 1,
                               round((width / 2) - (len(message) / 2)) - 1, "Можно не такой длинный?")
            player1 = self.window.getstr(round(height / 2),
                                         round(width / 2)-4).decode()

        self.window.clear()
        self.draw_border()
        message = "Введите ник второго игрока"
        self.window.addstr(round((height / 2)) - 1,
                           round((width / 2) - (len(message) / 2)) - 1, message)
        player2 = self.window.getstr(round(height / 2),
                                     round(width / 2)-4).decode()
        while len(player2) > 10:
            self.window.clear()
            self.draw_border()
            self.window.addstr(round((height / 2)) - 1,
                               round((width / 2) - (len(message) / 2)) - 1, "Можно не такой длинный?")
            player2 = self.window.getstr(round(height / 2),
                                         round(width / 2)-4).decode()

        curses.curs_set(0)
        self.window.clear()
        self.draw_border()
        self.window.addstr(round((height / 2)) - 1,
                           round((width / 2) - (len(message) / 2)) - 1, "Атлишна. Поехали...")
        self.window.refresh()
        curses.napms(2000)
        self.window.clear()
        self.draw_border()
        curses.noecho()
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


class Guifield:

    def __init__(self, game):
        height, width = game.window.getmaxyx()
        player1 = game.player1 + ": " + str(game.score["player1"])
        player2 = game.player2 + ": " + str(game.score["player2"])
        game.window.addstr(3, width-13, "Счёт")
        game.window.addstr(4, width-16, player1)
        game.window.addstr(5, width-16, player2)
