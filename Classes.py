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
    #TODO: сделать передачу дополнительно экрана на котором будет создаваться поле

    def __init__(self, screen, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.screen = screen
        self.window = curses.newwin(self.width, self.height, self.y, self.x)

    def border(self, symbol1, symbol2):
        self.window.box(symbol1, symbol2)
