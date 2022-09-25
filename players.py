"""
Player.py

This module will designate a class for individual players of a round.
"""


class Player:
    def __init__(self, player_id=0):
        self.player_id = player_id  # not necessary but i like having option to identify instance by int
        self.__name = self.set_name()
        self.__points = 0
        self.__total_points = 0
        self.__wins = 0
        self.__answers = {}

    def __str__(self):
        return f'{self.__name} ' \
               f'(Round Points: {self.__points}, Total Points: {self.__total_points}, Wins: {self.__wins})'

    def set_name(self):
        return input('Please choose a name: ')

    def add_pt(self, count):
        self.__points += count
        self.__total_points += count

    def add_win(self):
        self.__wins += 1

    def clear_data(self):
        self.__answers.clear()
        self.__points = 0

    def set_ans(self, final):
        self.__answers.update(final)

    def get_name(self):
        return self.__name

    def get_pts(self):
        return self.__points

    def get_total(self):
        return self.__total_points

    def get_ans(self):
        return self.__answers
