import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))
from src.score import Score


class ScoreTest(unittest.TestCase):

    def test_score_init(self):
        """ test score init"""

        score = Score()
        self.assertEqual(score.score, 0)

    def test_score_increment(self):
        """ test score incrementation"""

        score = Score()
        score.increment_score()
        self.assertEqual(score.score, 1)

    def test_score_max_increment(self):
        """ test score score maximum incrementation"""

        score = Score()

        score.increment_score()
        score.increment_score()
        score.increment_score()
        score.increment_score()
        score.increment_score()
        self.assertEqual(score.score, 5)

        self.assertRaises(Exception, score.increment_score)

    def test_score_decrement(self):
        """ test score decrementation"""

        score = Score()

        self.assertRaises(Exception, score.decrement_score)

        score.increment_score()
        score.increment_score()
        score.increment_score()
        self.assertEqual(score.score, 3)
        self.assertRaises(Exception, score.decrement_score)

        score.increment_score()
        self.assertEqual(score.score, 4)

        score.decrement_score()
        self.assertTrue(score.score, 3)

if __name__ == '__main__':
    unittest.main()
