import random


blank_dict = {  # make this a function instead
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': [],
}


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


CATEGORIES = ['Global Cities', 'Towns in Minnesota', 'Fast Food Restaurants', 'Singers', 'Spices', 'European Countries',
              'Netflix Shows', 'African Countries', 'Comedians', 'Bands/Musical Groups', 'States', 'Ice Cream Flavors',
              'Rappers', 'Cartoons', 'Clothing Brands']


def welcome():
    print(
        """
Merry Christmas!

Your challenge is, given a category, to think of an entry for each letter in the 
alphabet. When prompted, type your answer to make an entry. Type "view" to see what
letters remain. Type "stop" to give up.

Good Luck!
"""
    )


def get_category():
    prompt = CATEGORIES[random.randint(0, len(CATEGORIES) - 1)]
    print('New game beginning now.')
    print('The category is: ' + prompt)
    print()
    return prompt


def key(word):
    return word[0].upper()


# retrieve lower case word from user
def enter_word():
    word = input('Next choice: ')
    return word.strip().upper()


# puts the list in alphabetical order and prints it
def sort_print(input_list):
    input_list.sort()
    return input_list


# lets user choose to continue and clears relevant data from player instances to begin game
def play_again(all_players):
    pick = input('Shall we play...? (Press enter to continue or any other key to stop playing)')
    if pick == '':
        for each in all_players:
            each.clear_data()
        return True
