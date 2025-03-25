import math
import random

class player:
    def __init__(self, letter):
        # letter is x or 0
        self.letter = letter

    # we want allplayers to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass