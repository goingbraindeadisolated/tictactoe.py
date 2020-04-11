import curses
import cfg
from Player import Player


class Game:

    def __init__(self, board):
        self.board = board
        self.player1 = None
        self.player2 = None
        self.round_counter = 0      # Счетчик раундов
        self.winner = None     # Player

    def end(self):
        msg = self.winner.name + " Победил!"
        self.board.clear_inside()
        self.board.window.addstr(self.board.height // 2, self.board.width // 2 - len(msg) // 2, msg)
        self.board.refresh_window()
        curses.napms(1000)
        self.board.window.erase()

    def start(self):
        curses.curs_set(0)
        curses.mousemask(1)
        self.board.draw_edge()
        self.player1 = Player("X", "X")             # Можно сделать ники для каждого игрока,
        self.board.clear_inside()                   # но мне кажется так сложнее понимать кто ходит и т.д.
        self.player2 = Player("O", "O")             # Я вообще изначально так и хотел, но потом передумал
        self.board.clear_inside()

    def victory_validation(self):
        """
        Тут понятно, я думаю. Если счет какого-то игрока равен определенному в конфиге кол-ву, то игра заканчивается
        """
        if self.player1.score == cfg.PLAYER_SCORE_TARGET:

            self.winner = self.player1
            return True
        elif self.player2.score == cfg.PLAYER_SCORE_TARGET:
            self.winner = self.player2
            return True
        else:
            return False

    def get_player_nickname(self):
        message = "Введите ник игрока"
        height, width = self.board.get_window_hw()
        self.board.window.addstr((height//2)-1, (width//2)-(len(message)//2)-1, message)
        player = self.board.window.getstr(height // 2, width // 2 - 4).decode()
        while len(player) > 8:
            self.board.clear_inside()
            self.board.window.addstr(height // 2 - 1, (width // 2) - (len(message) // 2) - 1, "Можно не такой длинный?")
            player = self.board.window.getstr(height // 2, width // 2-4).decode()
        return player

    def change_round_counter(self):                 # После каждого раунда увеличивает счетчик раундов на 1
        self.round_counter += 1



