
class Score:
    """
    Score object will give value of player scores
    """

    POSSIBLE_SCORES = ["love", "fifteen", "thirty", "forty", "advantage"]

    def __init__(self, score=0):
        self.score = score

    def increment_score(self):
        self.score = self.score + 1

    def decrement_score(self):
        if self.score < 4:
            raise Exception('Score cannot be decrement if player has no \
                 advantage.')

        self.score = self.score - 1

    def __str__(self):
        return self.POSSIBLE_SCORES[self.score]
