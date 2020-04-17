from Game import Game
from Round import _Round
from Board import Board
import cfg
from Player import Player
import curses
'''
Основоной файл
'''
if cfg.GRID_SCALE > 2:
    board = Board()
    board.window.keypad(1)
    board.draw()
    game = Game(board)
    curses.curs_set(0)
    curses.mousemask(1)

    while not game.victory_validation():
        _round = _Round(game)
        _round.grid.create(board.window)
        _round.grid.print()
        _round.draw_scores(game.player1, game.player2)
        _round.next_move()
        while _round.ended is False:
            _round.click_monitoring()
            _round.end_validation()
            _round.next_move()
        game.change_round_counter()
    game.end_msg()
else:
    print("Значение cfg.GRID_SCALE должно быть больше 2")