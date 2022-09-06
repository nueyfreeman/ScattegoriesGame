"""
This module will designate a class to record the data from a single game.
"""

import copy
import scattegory as scat


class Game:
    def __init__(self, how_many_players, game_id):
        self.how_many_players = how_many_players
        self.game_id = game_id

    winner = ''
    answers = copy.deepcopy(scat.blank_dict)
    cat = ''
    result = 'Tie'

    def get_cat(self):
        self.cat = scat.get_category()

    def compare_scores(self):
        pass
