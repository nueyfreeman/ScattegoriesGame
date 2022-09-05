"""
This module will designate a class for individual players of a round.
"""


class Player:
    def __init__(self, name, answer_history, eye_d):
        self.name = name
        self.answer_history = answer_history
        self.eye_d = eye_d

    def print_name(self):
        return self.name


