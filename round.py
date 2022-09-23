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


# takes a new word from user while tracking letters remaining
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


# plays a round for one player
def play_round(participant, this_game):
    round_alphabet = ALPHA  # better as part of player obj??? if reusing player obj no, I think. but if not, yes?
    round_list = []  # could also be a variable in player object --> EVENTUALLY SAVING THE DATA THERE ANYWAY...
    while True:
        next_word = get_entry(round_alphabet)
        if next_word == 'STOP':  # breaks input loop
            print('Okay no more')
            break
        elif next_word == 'VIEW':  # lets user see their current list and what letters remain
            scat.sort_print(round_list)
            print('You still have no entry for: ' + round_alphabet)
        else:  # otherwise adds entry to list of answers this round
            round_list.append(next_word)
            this_game.answers[scat.to_key(next_word)].append(next_word)  # and to game answers in game object
            round_alphabet = round_alphabet.replace(scat.to_key(next_word), '_')  # updates alphabet removing letter
    scat.sort_print(round_list)
    print('You failed to come up with an answer for letters ' + round_alphabet)
    print('Hope that was good enough...')
    print()
    participant.set_ans(list_to_dict(round_list))  # change to remove <<DIRECT ACCESS>> to variable


# calculates points and finds winner from list of Player objects
def tally(all_turns, this_game):
    for player in all_turns:  # loops each dictionary of answers (one for each round played)
        print(player.get_ans())
        for letter in ALPHA:  # loops alphabet
            choice = player.answers[letter]  # takes answer for each letter in the dictionary <<DIRECT ACCESS>>
            if is_unique(choice, this_game):  # if it's unique adds one point
                player.add_pt(1)
        player.calc_total()
        print(player.name + ' got ' + str(player.points) + ' points. Now they have ' + str(player.total_points) + '.')
# <<DIRECT ACCESS>>  ^^^^^^^^^^^


# prints the winner(s) of the game by using info saved in winner directory
def final_results(all_players):
    high_score = 0
    champ = []
    for each in all_players:
        if each.total_points > high_score:
            champ.clear()
            champ.append(each)
        elif each.total_points == high_score:
            champ.append(each)
    if len(champ) == 1:
        print('Congratulations to the champion: ' + champ[0].name + '!!!')
    elif len(champ) > 1:
        print('It\'s a tie!')
        print(high_score)


# takes a players answer and checks it against the global answer record to see if it was unique
def is_unique(player_answer, this_game):
    if player_answer:  # returns false if empty list (no answer given)
        answers_list = this_game.answers[scat.to_key(player_answer)]  # locates the answer list from first letter <<DA>>
        if answers_list.count(player_answer) == 1:  # if received answer is unique in the list
            return True


# converts the list for the round to a dictionary with keys for each letter
def list_to_dict(the_list):
    new_dict = ROUND.copy()  # gets blank dictionary with {letter:empty list, etc}
    for each in the_list:  # loops answer list
        letter = scat.to_key(each)
        if letter in new_dict:
            new_dict[letter] = each  # assigns as value in dictionary based of first letter of each answer
    return new_dict


# takes name of all the players who will be in the game and creates a Player obj for them, exported together as a list
def create_roster(size):
    order = []
    for i in range(size):
        print('Your turn Player ' + str(i + 1) + ': ')
        order.append(user.Player(i))  # creates a Player object and adds it to the order list
        order[i].pick_name()
    return order


# clears necessary data from all players in a list using func from Player class
def new_game(all_players):
    for each in all_players:
        each.clear_data()


def main():
    scat.welcome()
    num_players = int(input('How many players will there be? '))
    p_order = create_roster(num_players)
    all_rounds = []
    round_id = 0  # NOT ACTUALLY MAKING USE OF THIS VARIABLE
    while True:
        if scat.play_again():
            this_round = game.Game(num_players, round_id)
            this_round.get_cat()  # CAN I RUN THIS FUNC DURING INITIALIZATION?
            new_game(p_order)  # PERHAPS THIS FUNC SHOULD BE PART OF GAME OBJ INSTEAD?
            for i in range(num_players):  # THE TIMER WOULD BE IN THIS LOOP
                print('Good luck, ' + p_order[i].name)  # <<DIRECT ACCESS>> ADD CATEGORY REMINDER
                play_round(p_order[i], this_round)
            tally(p_order, this_round)
            the_winners = this_round.compare_scores(p_order)
            for each in the_winners:
                print('The winner of this round was ' + each.name + '.')
                each.add_win()
            all_rounds.append(this_round)
            round_id += 1
        else:  # NOT EDITING TONIGHT BUT THESE LINES NOT NECESSARY
            break
    final_results(p_order)


"""
IN GENERAL I FEEL LIKE THERE MUST BE A MORE SUCCINCT WAY TO END THAN WHAT I HAVE NOW
    - THREE? FUNCTIONS ADDING/CALCULATING SCORES
    - FOLLOWING ALMOST THE EXACT SAME LOGICAL FLOW TO DETERMINE THE OVERALL WINNER
"""


if __name__ == '__main__':
    main()
