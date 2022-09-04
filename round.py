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
    players = 0
    champ = {'Result': 'Win', 'Player': 0, 'Points': 0}
    for player in all_rounds:  # loops each dictionary of answers (one for each round played)
        points = 0
        players += 1  # keeps track of player identity by keeping count
        for letter in ALPHA:  # loops alphabet
            choice = player[letter]  # takes answer for each letter in the dictionary
            if answers(choice):  # if it's unique adds one point
                points += 1
        print('Player ' + str(players) + ' got ' + str(points) + ' points.')
        print()
        if champ['Points'] < points:  # if score gives new leader updates directory
            champ['Result'] = 'Win'
            champ['Player'] = str(players)
            champ['Points'] = points
        elif champ['Points'] == points:  # also if score gives tied leader
            champ['Result'] = 'Tie'
            champ['Player'] = str(champ['Player']) + ' and ' + str(players)
    return champ


# prints the winner(s) of the game by using info saved in winner directory
def print_results(final_stats):
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
        answers_list = ANSWERS[player_answer[0]]  # locates the answer list based on first letter of received answer
        if answers_list.count(player_answer) == 1:  # if received answer is unique in the list
            return True


# converts the list for the round to a dictionary with keys for each letter
def list_to_dict(the_list):
    new_dict = ROUND.copy()  # gets blank dictionary with {letter:empty list, etc}
    for each in the_list:  # loops answer list
        letter = each[0].upper()
        if letter in new_dict:
            new_dict[letter] = each  # assigns as value in dictionary based of first letter of each answer
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
    print_results(winner(player_list))


if __name__ == '__main__':
    main()
