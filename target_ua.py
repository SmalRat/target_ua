"""
Module of game about making words(UA version)
"""
from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.

    >>> random.seed(2020)
    >>> generate_grid()
    ['і', 'щ', 'ш', 'ь', 'у']
    """
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    grid = []
    count = 0
    while count < 5:
        letter = random.choice(alphabet)
        if letter not in grid:
            count+=1
            grid.append(letter)
    return grid

def get_words(path: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> print("No time")
    No time
    """
    good_words = []
    with open(path, "r", encoding="utf-8") as dictionary:
        lines = dictionary.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].lower().strip()
            try:
                line = lines[i].split(" ")[1]
                if len(lines[i].split()[0]) < 6 and \
                        (line[:2] == "/n" or line[:2] == "/v" or\
                         line[:4] == "/adj" or line[:3] == "adv" or\
                         line[0] == "n" or line[0] == "v"\
                         or line[:3] == "adj"  or line[:4] == "noun")\
                        and (lines[i][0] in letters):
                    if (line[:2] == "/n" or line[0] == "n" or line[:4] == "noun") and line[:7] != "noninfl":
                        good_words.append(tuple((lines[i].split(" ")[0], "noun")))
                    if line[:4] == "/adj" or line[:3] == "adj":
                        good_words.append(tuple((lines[i].split(" ")[0], "adjective")))
                    if line[:2] == "/v" or line[0] == "v":
                        good_words.append(tuple((lines[i].split(" ")[0], "verb")))
                    if line[:3] == "adv":
                        good_words.append(tuple((lines[i].split(" ")[0], "adverb")))
            except:
                pass
    return good_words

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user's words
    >>> print("Sorry, l have no time")
    Sorry, l have no time

    :param user_words:
    :param language_part:
    :param letters:
    :param dict_of_words:
    :return:
    """
    words_list = []
    for word in dict_of_words:
        words_list.append(word[0])
    correct_words = []
    for word in user_words:
        if word[0] in letters and dict_of_words[words_list.index(word)][1] == language_part:
            correct_words.append(word)
            words_list.pop(words_list.index(word))
    return correct_words, words_list
print(get_words("base.lst", ['й', 'є', 'ю']))
