from src.game import Game
from src.player import Player

from random import randint
from faker import Faker

fake = Faker()

if __name__ == '__main__':
    first_player = Player(fake.first_name(), fake.last_name())
    second_player = Player(fake.first_name(), fake.last_name())
    game = Game(first_player, second_player)
    game_status = 0

    while game_status == 0:
        if randint(1, 2) == 1:
            game.first_player_win()
        else:
            game.second_player_win()

        game_status = game.evaluate()
        print(game)
        print("----------------------------------")
