"""
Round.py

Takes input from user to construct an alphabetical list of words, with options to view
the current list of words or to cease input. Uses a global string to keep track of which
letters haven't been used yet. Imports isolated functions from scattegory module.
"""

import random
import copy
import scattegory as scat
import players as user
ALPHA = scat.ALPHABET
ANSWERS = copy.deepcopy(scat.blank_dict)
ROUND = copy.deepcopy(scat.blank_dict)


# takes a new word from user while tracking letters remaining
def get_entry(turn_alphabet):
    while True:
        word = scat.enter_word()
        if word == 'STOP':
            return word
        elif word == 'VIEW':
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


# plays a round for one player and returns result as a dictionary
def play_round(participant):
    round_alphabet = ALPHA
    round_list = []
    while True:
        next_word = get_entry(round_alphabet)
        if next_word == 'STOP':  # breaks input loop
            print('Okay no more')
            print()
            break
        elif next_word == 'VIEW':  # lets user see their current list and what letters remain
            scat.sort_print(round_list)
            print('You still have no entry for: ' + round_alphabet)
            print()
        else:  # otherwise adds entry to list of answers this round
            round_list.append(next_word)
            ANSWERS[scat.to_key(next_word)].append(next_word)  # and to game answers
            round_alphabet = round_alphabet.replace(scat.to_key(next_word), '_')  # updates alphabet removing letter
    scat.sort_print(round_list)
    print('You failed to come up with an answer for letters ' + round_alphabet)
    print('Hope that was good enough...')
    print()
    participant.answers = list_to_dict(round_list)


# calculates points and finds winner from list of Player objects
def winner(all_rounds):
    for player in all_rounds:  # loops each dictionary of answers (one for each round played)
        for letter in ALPHA:  # loops alphabet
            choice = player.answers[letter]  # takes answer for each letter in the dictionary
            if answers(choice):  # if it's unique adds one point
                player.add_pt(1)
        print(player.print_name() + ' got ' + str(player.pts()) + ' points.')
    return


# prints the winner(s) of the game by using info saved in winner directory
def print_results(final_stats):  # TAKES GAME STATS VARIABLE INSTEAD
    if final_stats['Result'] == 'Win':
        print('Congratulations to the champion: Player ' + final_stats['Player'])
        print()
    elif final_stats['Result'] == 'Tie':
        print('It\'s a tie!')
        print('Well done Players ' + final_stats['Player'] + '. The rest of y\'all sorry.')
        print()


# takes a players answer and checks it against the global answer record to see if it was unique
def answers(player_answer):
    if player_answer:  # returns false if empty list (no answer given)
        answers_list = ANSWERS[scat.to_key(player_answer)]  # locates the answer list from first letter of given answer
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


def main():  # USE PLAYER CLASS IN MAIN, INCORPORATE PLAYER NAME, MULTIPLE ROUNDS, TRACKING GAME HISTORY
    scat.welcome()
    order = []  # better/possible to make this a tuple instead?
    game = int(input('How many players will there be? '))
    print('Affirmative. The category is: ' + scat.category(random.randint(0, len(scat.CATEGORIES) - 1)))
    print()
    for i in range(game):
        print('Your turn Player ' + str(i + 1) + ': ')
        order.append(user.Player(i))  # creates a Player object and adds it to the order list
        order[i].pick_name()
        play_round(order[i])
        print('Nice job, ' + order[i].print_name() + '!')
        # print(order[i].answer_history)
    winner(order)
    print(ANSWERS)


if __name__ == '__main__':
    main()
