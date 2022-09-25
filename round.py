"""
Round.py

Takes input from user to construct an alphabetical list of words, with options to view
the current list of words or to cease input. Uses a global string to keep track of which
letters haven't been used yet. Imports isolated functions from scattegory module.
"""

import copy
import scattegory as scat
import players as user
import game
ALPHA = scat.ALPHABET
ANSWERS = copy.deepcopy(scat.blank_dict)
ROUND = copy.deepcopy(scat.blank_dict)


# takes a new word from user (ALL INTERFACE OPTIONS MUST OCCUR HERE)
def get_entry(turn_alphabet):
    while True:
        word = scat.enter_word()
        if word == 'STOP':  # STOP AND VIEW must be here in the control flow or else could be accepted as answers...
            return word
        elif word == 'VIEW':  # ... therefore any other interface options (during round) must occur here as well
            return word
        else:
            if check(turn_alphabet, word):
                return word
            else:
                print('That ain\'t it chief. Try again')


# checks that the entered word starts with an acceptable letter
def check(letters_remaining, entry):
    letter = entry[0]
    if letter in letters_remaining:
        return True


# plays a round for one player (INTERFACE ACTIONS MUST TAKE PLACE HERE)
def play_round(participant, this_game):
    r_alpha = ALPHA
    round_list = []  # CAN UPDATE FUNCTION TO SAVE ANSWERS DIRECTLY TO A DICTIONARY
    while True:
        next_word = get_entry(r_alpha)
        if next_word == 'STOP':  # breaks input loop
            break
        elif next_word == 'VIEW':  # lets user see their current list and what letters remain
            scat.sort_print(round_list)
            print('You still have no entry for: ' + r_alpha)
        else:
            round_list.append(next_word)  # otherwise adds entry to list of answers this round
            this_game.answers[scat.key(next_word)].append(next_word)  # and to game answers in game object
            r_alpha = r_alpha.replace(scat.key(next_word), '_')  # updates alphabet removing letter
    scat.sort_print(round_list)
    print('You failed to come up with an answer for letters ' + r_alpha)
    print('Hope that was good enough...')
    print()
    participant.set_ans(list_to_dict(round_list))


# calculates points and finds winner from list of Player objects
def tally(all_turns, this_game):
    for player in all_turns:  # loops player instances
        for letter in ALPHA:  # loops alphabet
            choice = player.get_ans()[letter]  # takes answer for each letter in the dictionary
            if is_unique(choice, this_game):  # if it's unique adds one point
                player.add_pt(1)
        print(player.get_name() + ' got ' +
              str(player.get_pts()) + ' points this round. Their total is ' + str(player.get_total()))


# prints the winner(s) of the game by using info saved in winner directory <<<<<DOES NOT WORK>>>>>>
def final_results(all_players):  # DOES NOT WORK
    pass
    """high_score = 0
    champ = []
    for each in all_players:
        if each.total_points > high_score:
            champ.clear()
            champ.append(each)
        elif each.total_points == high_score:
            champ.append(each)
    if len(champ) == 1:
        print('Congratulations to the champion: ' + champ[0].name + '!!!')
    else:
        print('It\'s a tie!')
        print(high_score)
    """


# takes a players answer and checks it against the global answer record to see if it was unique
def is_unique(player_answer, this_game):
    if player_answer:  # returns false if empty list (no answer given)
        answers_list = this_game.get_answers()[scat.key(player_answer)]  # locates the answer list from first letter
        if answers_list.count(player_answer) == 1:  # if received answer is unique in the list
            return True


# converts the list for the round to a dictionary (SURELY CAN MAKE A BETTER ALGORITHM FOR SAVING ANSWERS)
def list_to_dict(the_list):
    new_dict = ROUND.copy()  # gets blank dictionary with {letter:empty list, etc}
    for each in the_list:  # loops answer list
        letter = scat.key(each)
        if letter in new_dict:
            new_dict[letter] = each  # assigns as value in dictionary based of first letter of each answer
    return new_dict


# takes name of all the players and creates a Player instance for them, returned in a list
def create_roster(size):
    order = []
    for i in range(size):
        print('Your turn Player ' + str(i + 1) + ': ')
        order.append(user.Player(i))  # creates a Player object and adds it to the order list
    return order


# clears necessary data from all players in a list using func from Player class
def new_game(all_players):
    for each in all_players:
        each.clear_data()


def main():
    scat.welcome()
    num_players = int(input('How many players will there be? '))
    p_order = create_roster(num_players)
    while scat.play_again():
        this_round = game.Game(num_players)
        this_round.set_cat()  # CAN I RUN THIS FUNC DURING INITIALIZATION?
        new_game(p_order)  # PERHAPS THIS FUNC SHOULD BE PART OF GAME OBJ INSTEAD?
        for i in range(num_players):  # THE TIMER WOULD BE IN THIS LOOP
            print('Remember - the category is {}. Good luck, {}!'.format(this_round.get_cat(), p_order[i].get_name()))
            play_round(p_order[i], this_round)
        tally(p_order, this_round)
        the_winners = this_round.compare_scores(p_order)
        for each in the_winners:
            print('The winner of this round was ' + each.get_name() + '.')
            each.add_win()
    final_results(p_order)


"""
IN GENERAL I FEEL LIKE THERE MUST BE A MORE SUCCINCT WAY TO END THAN WHAT I HAVE NOW
    - THREE? FUNCTIONS ADDING/CALCULATING SCORES
    - FOLLOWING ALMOST THE EXACT SAME LOGICAL FLOW TO DETERMINE THE OVERALL WINNER
"""


if __name__ == '__main__':
    main()
