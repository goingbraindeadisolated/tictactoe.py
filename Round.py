import curses


class _Round:

    def __init__(self, game):
        self.game = game
        self.round_changing_counter = 0
        self.round_start_char, self.round_next_char = None, None    # TODO: Убрать
        self.current_char = None    # TODO: Убрать
        self.winner = None

    def start(self):

        self.round_changing_counter = 0
        self.round_start_char, self.round_next_char = self.set_chars()
        self.current_char = self.round_start_char

    def set_chars(self):   # TODO: Переименовать в player_move_sequence() и сделать изменение self.game.player.char в зависимости от self.game.round_counter
        """
         Исходя из значения счетчика раундов в классе Game, задает символы для четных и нечетных раундов
        """

        if self.game.score["round_сounter"] % 2 == 0:
            round_start_char = "X"
            round_next_char = "O"
        else:
            round_start_char = "O"
            round_next_char = "X"
        return round_start_char, round_next_char

    def change_char(self): # TODO: сделать изменение self.player.char
        """
        Изменяет текущий символ
        """
        self.round_changing_counter += 1
        if self.round_changing_counter % 2 == 0:
            self.current_char = self.round_start_char
        else:
            self.current_char = self.round_next_char

    def victory_validation(self):
        board = self.game.board.grid
        cell_numbers = ((0, 4, 8), (2, 4, 6), range(0, 8, 3), range(3))
        if board[0].is_filled() and board[4].is_filled() and board[8].is_filled():     # TODO: сделать изменение self.winner в зависимости от board.storage
            if board[0].storage == board[4].storage == board[8].storage:
                return True
        elif board[2].is_filled() and board[4].is_filled() and board[6].is_filled():
            if board[2].storage == board[4].storage == board[6].storage:
                return True
        for i in range(0, 8, 3):
            if board[i].is_filled() and board[i+1].is_filled() and board[i+2].is_filled():
                if board[i].storage == board[i+1].storage == board[i+2].storage:
                    return True
        for i in range(3):
            if board[i].is_filled() and board[i+3].is_filled() and board[i+6].is_filled():
                if board[i].storage == board[i+3].storage == board[i+6].storage:
                    return True
        return False

    def end(self):
        self.game.score
        message = self.player1 + ": " + str(self.score["player1"]) + "\n" + self.player2 + ": " + str(self.score["player2"])
        self.game.window.erase()
        self.game.window.addstr(round(self.game.wh/2), round(self.game.ww/2)-round(len(message/4)))
        curses.namps(1000)

    def get_current_char(self):
        return self.current_char

