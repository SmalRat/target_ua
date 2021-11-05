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
    >>> get_words("base.lst", ['й', 'є', 'ю'])
    [('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), \
('єдваб', 'noun'), ('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), \
('ємно', 'adverb'), ('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), \
('єресь', 'noun'), ('єри', 'noun'), ('єрик', 'noun'), ('єрик', 'noun'), \
('єство', 'noun'), ('єті', 'noun'), ('єхида', 'noun'), ('йняти', 'verb'), \
('йог', 'noun'), ('йога', 'noun'), ('йод', 'noun'), ('йодат', 'noun'), \
('йодид', 'noun'), ('йодил', 'noun'), ('йодит', 'noun'), ('йодль', 'noun'), \
('йола', 'noun'), ('йолоп', 'noun'), ('йомен', 'noun'), ('йон', 'noun'), \
('йорж', 'noun'), ('йорж', 'noun'), ('йот', 'noun'), ('йота', 'noun'), \
('йти', 'verb'), ('йтися', 'verb'), ('юань', 'noun'), ('юга', 'noun'), \
('югурт', 'noun'), ('юда', 'noun'), ('юдей', 'noun'), ('юдин', 'adjective'), \
('юдоль', 'noun'), ('юзом', 'adverb'), ('юїтка', 'noun'), ('юка', 'noun'), \
('юкола', 'noun'), ('юнак', 'noun'), ('юнга', 'noun'), ('юний', 'adjective'), \
('юніор', 'noun'), ('юнка', 'noun'), ('юнкер', 'noun'), ('юнкор', 'noun'), \
('юннат', 'noun'), ('юнь', 'noun'), ('юпка', 'noun'), ('юра', 'noun'), \
('юрба', 'noun'), ('юрик', 'noun'), ('юрист', 'noun'), ('юрма', 'noun'), \
('юрода', 'noun'), ('юрок', 'noun'), ('юрок', 'noun'), \
('юрта', 'noun'), ('юрфак', 'noun'), ('юс', 'noun'), ('ют', 'noun'), \
('ютуб', 'noun'), ('юферс', 'noun'), ('юхта', 'noun'), ('юшити', 'verb'), \
('юшка', 'noun'), ('ююба', 'noun')]
    """
    good_words = []
    with open(path, "r", encoding="utf-8") as dictionary:
        lines = dictionary.readlines()
        for i, _ in enumerate(lines):
            lines[i] = lines[i].lower().strip()
            try:
                line = lines[i].split(" ")[1]
                if len(lines[i].split()[0]) < 6 and \
                        (line[:2] == "/n" or line[:2] == "/v" or\
                         line[:4] == "/adj" or line[:3] == "adv" or\
                         line[0] == "n" or line[0] == "v"\
                         or line[:3] == "adj"  or line[:4] == "noun")\
                        and (lines[i][0] in letters):
                    if (line[:2] == "/n" or line[0] == "n" or line[:4] == "noun")\
                            and line[:7] != "noninfl":
                        good_words.append(tuple((lines[i].split(" ")[0], "noun")))
                    if line[:4] == "/adj" or line[:3] == "adj":
                        good_words.append(tuple((lines[i].split(" ")[0], "adjective")))
                    if line[:2] == "/v" or line[0] == "v":
                        good_words.append(tuple((lines[i].split(" ")[0], "verb")))
                    if line[:3] == "adv":
                        good_words.append(tuple((lines[i].split(" ")[0], "adverb")))
            except IndexError:
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
    new_dict = []
    for i, word in enumerate(dict_of_words):
        if dict_of_words[i][1] == language_part:
            new_dict.append(word)
            words_list.append(word[0])
    correct_words = []

    for word in user_words:
        if word in words_list:
            if word[0] in letters and new_dict[words_list.index(word)][1] == language_part:
                correct_words.append(word)
                words_list.pop(words_list.index(word))
    return correct_words, words_list
