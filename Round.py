import curses


class _Round:

    def __init__(self, game):
        self.game = game
        self.move_changing_counter = 0      # Кол-во сменов хода
        self.current_player = None
        self.ended = False
        self.start_player, self.next_player = self.set_player_move_sequence()

    def start(self):
        self.ended = False
        self.next_move()
        self.game.board.clear_grid()
        self.game.board.draw_grid()
        self.game.board.draw_scores(self.game.player1, self.game.player2)

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
        self.game.board.draw_current_move(self.current_player)

    def victory_validation(self):
        """
         Сверяет номер заполненных клеток со списком, в котором указаны все комбинации,
         при которых игра выйграна.
        """
        board = self.game.board.grid
        cell_numbers = ((0, 4, 8), (2, 4, 6), (0, 3, 6), (0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8))
        for i in cell_numbers:
            if board[i[0]].is_filled() and board[i[1]].is_filled() and board[i[2]].is_filled():
                if board[i[0]].storage == board[i[1]].storage == board[i[2]].storage == self.game.player1.char:
                    self.ended = True
                    self.game.player1.change_score()
                    self.win_msg(self.game.player1)
                elif board[i[0]].storage == board[i[1]].storage == board[i[2]].storage == self.game.player2.char:
                    self.ended = True
                    self.game.player2.change_score()
                    self.win_msg(self.game.player2)
        if board[0].is_filled() and board[1].is_filled() and board[2].is_filled() and board[3].is_filled() and \
                board[4].is_filled() and board[5].is_filled() and \
                board[6].is_filled() and board[7].is_filled() and board[8].is_filled():
            self.ended = True
            self.tie_msg()

    def end(self):
        self.game.change_round_counter()

    def get_current_char(self):
        return self.current_player.get_char()

    def win_msg(self, player):
        msg = player.name + " Выигрывает раунд"
        self.game.board.clear_inside()
        self.game.board.window.addstr(self.game.board.height // 2, self.game.board.width // 2 - len(msg) // 2, msg)
        self.game.board.refresh_window()
        curses.napms(1000)
        self.game.board.clear_inside()

    def tie_msg(self):
        msg = "Ничья"
        self.game.board.clear_inside()
        self.game.board.window.addstr(self.game.board.height // 2, self.game.board.width // 2 - len(msg) // 2, msg)
        self.game.board.refresh_window()
        curses.napms(1000)
        self.game.board.clear_inside()

