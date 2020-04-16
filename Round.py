import curses
from Grid import Grid
import cfg

class _Round:

    def __init__(self, game):
        self.game = game
        self.move_changing_counter = 0      # Кол-во сменов хода
        self.current_player = None
        self.ended = False
        self.grid = Grid(2, 1, cfg.GRID_SCALE)
        self.start_player, self.next_player = self.set_player_move_sequence()

    def set_player_move_sequence(self):
        """
        Вызывается в начале каждого раунда
        и устанавливает последовательность ходов в зависимости от количества сыгранных раундов.
        """

        if self.game.round_counter % 2 == 0:
            start_player = self.game.player1
            next_player = self.game.player2
        else:
            start_player = self.game.player2
            next_player = self.game.player1
        return start_player, next_player

    def next_move(self):
        if self.move_changing_counter % 2 == 0:
            self.current_player = self.start_player
        else:
            self.current_player = self.next_player
        self.move_changing_counter += 1
        self.draw_current_move()

    def draw_scores(self, player1, player2):        # Отрисовывает поле со счетом
        msg = player1.name + ":" + str(player1.score) + " " + player2.name + ":" + str(player2.score)
        self.game.board.window.addstr(4, self.game.board.width*3//4-len(msg)//2, msg)
        self.game.board.window.refresh()

    def draw_current_move(self):
        msg = "Ход: " + self.current_player.name
        self.game.board.window.addstr(2, 3*self.game.board.width//4-len(msg)//2, msg)
        self.game.board.window.refresh()

    def end_validation(self):
        board = self.grid.cells         # TODO: Нихуя не работает, хоть и отслеживает
        # Проверка по горизонтали
        for _ in range(cfg.GRID_SCALE):
            self.ended = all(board[_][__].is_filled() is True for __ in range(cfg.GRID_SCALE)) and\
                         any(board[_][__] == board[_][0] for __ in range(cfg.GRID_SCALE))
            if self.ended:
                self.current_player.increase_score()
                self.win_msg(self.current_player)
                return
        # Проверка по вертикали
        for _ in range(cfg.GRID_SCALE):
            self.ended = all(board[__][_].is_filled() is True for __ in range(cfg.GRID_SCALE)) and\
                         any(board[__][_] == board[0][_] for __ in range(cfg.GRID_SCALE))
            if self.ended:
                self.current_player.increase_score()
                self.win_msg(self.current_player)
                return
        # Проверка по диагонали от левого верхнего угла
        self.ended = all(board[_][_].is_filled() is True for _ in range(cfg.GRID_SCALE)) and\
                     all(board[_][_] == board[0][0] for _ in range(cfg.GRID_SCALE))
        if self.ended:
            self.current_player.increase_score()
            self.win_msg(self.current_player)
            return
        # Проверка по диагонали от правого верхнего угла
        self.ended = all(board[_][-1 - _].is_filled() is True for _ in range(cfg.GRID_SCALE)) and\
                     all(board[_][-1 - _] == board[0][-1] for _ in range(cfg.GRID_SCALE))
        if self.ended:
            self.current_player.increase_score()
            self.win_msg(self.current_player)
            return

    def click_monitoring(self):
        while True:
            event = self.game.board.window.getch()
            if event == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                for i in range(len(self.grid.cells)):
                    x, y = self.grid.cells[i][0].get_min_xy()
                    if y < my < y+2:
                        for j in range(len(self.grid.cells[i])):
                            x, y = self.grid.cells[i][j].get_min_xy()
                            if x < mx < x+4:
                                if not self.grid.cells[i][j].is_filled():
                                    self.grid.cells[i][j].fill(self.current_player.char)
                                    return

    def get_current_char(self):
        return self.current_player.get_char()

    def win_msg(self, player):
        msg = player.name + " Выигрывает раунд"
        self.game.board.clear()
        self.game.board.window.addstr(self.game.board.height // 2, self.game.board.width // 2 - len(msg) // 2, msg)
        self.game.board.window.refresh()
        curses.napms(1000)
        self.game.board.clear()

    def tie_msg(self):
        msg = "Ничья"
        self.game.board.clear()
        self.game.board.window.addstr(self.game.board.height // 2, self.game.board.width // 2 - len(msg) // 2, msg)
        self.game.board.window.refresh()
        curses.napms(1000)
        self.game.board.clear()

