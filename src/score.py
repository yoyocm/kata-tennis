
class Score:
    """
    Score class stores value and increment and decrement of this value
    """
    # TODO rethink score displaying
    POSSIBLE_SCORES = ["love", "fifteen", "thirty", "forty"]

    def __init__(self, score=0):
        self.score = score

    def increment_score(self):
        self.score = self.score + 1

    def __str__(self):
        if self.score > 3:
            tmp = 3
        else:
            tmp = self.score

        return self.POSSIBLE_SCORES[tmp]

    def __eq__(self, other):
        return self.score == other.score
