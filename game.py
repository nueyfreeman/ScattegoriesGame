"""
Game.py

This module will designate a class to record the data from a single game.
"""

import copy
import scattegory as scat


class Game:
    def __init__(self, how_many_players, game_id):
        self.how_many_players = how_many_players
        self.game_id = game_id

    winners = []  # add double underscore to distinguish as private variable (add revisit encapsulation and aggregation)
    round_high = 0
    answers = copy.deepcopy(scat.blank_dict)
    cat = ''
    result = 'Tie'

    def show_cat(self):
        return self.cat

    def show_winner(self):
        return self.winners

    def show_result(self):
        return self.result

    def get_answers(self):
        return self.answers

    def get_cat(self):
        self.cat = scat.get_category()

    def compare_scores(self, all_players):  # takes list of player objects as arg
        for each in all_players:
            if each.points > self.round_high:
                self.winners.clear()
                self.winners.append(each)
                self.round_high = each.points
                self.result = 'Win'
            elif each.points == self.round_high:
                self.winners.append(each)
                self.result = 'Tie'
        return self.winners  # change to have function return nothing and instead call show_winner()
