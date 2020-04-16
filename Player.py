class Player:
    def __init__(self, name, char):
        self.name = name
        self.score = 0
        self.char = char

    def increase_score(self):
        self.score += 1

    def get_char(self):
        return self.char
