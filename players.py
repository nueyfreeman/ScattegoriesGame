"""
Player.py

This module will designate a class for individual players of a round.
"""


class Player:
    answers = {}
    points = 0
    total_points = 0
    wins = 0

    def __init__(self, player_id):  # not necessary at this point but I like ability to distinguish obj by int
        self.player_id = player_id
        self.name = self.pick_name()  # WORKS BUT... what's going on? I use the variable while defining the variable

    def __str__(self):
        return f'{self.name} ' \
               f'(Round Points: {self.points}, Total Points: {self.total_points}, Wins: {self.wins})'

    # name = ''  # add double underscore to distinguish as private variable (add revisit encapsulation and aggregation)

    def pick_name(self):
        self.name = input('Please choose a name: ')
        return self.name

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

    def get_name(self):
        return self.name

    def get_pts(self):
        return self.points

    def get_total(self):
        return self.total_points

    def get_ans(self):
        return self.answers
