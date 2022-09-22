"""
Player.py

This module will designate a class for individual players of a round.
"""


class Player:
    def __init__(self, player_id):  # not necessary at this point but I like ability to distinguish obj by int
        self.player_id = player_id

    name = ''  # add double underscore to distinguish as private variable (add revisit encapsulation and aggregation)
    answers = {}
    points = 0
    total_points = 0
    wins = 0

    def pick_name(self):
        self.name = input('Please choose a name: ')

    def add_pt(self, count):
        self.points += count

    def calc_total(self):
        self.total_points += self.points
        # self.points = 0    WHERE IN THE PROGRAM FLOW IS BEST PLACE TO CLEAR POINTS???

    def add_win(self):
        self.wins += 1

    def clear_data(self):
        self.answers.clear()
        self.points = 0

    def set_ans(self, final):
        self.answers = final
        """
        self.answers.update(final) ruins score calculation (returning same score of the last player to go
        for every player...), but it appears not to have messed up the actual dictionary variable "answers,"
        why is that???
        """

    def get_ans(self):
        return self.answers
