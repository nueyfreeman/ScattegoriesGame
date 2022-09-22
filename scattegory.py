import random


blank_dict = {
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


def category(draw):   # REDUNDANT --> DELETE IT
    return CATEGORIES[draw]


def get_category():
    prompt = CATEGORIES[random.randint(0, len(CATEGORIES) - 1)]
    print('New game beginning now.')
    print('The category is: ' + prompt)
    print()
    return prompt


def to_key(word):
    letter = word[0]
    return letter.upper()


# retrieve lower case word from user
def enter_word():
    word = input('Next choice: ')
    word.strip()
    return word.upper()


# puts the list in alphabetical order and prints it
def sort_print(input_list):
    input_list.sort()
    print(input_list)


def play_again():
    pick = input('Shall we play...? (Type y to continue or any other key to stop playing)')
    return True if pick == 'y' else False  # felt pretty simple but maybe better not to use one-liners at all?
