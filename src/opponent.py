from src.player import Player
from src.doublet import Doublet
from faker import Faker


class Opponent:
    """
    Opponent class allows to create Player or Doublet
    with the Factory design pattern
    """

    def factory(type):
        fake = Faker()

        if type == "Player":
            return Player(fake.first_name(), fake.last_name())

        if type == "Doublet":
            p1 = Player(fake.first_name(), fake.last_name())
            p2 = Player(fake.first_name(), fake.last_name())
            return Doublet(p1, p2)

        assert 0, "Bad opponent creation: " + type
