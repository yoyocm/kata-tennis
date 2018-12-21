from src.abstract_opponent import AbstractOpponent


class Doublet(AbstractOpponent):
    """
    Doublet players and behaviour is implemented here
    """

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def __str__(self):
        return str(self.first_player) + " / " + str(self.second_player)
