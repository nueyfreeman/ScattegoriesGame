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
        for every player...), why is that???
        
        self.answers.update(final) -- makes what appears to be a class variable called by "obj.answers"
        self.answers = final -- saves final as an instance variable called by "obj.answers"
        
        problem seems to be that i've done all this without knowing class variables were a thing. I didn't
        have any problems, but now I'm finding that some of the variables i've used can actually act as
        class variables by accident, even though i've intended and successfully used them as instance
        variables up to this point
        
        so I actually seem to be quite lacking in knowledge here and presently have no idea how my classes
        will behave. essentially I have been getting lucky so far by designing a program assuming that
        there is one kind of variable in a class, when actually there are multiple and I don't know how
        to tell which kind i've created or used  
        """

    def get_ans(self):
        return self.answers
