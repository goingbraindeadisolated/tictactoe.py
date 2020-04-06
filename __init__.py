import curses
from Game import Game
from Round import _Round
from Board import Board
'''
Основоной файл
'''
board = Board(3, 3)
board.window.keypad(1)
board.create()
game = Game(board)
game.start()
while not game.victory_validation():
    _round = _Round(game)
    _round.start()
    while not _round.victory_validation():
        cell = board.click_monitor()
        board.change_cell_storage(_round.get_current_char(), cell)
        _round.change_char()

    _round.end()
game.end()
