from src.game import Game

from random import randint

if __name__ == '__main__':
    game = Game()
    game_status = 0

    while game_status == 0:
        if randint(1, 2) == 1:
            game.first_player_win()
        else:
            game.second_player_win()

        game_status = game.evaluate()
        print(game)
        print("----------------------------------")
