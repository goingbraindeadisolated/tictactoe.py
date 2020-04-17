from Cell import Cell


class Grid:

    def __init__(self, x, y, scale):
        self.scale = scale
        self.cells = []
        self.x = x
        self.y = y

    def create(self, window):
        self.cells = [[Cell(x*4+self.x, y*2+self.y, window) for x in range(self.scale)] for y in range(self.scale)]

    def print(self):
        for y in range(self.scale):
            for x in range(self.scale):
                self.cells[y][x].print()

    def change_cell_storage(self, y, x, storage):
        self.cells[y][x].fill(storage)