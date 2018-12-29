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

    def test_score_multiple_increments(self):
        """ test score multiple increments"""

        score = Score()

        score.increment_score()
        score.increment_score()
        score.increment_score()
        score.increment_score()
        score.increment_score()
        self.assertEqual(score.score, 5)

        score.increment_score()
        self.assertEqual(score.score, 6)

if __name__ == '__main__':
    unittest.main()
