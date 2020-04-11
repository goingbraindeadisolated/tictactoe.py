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
    while _round.ended is False:
        cell = board.click_monitor()
        board.change_cell_storage(_round.get_current_char(), cell)
        _round.victory_validation()
        _round.next_move()

    _round.end()
game.end()
