"""
Player.py

This module will designate a class for individual players of a round.
"""


class Player:
    answers = {}
    points = 0
    total_points = 0
    wins = 0

    def __init__(self, player_id):  # not necessary at this point, but I like ability to distinguish obj by int
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
        """
        SOLVED
        
        self.answers.update(final) ruins score calculation (returning same score of the last player to go
        for every player...), why is that???
        
        self.answers.update(final) -- sets/resets what appears to be a class variable called by "obj.answers"
        self.answers = final -- saves "final" as an instance variable called by "obj.answers"
        
        the problem seems to be that i've done all this without knowing class variables were a thing. I didn't
        have any problems, but now I'm finding that some of the variables i've used can actually act as
        class variables by accident, even though i've intended and successfully used them as instance
        variables up to this point
        
        it turns out my problem was not only in the difference between instance variables and class variables
        but also in not having a full grasp of the difference between mutable and immutable variables
        
        class variables can only be mutable (lists, sets, dictionaries) -- you can designate a class variable
        and assign it an immutable type, but then it will still behave as an instance variable. so when I was
        confused that my class variables, which i originally had designed as instance variables, were still
        behaving as instance variables despite my mistake, it was because they were all of immutable types.
        
        except the "answer" variable which was a dictionary. so my program was working with " = final" because
        i was actually reassigning to a brand new dictionary object each time. when i changed it to ".update"
        it uncovered the mistake (which had actually been there the whole time) by actually using a class
        variable properly by mutating the same dictionary object.
        
        will now rework my classes with proper variable instrumentation and make sure im using the proper
        mutable methods for the relevant variables (which should optimize the thing i think?)
        """

    def get_ans(self):
        return self.answers
