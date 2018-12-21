from .score import Score


class Game:
    """
    Game object has to handle rules of the tennis game
    and score evolution
    """

    def __init__(self, first_player, second_player):
        """
        Initialize a game
        """
        self.first_player = first_player
        self.second_player = second_player
        self.first_player_score = Score()
        self.second_player_score = Score()

    def first_player_win(self):
        if self.second_player_score.score < 4:
            self.first_player_score.increment_score()
        else:
            self.second_player_score.decrement_score()

    def second_player_win(self):
        if self.first_player_score.score < 4:
            self.second_player_score.increment_score()
        else:
            self.first_player_score.decrement_score()

    def evaluate(self):
        """
        Returns Player who won or None if the game is not completed
        """

        if self.first_player_score.score < 4 and self.second_player_score.score < 4:
            return None

        score_difference = self.first_player_score.score - self.second_player_score.score
        if score_difference >= 2:
            return self.first_player
        elif score_difference <= -2:
            return self.second_player

        return None

    def _complete_player_line(self, line, max_len):
        diff = max_len - len(line)

        if diff > 0:
            return line + (diff * " ")

        return line

    def __str__(self):
        evaluate_result = self.evaluate()
        
        if evaluate_result:
            return str(evaluate_result) + " won."

        max_len_player_name = max(
            len(str(self.first_player)),
            len(str(self.second_player))
            )

        first_player_line = str(self.first_player)
        first_player_line = self._complete_player_line(first_player_line, max_len_player_name) + \
            "\t" + str(self.first_player_score)

        second_player_line = str(self.second_player)
        second_player_line = self._complete_player_line(second_player_line, max_len_player_name) + \
            "\t" + str(self.second_player_score)

        return first_player_line + "\n" + second_player_line
