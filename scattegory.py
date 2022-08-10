
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


CATEGORIES = ['Cities', 'Snack Foods', 'Musical Artists', 'Sports Teams/Clubs', 'Novels', 'Actors']


def welcome():
    print(
        """
Merry Christmas!

Your challenge is, given a category, to think of an entry for each letter in the 
alphabet. When prompted, type your answer to make an entry. Type "view" to see what
letters remain. Type "stop" to give up.

Good Luck!"""
    )


def category(draw):
    return CATEGORIES[draw]


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
