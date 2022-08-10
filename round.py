"""
Round.py

Takes inputs from user to construct an alphabetical list of words, with options to view
the current list of words or to cease input. Uses a global string to keep track of which
letters haven't been used yet. Imports isolated functions from scattegory module.
"""

import random
import scattegory as scat
global ACCEPTABLE
ALPHABET = scat.ALPHABET
ANSWERS = scat.blank_dict.copy()


# takes a new word from user while using global string ACCEPTABLE to track letters remaining
def get_entry():
    while True:
        word = scat.enter_word()
        if word == 'STOP':
            return word
        elif word == 'VIEW':
            return word
        else:
            if check(word):
                return word
            else:
                print('That ain\'t it chief. Try again')


# checks that the entered word starts with an acceptable letter, if so, updates global string
def check(entry):
    global ACCEPTABLE
    letter = entry[0]
    if letter in ACCEPTABLE:
        ACCEPTABLE = ACCEPTABLE.replace(letter, '_')
        return True


# plays a round for one player and returns result as a dictionary
def play_round():
    global ACCEPTABLE
    ACCEPTABLE = ALPHABET  # re-initializes string for alphabet
    name_list = []
    while True:
        next_word = get_entry()
        if next_word == 'STOP':  # breaks input loop
            print('Okay no more')
            break
        elif next_word == 'VIEW':  # lets user see their current list and what letters remain
            scat.sort_print(name_list)
            print('You still have no entry for: ')
            print(ACCEPTABLE)
        else:  # otherwise adds entry to list
            name_list.append(next_word)
            ANSWERS[next_word[0]].append(next_word)
            # TRY ADJUSTING COUNTER STRING HERE SO NO NEED TO KEEP RESETTING GLOBAL VARIABLE
    scat.sort_print(name_list)
    print(ACCEPTABLE)
    # FUNCTION TO POP EACH ENTRY IN LIST AND ADD IT TO APPROPRIATE ANSWER LIST
    name_dict = list_to_dict(name_list)
    '''
    THIS IS WHERE THE PROBLEM IS ^^^ THIS LINE/FUNCTION USES ANSWER DICT INSTEAD OF A BLANK ONE
    '''
    return name_dict


# pops each entry from list and adds it to global answers
def add_to_answers(the_list):
    pass


# calculates points and finds winner from player list
def winner(all_rounds):
    scores = []
    for player in all_rounds:
        points = 0
        for letter in ALPHABET:
            choice = player[letter]
            if answers(choice):
                points += 1


# takes a players answer and checks it against the global answer record to see if it was unique
def answers(player_answer):
    answers_list = ANSWERS[player_answer[0]]
    if answers_list.count(player_answer) == 1:
        return True


def list_to_dict(the_list):
    new_dict = scat.blank_dict.copy()
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
    print('The category will be: ' + scat.category(random.randint(0, len(scat.CATEGORIES))))
    for i in range(players):
        print('Your turn Player ' + str(i + 1) + ': ')
        this_round = play_round()
        player_list.append(this_round)
        print(player_list[i])
    # winner(player_list)
    print(ANSWERS)


if __name__ == '__main__':
    main()
