"""
Game.py

This module will designate a class to record the data from a single game.
"""

import copy
import scattegory as scat

"""
class Session:
    def __init__(self):
        self.np = get_num_players(self)

        def get_num_players():
            num_players = int(input('How many players will there be? '))
            return num_players

    all_rounds = []

    def add_round(self, game_obj):
        self.all_rounds.append(game_obj)

    def show_full_session(self):
        return self.all_rounds
"""


class Game:
    all_cats = []

    def __init__(self, how_many_players, game_id=0):
        self.__how_many_players = how_many_players
        self.__game_id = game_id
        self.__answers = copy.deepcopy(scat.blank_dict)
        self.__cat = self.set_cat()
        self.__winners = []
        self.__round_high = 0

    def get_cat(self):
        return self.__cat

    def add_ans(self, word):
        self.__answers[scat.key(word)].append(word)

    def get_answers(self):
        return self.__answers

    def set_cat(self):  # loops until fresh category is chosen
        while True:
            new_cat = scat.get_category()
            if new_cat not in self.all_cats:
                self.__cat = new_cat
                self.all_cats.append(self.__cat)
                return self.__cat

    def compare_scores(self, all_players):  # takes list of player objects as arg
        for each in all_players:
            if each.get_pts() > self.__round_high:
                self.__winners.clear()
                self.__winners.append(each)
                self.__round_high = each.get_pts()
            elif each.get_pts() == self.__round_high:
                self.__winners.append(each)
        return self.__winners
