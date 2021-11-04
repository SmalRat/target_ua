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
    >>> get_words("base.lst", ['і', 'щ', 'ш', 'ь', 'у'])
    [('ібіс', 'noun'), ('івасі', 'noun'), ('іврит', 'noun'), ('іглу', 'noun'), ('ігрек', 'noun'), ('ідеал', 'noun'), ('ідея', 'noun'), ('ідіот', 'noun'), ('ідо', 'noun'), ('ідол', 'noun'), ('ієрей', 'noun'), ('іже', 'noun'), ('іжиця', 'noun'), ('ізвод', 'noun'), ('ізгой', 'noun'), ('ізм', 'noun'), ('ізнов', 'adverb'), ('ізюбр', 'noun'), ('ікати', 'verb'), ('ікло', 'noun'), ('ікона', 'noun'), ('ікра', 'noun'), ('ікс', 'noun'), ('іксія', 'noun'), ('ілеус', 'noun'), ('ільм', 'noun'), ('імаго', 'noun'), ('імаго', 'noun'), ('імаго', 'noun'), ('імам', 'noun'), ('імбир', 'noun'), ('імід', 'noun'), ('імідж', 'noun'), ('імін', 'noun'), ('імла', 'noun'), ('імпет', 'noun'), ('імхо', 'noun'), ("ім'я", 'noun'), ('інак', 'adverb'), ('інако', 'adverb'), ('інвар', 'noun'), ('інгуш', 'noun'), ('інде', 'adverb'), ('індик', 'noun'), ('індій', 'noun'), ('індол', 'noun'), ('індус', 'noun'), ('інет', 'noun'), ('інжир', 'noun'), ('іній', 'noun'), ('інкуб', 'noun'), ('іноді', 'adverb'), ('інок', 'noun'), ('інтим', 'noun'), ('інфіз', 'noun'), ('інь', 'noun'), ('іон', 'noun'), ('іоніт', 'noun'), ('іонол', 'noun'), ('іприт', 'noun'), ('ірбіс', 'noun'), ('ірга', 'noun'), ('іржа', 'noun'), ('ірис', 'noun'), ('ірис', 'noun'), ('ірит', 'noun'), ('ірмос', 'noun'), ('ірод', 'noun'), ('іскра', 'noun'), ('іслам', 'noun'), ('іспит', 'noun'), ('істик', 'noun'), ('іти', 'verb'), ('ітися', 'verb'), ('ітрій', 'noun'), ('іуда', 'noun'), ('іудей', 'noun'), ('іудин', 'adjective'), ('ішак', 'noun'), ('ішіас', 'noun'), ('ішхан', 'noun'), ('іще', 'adverb'), ('уазик', 'noun'), ('убити', 'verb'), ('убік', 'adverb'), ('убір', 'noun'), ('убіч', 'adverb'), ('убрід', 'adverb'), ('убрус', 'noun'), ('убути', 'verb'), ('увага', 'noun'), ('увал', 'noun'), ('увеїт', 'noun'), ('увера', 'noun'), ('уверх', 'adverb'), ('увись', 'adverb'), ('увити', 'verb'), ('увід', 'noun'), ('увід', 'noun'), ('увік', 'adverb'), ('увіч', 'adverb'), ('уволю', 'adverb'), ('угав', 'noun'), ('угар', 'noun'), ('угара', 'noun'), ('уггі', 'noun'), ('угин', 'noun'), ('угі', 'noun'), ('угія', 'noun'), ('углиб', 'adverb'), ('углич', 'noun'), ('угода', 'noun'), ('угорі', 'adverb'), ('угору', 'adverb'), ('угрин', 'noun'), ('удав', 'noun'), ('удар', 'noun'), ('удати', 'verb'), ('удача', 'noun'), ('удень', 'adverb'), ('удій', 'noun'), ('уділ', 'noun'), ('удова', 'noun'), ('удовж', 'adverb'), ('удома', 'adverb'), ('уже', 'adverb'), ('ужити', 'verb'), ('узбіч', 'adverb'), ('узвар', 'noun'), ('узвіз', 'noun'), ('узір', 'noun'), ('узор', 'noun'), ('узус', 'noun'), ('узути', 'verb'), ('узяти', 'verb'), ('уїзд', 'noun'), ('уїсти', 'verb'), ('уйгур', 'noun'), ('уймак', 'noun'), ('указ', 'noun'), ('укіс', 'noun'), ('уклад', 'noun'), ('уклін', 'noun'), ('уклон', 'noun'), ('укол', 'noun'), ('украй', 'adverb'), ('укріп', 'noun'), ('укупі', 'adverb'), ('укус', 'noun'), ('улад', 'adverb'), ('улан', 'noun'), ('улар', 'noun'), ('улем', 'noun'), ('улити', 'verb'), ('улич', 'noun'), ('уліво', 'adverb'), ('улов', 'noun'), ('улус', 'noun'), ('ульва', 'noun'), ('ум', 'noun'), ('умбон', 'noun'), ('умбра', 'noun'), ('умент', 'adverb'), ('умити', 'verb'), ('умить', 'adverb'), ('уміст', 'noun'), ('уміти', 'verb'), ('умма', 'noun'), ('умова', 'noun'), ('унабі', 'noun'), ('унада', 'noun'), ('униз', 'adverb'), ('унизу', 'adverb'), ('уніат', 'noun'), ('унізм', 'noun'), ('унія', 'noun'), ('уночі', 'adverb'), ('унт', 'noun'), ('унтер', 'noun'), ('унук', 'noun'), ('унуча', 'noun'), ('унція', 'noun'), ('упень', 'adverb'), ('уперш', 'adverb'), ('упин', 'noun'), ('упир', 'noun'), ('упити', 'verb'), ('уплав', 'adverb'), ('уплив', 'noun'), ('упор', 'noun'), ('упор', 'noun'), ('упору', 'adverb'), ('упряж', 'noun'), ('ураз', 'adverb'), ('ураза', 'noun'), ('уран', 'noun'), ('уреат', 'noun'), ('урема', 'noun'), ('урина', 'noun'), ('урити', 'verb'), ('уріз', 'noun'), ('урна', 'noun'), ('урода', 'noun'), ('урок', 'noun'), ('урюк', 'noun'), ('уряд', 'adverb'), ('уряд', 'noun'), ('усач', 'noun'), ('услід', 'adverb'), ('усмак', 'adverb'), ('усміх', 'noun'), ('усний', 'adjective'), ('усоте', 'adverb'), ('успід', 'adverb'), ('успіх', 'noun'), ('уста', 'noun'), ('устав', 'noun'), ('усташ', 'noun'), ('уступ', 'noun'), ('устя', 'noun'), ('устяж', 'adverb'), ('усус', 'noun'), ('усуху', 'adverb'), ('усюди', 'adverb'), ('усяко', 'adverb'), ('утвір', 'noun'), ('утеча', 'noun'), ('утиль', 'noun'), ('утиск', 'noun'), ('утік', 'noun'), ('утіха', 'noun'), ('утлий', 'adjective'), ('утома', 'noun'), ('утор', 'noun'), ('утяти', 'verb'), ('ухати', 'verb'), ('ухил', 'noun'), ('ухід', 'noun'), ('учвал', 'adverb'), ('учень', 'noun'), ('учити', 'verb'), ('учора', 'adverb'), ('учта', 'noun'), ('учути', 'verb'), ('ушир', 'adverb'), ('ушити', 'verb'), ('ушкал', 'noun'), ('ушко', 'noun'), ('ушу', 'noun'), ('ущент', 'adverb'), ('уява', 'noun'), ('уявки', 'adverb'), ('уявне', 'noun'), ('уявно', 'adverb'), ('шабат', 'noun'), ('шабаш', 'noun'), ('шабер', 'noun'), ('шабля', 'noun'), ('шавка', 'noun'), ('шаг', 'noun'), ('шайба', 'noun'), ('шайка', 'noun'), ('шакал', 'noun'), ('шал', 'noun'), ('шалаш', 'noun'), ('шале', 'noun'), ('шалик', 'noun'), ('шалон', 'noun'), ('шалот', 'noun'), ('шаль', 'noun'), ('шаля', 'noun'), ('шаман', 'noun'), ('шамот', 'noun'), ('шана', 'noun'), ('шанкр', 'noun'), ('шанс', 'noun'), ('шапка', 'noun'), ('шар', 'noun'), ('шарж', 'noun'), ('шарм', 'noun'), ('шарф', 'noun'), ('шасі', 'noun'), ('шасла', 'noun'), ('шатен', 'noun'), ('шати', 'noun'), ('шатія', 'noun'), ('шатл', 'noun'), ('шатро', 'noun'), ('шаттл', 'noun'), ('шатун', 'noun'), ('шатуш', 'noun'), ('шафа', 'noun'), ('шафар', 'noun'), ('шафка', 'noun'), ('шах', 'noun'), ('шах', 'noun'), ('шахва', 'noun'), ('шахи', 'noun'), ('шахід', 'noun'), ('шахта', 'noun'), ('шашка', 'noun'), ('шваль', 'noun'), ('шваля', 'noun'), ('швач', 'noun'), ('швець', 'noun'), ('швора', 'noun'), ('шевро', 'noun'), ('шейк', 'noun'), ('шейх', 'noun'), ('шелак', 'noun'), ('шелех', 'noun'), ('шелті', 'noun'), ('шельф', 'noun'), ('шелюг', 'noun'), ('шелюг', 'noun'), ('шеляг', 'noun'), ('шемая', 'noun'), ('шепіт', 'noun'), ('шерег', 'noun'), ('шерех', 'noun'), ('шериф', 'noun'), ('шерп', 'noun'), ('шеф', 'noun'), ('шефів', 'adjective'), ('шиба', 'noun'), ('шибер', 'noun'), ('шибка', 'noun'), ('шиїзм', 'noun'), ('шиїт', 'noun'), ('шийка', 'noun'), ('шик', 'noun'), ('шило', 'noun'), ('шина', 'noun'), ('шинка', 'noun'), ('шиння', 'noun'), ('шинок', 'noun'), ('шип', 'noun'), ('шип', 'noun'), ('шип', 'noun'), ('шипик', 'noun'), ('шипун', 'noun'), ('шир', 'noun'), ('ширма', 'noun'), ('шитво', 'noun'), ('шити', 'verb'), ('шитий', 'adjective'), ('шиття', 'noun'), ('шифер', 'noun'), ('шифон', 'noun'), ('шифр', 'noun'), ('шихта', 'noun'), ('шишак', 'noun'), ('шишка', 'noun'), ('шия', 'noun'), ('шіацу', 'noun'), ('шкала', 'noun'), ('шкапа', 'noun'), ('шквал', 'noun'), ('шків', 'noun'), ('шкіра', 'noun'), ('шкіц', 'noun'), ('шкода', 'noun'), ('шкода', 'noun'), ('шкода', 'noun'), ('школа', 'noun'), ('шкот', 'noun'), ('шкура', 'noun'), ('шлак', 'noun'), ('шлам', 'noun'), ('шланг', 'noun'), ('шлейф', 'noun'), ('шлем', 'noun'), ('шлея', 'noun'), ('шлик', 'noun'), ('шлір', 'noun'), ('шліф', 'noun'), ('шліх', 'noun'), ('шліц', 'noun'), ('шлюб', 'noun'), ('шлюз', 'noun'), ('шлюп', 'noun'), ('шлюха', 'noun'), ('шляк', 'noun'), ('шляк', 'noun'), ('шлям', 'noun'), ('шлях', 'noun'), ('шмат', 'noun'), ('шмата', 'noun'), ('шмига', 'noun'), ('шнапс', 'noun'), ('шнек', 'noun'), ('шнур', 'noun'), ('шов', 'noun'), ('шовк', 'noun'), ('шок', 'noun'), ('шокер', 'noun'), ('шолом', 'noun'), ('шопа', 'noun'), ('шопка', 'noun'), ('шорея', 'noun'), ('шори', 'noun'), ('шорка', 'noun'), ('шорка', 'noun'), ('шорти', 'noun'), ('шосе', 'noun'), ('шоста', 'noun'), ('шоу', 'noun'), ('шофер', 'noun'), ('шпага', 'noun'), ('шпак', 'noun'), ('шпала', 'noun'), ('шпана', 'noun'), ('шпара', 'noun'), ('шпат', 'noun'), ('шпача', 'noun'), ('шпень', 'noun'), ('шпиг', 'noun'), ('шпик', 'noun'), ('шпик', 'noun'), ('шпиль', 'noun'), ('шпиця', 'noun'), ('шпіц', 'noun'), ('шпон', 'noun'), ('шпона', 'noun'), ('шпора', 'noun'), ('шприц', 'noun'), ('шпрот', 'noun'), ('шпуля', 'noun'), ('шпунт', 'noun'), ('шпур', 'noun'), ('шрам', 'noun'), ('шримс', 'noun'), ('шрифт', 'noun'), ('шріт', 'noun'), ('шрот', 'noun'), ('шруті', 'noun'), ('штаб', 'noun'), ('штаба', 'noun'), ('штаг', 'noun'), ('штазі', 'noun'), ('штам', 'noun'), ('штамб', 'noun'), ('штамп', 'noun'), ('штани', 'noun'), ('штат', 'noun'), ('штейн', 'noun'), ('штетл', 'noun'), ('штиб', 'noun'), ('штиба', 'noun'), ('штик', 'noun'), ('штиль', 'noun'), ('штиль', 'noun'), ('штир', 'noun'), ('штирк', 'noun'), ('штифт', 'noun'), ('штих', 'noun'), ('шток', 'noun'), ('шток', 'noun'), ('штора', 'noun'), ('шторм', 'noun'), ('штос', 'noun'), ('штоф', 'noun'), ('штоф', 'noun'), ('штраф', 'noun'), ('штрек', 'noun'), ('штрик', 'noun'), ('штрих', 'noun'), ('штука', 'noun'), ('штурм', 'noun'), ('штуф', 'noun'), ('шуба', 'noun'), ('шубка', 'noun'), ('шуга', 'noun'), ('шугай', 'noun'), ('шугай', 'noun'), ('шудра', 'noun'), ('шукач', 'noun'), ('шулер', 'noun'), ('шулий', 'adjective'), ('шулик', 'noun'), ('шуляк', 'noun'), ('шум', 'noun'), ('шумко', 'adverb'), ('шумно', 'adverb'), ('шумок', 'noun'), ('шунт', 'noun'), ('шурин', 'noun'), ('шурпа', 'noun'), ('шуруп', 'noun'), ('шурф', 'noun'), ('шуряк', 'noun'), ('шуст', 'noun'), ('шутий', 'adjective'), ('шуфля', 'noun'), ('шушун', 'noun'), ('шхери', 'noun'), ('шхуна', 'noun'), ('щасні', 'noun'), ('щасно', 'adverb'), ('щастя', 'noun'), ('ще', 'adverb'), ('щебет', 'noun'), ('щем', 'noun'), ('щемно', 'adverb'), ('щеня', 'noun'), ('щепа', 'noun'), ('щерба', 'noun'), ('щигля', 'noun'), ('щипак', 'noun'), ('щипок', 'noun'), ('щипці', 'noun'), ('щир', 'noun'), ('щирий', 'adjective'), ('щит', 'noun'), ('щиток', 'noun'), ('щі', 'noun'), ('щіпка', 'noun'), ('щітка', 'noun'), ('щіть', 'noun'), ('щічка', 'noun'), ('щогла', 'noun'), ('щодва', 'adverb'), ('щодві', 'adverb'), ('щодня', 'adverb'), ('щока', 'noun'), ('щоніч', 'adverb'), ('щораз', 'adverb'), ('щорік', 'adverb'), ('щотри', 'adverb'), ('щука', 'noun'), ('щуп', 'noun'), ('щупак', 'noun'), ('щупик', 'noun'), ('щупля', 'noun'), ('щур', 'noun'), ('щурик', 'noun'), ('щурка', 'noun'), ('щуря', 'noun'), ('щучий', 'adjective'), ('щучин', 'adjective'), ('щучка', 'noun')]
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
                    if (line[:2] == "/n" or line[0] == "n" or line[:4] == "noun"):
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
    #results()
    print(get_words("base.lst", ['і', 'щ', 'ш', 'ь', 'у']))
