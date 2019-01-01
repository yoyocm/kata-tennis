from src.game import Game
from src.opponent import Opponent

from random import randint

if __name__ == '__main__':
    first_opponent = Opponent.factory('Player')
    second_opponent = Opponent.factory('Player')
    #first_opponent = Opponent.factory('Doublet')
    #second_opponent = Opponent.factory('Doublet')
    game = Game(first_opponent, second_opponent)
    game_status = 0

    while not game_status:
        if randint(1, 2) == 1:
            game.first_player_win()
        else:
            game.second_player_win()

        game_status = game.evaluate()
        print(game)
        print("---------------------------------------------")
