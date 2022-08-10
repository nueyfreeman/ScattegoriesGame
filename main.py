"""
First project tinkering with Python and practicing lists

Lets user input words which are catalogued in an alphabetized list with no repeat letters. They
can enter "v" to view the list or "n" to stop input and view the final list.
"""


# checks to see if already have a name starting with that character
def have_already(word, old_list):
    new_list = old_list.copy()  # copy list
    while new_list:
        name = new_list.pop()
        letter = name[0]
        match = word[0]
        if letter == match:
            print('You already have a name starting with "' + match + '" . Please try another.')
            return True


# sorts the current list and prints it
def sort_print(input_list):
    input_list.sort()
    print(input_list)


# makes a list
def build_list():
    name_list = []
    again = True
    while again:
        if get_name(name_list):
            print('Got it. Add another?')
        else:
            print('List completed')
            again = False
    sort_print(name_list)
    return name_list


# takes input with option to view list and to cease inputs
def get_name(n_list):
    entry = (input('Enter a name: '))
    if entry == 'n':
        return False
    elif entry == 'v':
        sort_print(n_list)
        return True
    elif entry == '':
        return True
    else:
        if have_already(entry, n_list):
            return True
        else:
            n_list.append(entry)
            return True


def main():
    list1 = build_list()
    list2 = build_list()
    print(list1)
    print(list2)


if __name__ == '__main__':
    main()
