from src.abstract_opponent import AbstractOpponent


class Player(AbstractOpponent):
    """
    Player informations and behaviour are implemented here.
    Player inherits from AbstractOpponent
    and has to implement __str__ function
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + " " + self.last_name
