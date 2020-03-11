import curses

# class Noughts:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def print(self, screen):
#         screen.addch(self.x, self.y, "X")
#
#
# class Crosses:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def print(self, screen):
#         screen.addch(self.x, self.y, "O")
#
#
class Game:
    round = { "x" : 0, "y" : 0,"count" : 0}
    win = False
    def __init__(self):
        Game.win =  False
    def __del__(self):
        Game.win = True

class Field:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.window = curses.newwin(self.width, self.height, self.y, self.x)

    def border(self, symbol):
        self.window.box(symbol, symbol)
