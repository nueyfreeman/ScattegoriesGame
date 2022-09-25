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
    def __init__(self, how_many_players, game_id):
        self.how_many_players = how_many_players
        self.game_id = game_id

    winners = []  # add double underscore to distinguish as private variable (add revisit encapsulation and aggregation)
    round_high = 0
    answers = copy.deepcopy(scat.blank_dict)
    cat = ''
    result = 'Tie'

    def get_cat(self):
        return self.cat

    def get_winner(self):
        return self.winners

    def get_result(self):
        return self.result

    def get_answers(self):
        return self.answers

    def set_cat(self):
        self.cat = scat.get_category()

    def compare_scores(self, all_players):  # takes list of player objects as arg
        for each in all_players:
            if each.get_pts() > self.round_high:
                self.winners.clear()
                self.winners.append(each)
                self.round_high = each.get_pts()
                self.result = 'Win'
            elif each.get_pts() == self.round_high:
                self.winners.append(each)
                self.result = 'Tie'
        return self.winners  # change to have function return nothing and instead call show_winner()
