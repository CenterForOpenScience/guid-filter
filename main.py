from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, double_to_single
from wordlist import wordlist
import itertools
from functools import partial
from multiprocessing import pool
from multiprocessing.context import Process
ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'
BLACKLIST = wordlist.words


def main():
    blacklist = set(generate_blacklist(BLACKLIST))
    bad_guids = process_guids(blacklist)
    return bad_guids


def generate_blacklist(blacklist):
    result = []
    result += blacklist
    print('Generating blacklist...')
    n = 1
    total = len(blacklist)
    for word in blacklist:
        print('Processing word {0}/{1}'.format(n, total))
        n += 1
        result += vowel_expand(word, 3)
        result += drop_vowel(word)
        result += words_with_ck(word)
        result += l33t(word)
        result += double_to_single(word)
    return result


def get_combinations(length):
    combinations = {}
    for x in range(length):
        combinations[x + 1] = list(itertools.product(ALPHABET, repeat=(x+1)))
    return combinations


def generate_guids(full_blacklist, combinations):
    blacklist_guids = set()

    if type(full_blacklist) != list:
        full_blacklist = [full_blacklist]

    for word in full_blacklist:
        if 2 < len(word) < 5:
            positions = n_positions(word, 5)
            n_random = 5 - len(word)
            for c in combinations[n_random]:
                for i in range(0, positions):
                    word_list = create_word_list(word, i)
                    available_indices = [i for i, x in enumerate(word_list) if not x]
                    for idx in available_indices:
                        index = available_indices.index(idx)
                        word_list[idx] = c[index]
                    result = ''.join(word_list)
                    blacklist_guids.add(result)
                    print(len(blacklist_guids), result)
        elif len(word) == 5:
            blacklist_guids.add(word)
            print(len(blacklist_guids), word)
    return blacklist_guids


def process_guids(data, n=4):
    p = pool.Pool(processes=n)
    c = get_combinations(2)
    map_func = partial(generate_guids, combinations=c)
    results = p.map(generate_guids, data)
    p.close()

    total = set()
    for r in results:
        total = total.union(r)
    return total


def create_word_list(word, index):
    word_list = [None] * 5

    for letter in word:
        word_list[index] = letter
        index += 1
    return word_list


def n_positions(word, n):
    return n - len(word) + 1


if __name__ == '__main__':
    main()

