from .score import Score


class Game:
    """
    Game object has to handle rules of the tennis game
    and score evolution
    """

    def __init__(self, first_player, second_player):
        """
        Initialize a game with two opponents and scores
        """
        self.first_player = first_player
        self.second_player = second_player
        self.first_player_score = Score()
        self.second_player_score = Score()

    def first_player_win(self):
        if self.evaluate() is not None:
            raise Exception('Game is over.')
        self.first_player_score.increment_score()

    def second_player_win(self):
        if self.evaluate() is not None:
            raise Exception('Game is over.')
        self.second_player_score.increment_score()

    def _is_deuce(self):
        return self.first_player_score.score >= 3 and self.first_player_score == self.second_player_score

    def _is_advantage(self):
        return (self.first_player_score.score > 3 or self.second_player_score.score > 3) and self.first_player_score != self.second_player_score

    def _is_over(self):
        score_difference = self.first_player_score.score - self.second_player_score.score
        return abs(score_difference) > 2 and (self.first_player_score.score > 3 or self.second_player_score.score > 3)

    def _get_leading_player(self):
        score_difference = self.first_player_score.score - self.second_player_score.score

        if score_difference > 0:
            return self.first_player
        elif score_difference < 0:
            return self.second_player

        return None

    def evaluate(self):
        """
        Returns Player who won or None if the game is not completed
        """
        score_difference = self.first_player_score.score - self.second_player_score.score

        if abs(score_difference) < 2 or (self.first_player_score.score < 4 and self.second_player_score.score < 4):
            return None

        if score_difference > 0:
            return self.first_player
        elif score_difference < 0:
            return self.second_player

        return None

    def _complete_player_line(self, line, max_len):
        diff = max_len - len(line)

        if diff > 0:
            return line + (diff * " ")

        return line

    def __str__(self):
        winner = self.evaluate()

        if winner:
            return str(winner) + " won."

        max_len_player_name = max(
            len(str(self.first_player)),
            len(str(self.second_player))
            )

        if self._is_deuce():
            first_player_score = "deuce"
            second_player_score = "....."
        elif self._is_advantage():
            advantaged_player = self._get_leading_player()
            if advantaged_player == self.first_player:
                first_player_score = "Ad"
                second_player_score = ""
            else:
                first_player_score = ""
                second_player_score = "Ad"
        else:
            first_player_score = str(self.first_player_score)
            second_player_score = str(self.second_player_score)

        first_player_line = str(self.first_player)
        first_player_line = self._complete_player_line(first_player_line, max_len_player_name) + \
            "\t" + first_player_score

        second_player_line = str(self.second_player)
        second_player_line = self._complete_player_line(second_player_line, max_len_player_name) + \
            "\t" + second_player_score

        return first_player_line + "\n" + second_player_line
