"""
This module will designate a class for individual players of a round.
"""


class Player:
    def __init__(self, player_id):
        self.player_id = player_id

    name = ''
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
        self.points = 0

    def add_win(self):
        self.wins += 1

