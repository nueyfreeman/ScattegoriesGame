"""
Round.py

Takes inputs from user to construct an alphabetical list of words, with options to view
the current list of words or to cease input. Uses a global string to keep track of which
letters haven't been used yet. Imports isolated functions from scattegory module.
"""

import random
import copy
import scattegory as scat
ALPHA = scat.ALPHABET
ANSWERS = copy.deepcopy(scat.blank_dict)
ROUND = copy.deepcopy(scat.blank_dict)


# takes a new word from user while using global string ACCEPTABLE to track letters remaining
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


# checks that the entered word starts with an acceptable letter, if so, updates global string
def check(letters_remaining, entry):
    letter = entry[0]
    if letter in letters_remaining:
        return True


# plays a round for one player and returns result as a dictionary
def play_round():
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
            ANSWERS[next_word[0]].append(next_word)  # and to game answers
            round_alphabet = round_alphabet.replace(next_word[0], '_')  # updates alphabet string removing that letter
    scat.sort_print(round_list)
    print('You failed to come up with an answer for letters ' + round_alphabet)
    print('Hope that was good enough...')
    print()
    return list_to_dict(round_list)


# calculates points and finds winner from player list
def winner(all_rounds):
    scores = []
    for player in all_rounds:
        points = 0
        for letter in ALPHA:
            choice = player[letter]
            if answers(choice):
                points += 1


# takes a players answer and checks it against the global answer record to see if it was unique
def answers(player_answer):
    answers_list = ANSWERS[player_answer[0]]
    if answers_list.count(player_answer) == 1:
        return True


def list_to_dict(the_list):
    new_dict = ROUND.copy()
    for each in the_list:
        letter = each[0]
        k = letter.upper()
        if k in new_dict:
            new_dict[k] = each
    return new_dict


def main():
    scat.welcome()
    player_list = []
    players = int(input('How many players will there be? '))
    print('Bet.')
    print()
    print('The category will be: ' + scat.category(random.randint(0, len(scat.CATEGORIES) - 1)))
    for i in range(players):
        print('Your turn Player ' + str(i + 1) + ': ')
        player_list.append(play_round())
        #print(player_list[i])
    # winner(player_list)
    print(ANSWERS)


if __name__ == '__main__':
    main()
