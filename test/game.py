import unittest
import os
import sys
from faker import Faker
sys.path.append(os.path.abspath('..'))
from src.game import Game
from src.player import Player


class GameTest(unittest.TestCase):
    fake = Faker()

    def test_game_init(self):
        """ test game init"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)
        self.assertEqual(game.first_player_score.score, 0)
        self.assertEqual(game.second_player_score.score, 0)
        self.assertEqual(game.evaluate(), None)

    def test_game_first_player_win(self):
        """ test game first player win"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.first_player_win()
        game.first_player_win()
        game.first_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 0)
        self.assertEqual(game.evaluate(), None)

        game.first_player_win()
        self.assertEqual(game.evaluate(), p1)

    def test_game_second_player_win(self):
        """ test game second player win"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.second_player_win()
        game.second_player_win()
        game.second_player_win()
        self.assertEqual(game.first_player_score.score, 0)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)

        game.second_player_win()
        self.assertEqual(game.evaluate(), p2)

    def test_game_first_player_win_after_advantage(self):
        """ test game first player win after advantage"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.second_player_win()
        game.second_player_win()
        game.second_player_win()

        game.first_player_win()
        game.first_player_win()
        game.first_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)

        game.first_player_win()
        self.assertEqual(game.first_player_score.score, 4)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)

        game.first_player_win()
        self.assertEqual(game.evaluate(), p1)

    def test_game_second_player_win_after_advantage(self):
        """ test game second player win after advantage"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.second_player_win()
        game.second_player_win()
        game.second_player_win()

        game.first_player_win()
        game.first_player_win()
        game.first_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)

        game.second_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 4)
        self.assertEqual(game.evaluate(), None)

        game.second_player_win()
        self.assertEqual(game.evaluate(), p2)

    def test_game_first_player_lose_advantage(self):
        """ test game first player win after lose advantage"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.second_player_win()
        game.second_player_win()
        game.second_player_win()

        game.first_player_win()
        game.first_player_win()
        game.first_player_win()
        game.first_player_win()

        self.assertEqual(game.first_player_score.score, 4)
        self.assertEqual(game.second_player_score.score, 3)

        game.second_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)

    def test_game_second_player_lose_advantage(self):
        """ test game second player win after lose advantage"""
        p1 = Player(self.fake.first_name(), self.fake.last_name())
        p2 = Player(self.fake.first_name(), self.fake.last_name())
        game = Game(p1, p2)

        game.first_player_win()
        game.first_player_win()
        game.first_player_win()

        game.second_player_win()
        game.second_player_win()
        game.second_player_win()
        game.second_player_win()

        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 4)

        game.first_player_win()
        self.assertEqual(game.first_player_score.score, 3)
        self.assertEqual(game.second_player_score.score, 3)
        self.assertEqual(game.evaluate(), None)


if __name__ == '__main__':
    unittest.main()
