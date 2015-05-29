import itertools
from wordlist import WordList
import os
import multiprocessing as mp

ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'

wordlist = WordList(lower=True, strip_nonalpha=True)

# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/archive/master.zip

for filename in ['de', 'en', 'es', 'fr', 'it', 'nl', 'pt', 'ru']: # 'ja', 'zh'
    fn = os.path.join('dictionaries/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words-master', filename)
    wordlist.add_file(fn, min=3)

# http://wordlist.sourceforge.net/12dicts-readme-r5.html
# http://downloads.sourceforge.net/project/wordlist/12Dicts/5.0/12dicts-5.0.zip
# for filename in ['2of12inf.txt', '5desk.txt', '2of4brif.txt', '2of12.txt', '6of12.txt', '3esl.txt']:
for filename in ['6of12.txt', '5desk.txt', '3esl.txt', '2of4brif.txt']:
    fn = os.path.join('dictionaries/12dicts-5.0', filename)
    wordlist.add_file(fn, min=3)

wordlist.add_file('dictionaries/12dicts-5.0/neol2007.txt', split_further=',')
#
# http://icon.shef.ac.uk/Moby/mlang.html
# http://www.dcs.shef.ac.uk/research/ilash/Moby/mlang.tar.Z
# for filename in ['french.txt', 'german.txt', 'italian.txt', 'japanese.txt', 'spanish.txt']:
#     fn = os.path.join('dictionaries/mlang', filename)
#     wordlist.add_file(fn, min=4)


def generate_guids(words, combinations=None, min_length, max_length):
    guids = set()

    if not combinations:
        pass

    if isinstance(words, list):
        words = [words]

    for word in words:
        if min_length < len(word) < max_length:
            positions = n_positions(word, max_length)
            n_random = max_length - len(word)
            for c in combinations[n_random]:
                for i in range(0, positions):
                    word_list = create_word_list(word, i)
                    available_indices = [i for i, x in enumerate(word_list) if not x]
                    for idx in available_indices:
                        index = available_indices.index(idx)
                        word_list[idx] = c[index]
                    result = ''.join(word_list)
                    guids.add(result)
        elif len(word) == max_length:
            guids.add(word)
    return guids


def process(word, combos, alphabet=ALPHABET):
    def n_positions(word, n):
        return n - len(word) + 1

    def create_word_list(word, index):
        word_list = [None] * 5

        for letter in word:
            word_list[index] = letter
            index += 1
        return word_list

    results = set()
    for w in [word]:
        positions = n_positions(w, 5)
        n_random = 5 - len(w)
        if n_random > 0 and n_random < 5:
            for c in list(itertools.product(alphabet, repeat=n_random)):
                for i in range(0, positions):
                    word_list = create_word_list(w, i)
                    available_indices = [i for i, x in enumerate(word_list) if not x]
                    for idx in available_indices:
                        for letter in c:
                            word_list[idx] = letter
                            continue
                    result = ''.join(word_list)
                    if result not in results:
                        results.add(result)
        elif n_random == 0:
            if w not in results:
                results.add(w)
    return results