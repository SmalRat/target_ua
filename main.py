"""
Module of game about making words
"""
from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    >>> random.seed(2190)
    >>> generate_grid()
    [['S', 'L', 'B'], ['H', 'X', 'V'], ['S', 'Q', 'R']]
    """
    grid = []
    for i in range(3):
        grid.append([])
        for j in range(3):
            j += 0
            grid[i].append(chr(random.randint(65, 90)))
    return grid


def get_words(path: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words("en.txt", ['f', 'r', 'l', 'h', 'k', 'd', 'z', 'g', 'i'])
    ['dirk', 'firk', 'khir']
    """
    good_words = []
    main_letter = letters[4]
    with open(path, "r", encoding="utf-8") as dictionary:
        lines = dictionary.readlines()
        for i in range(3, len(lines)):
            lines[i] = lines[i].lower().strip()
            if (main_letter in lines[i]) and len(lines[i]) >= 4:
                check = 1
                for letterl in lines[i]:
                    if (letterl not in letters) or lines[i].count(letterl) > letters.count(letterl):
                        check = 0
                if check == 1:
                    good_words.append(lines[i])
    return good_words



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.

    Don't know, how to write this doctest, how to use shortcuts.
    """
    words = []
    while True:
        try:
            words.append(input())
        except EOFError:
            break
    return words


def get_pure_user_words(user_words: List[str], letters: List[str],\
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['dirk', 'firk', 'frlhk'],\
    ['f', 'r', 'l', 'h', 'k', 'd', 'z', 'g', 'i'],\
    ['dirk', 'firk', 'khir'])
    ['frlhk']
    """
    pure_words = []
    main_letter = letters[4]
    for i, _ in enumerate(user_words):
        user_words[i] = user_words[i].lower().strip()
        if (main_letter in user_words[i]) and len(user_words[i]) >= 4\
                and (user_words[i] not in words_from_dict):
            check = 1
            for letterl in user_words[i]:
                if (letterl not in letters) or \
                        user_words[i].count(letterl) > letters.count(letterl):
                    check = 0
            if check == 1:
                pure_words.append(user_words[i])
    return pure_words


def results():
    """
    Prints results
    >>> print("some results")
    some results
    """
    letters_init = generate_grid()
    letters_end = []
    for i in range(3):
        letters_end += letters_init[i]
    for i, letter in enumerate(letters_end):
        letters_end[i] = letter.lower()
    dictionarym = get_words("en.txt", letters_end)
    user_words_list = get_user_words()
    get_pure_user_words(user_words_list, letters_end, dictionarym)


if __name__ == "__main__":
    results()
