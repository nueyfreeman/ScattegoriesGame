"""
This module will designate a class for individual players of a round.
"""


class Player:
    def __init__(self, eye_d):
        self.eye_d = eye_d

    name = ''
    answers = {}
    points = 0
    total_points = 0
    wins = 0

    def pick_name(self):
        self.name = input('Please choose a name: ')

    def print_name(self):
        return self.name

    def print_eye_d(self):
        return self.eye_d

    def pts(self):
        return self.points

    def add_pt(self, count):
        self.points = self.points + count

    def calc_total(self, count):
        self.total_points = self.total_points + count

    def total(self):
        return self.total_points

    def add_win(self, count):
        self.wins = self.wins + count

    def get_score(self, outside_dict):
        for answer in self.answers:
            if answer in outside_dict:
                pass
