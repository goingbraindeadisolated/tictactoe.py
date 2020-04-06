import curses
import cfg
import Player


class Game:

    def __init__(self, board):     # Добавить self.player1 = Player(get_player_nickname()) для двух игроков
        self.ww = 3*5*2+2
        self.wh = 3*2+3
        self.score = {"player1": 0,         # Оставить только round_counter
                      "player2": 0,
                      "round_сounter": 0}
        self.winner = None     # Player
        self.board = board

    def end(self):
        pass

    def start(self):
        curses.curs_set(0)
        curses.mousemask(1)
        self.board.draw()

    def victory_validation(self):
        if self.score["player1"] == cfg.PLAYER_SCORE_TARGET:
            self.winner = "player1"
            return True
        elif self.score["player2"] == cfg.PLAYER_SCORE_TARGET:
            self.winner = "player2"
            return True
        else:
            return False

    def get_player_nickname(self):
        message = "Введите ник игрока"
        self.window.addstr(round((self.wh/2))-1,
                           round((self.ww/2)-(len(message)/2))-1, message)
        while player1.__len__ > 10:
            self.window.clear()
            self.draw_border()
            self.window.addstr(round((self.wh / 2)) - 1,
                               round((self.ww / 2) - (len(message) / 2)) - 1, "Можно не такой длинный?")
            player1 = self.window.getstr(round(self.wh / 2),
                                         round(self.ww / 2)-4).decode()

        return player



