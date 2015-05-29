from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, double_to_single
from wordlist import wordlist
import itertools
from functools import partial
from multiprocessing import pool
import csv
import time
ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'
BLACKLIST = wordlist.words


def main():
    tick = time.time()
    blacklist = set(generate_blacklist(BLACKLIST, min_length=2, max_length=5))
    print(time.time()-tick)
    print(len(blacklist))

    tick = time.time()
    bad_guids = process_guids(list(blacklist))
    print(time.time()-tick)
    return bad_guids


def generate_blacklist(blacklist, min_length, max_length):
    result = [w for w in blacklist if min_length < len(w) <= max_length]
    print('Generating blacklist...')
    n = 1
    total = len(blacklist)
    for word in blacklist:
        print('Processing word {0}/{1}'.format(n, total))
        n += 1
        if len(word) <= max_length:
            result += vowel_expand(word, 3)
            result += words_with_ck(word)
            result += l33t(word)
        result += drop_vowel(word)
        result += double_to_single(word)
    return result


def get_combinations(length):
    combinations = {}
    for x in range(length):
        combinations[x + 1] = list(itertools.product(ALPHABET, repeat=(x+1)))
    return combinations


def generate_guids(full_blacklist, combinations, min_length, max_length):
    with open('blacklist.csv', 'w') as blacklist_csv:
        writer = csv.writer(blacklist_csv)
        blacklist_guids = set()

        if type(full_blacklist) != list:
            full_blacklist = [full_blacklist]

        for word in full_blacklist:
            if min_length < len(word) < max_length:
                print(word)
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
                        blacklist_guids.add(result)
                        writer.writerow([result])
                        print(len(blacklist_guids), result)
            elif len(word) == max_length:
                blacklist_guids.add(word)
                writer.writerow([word])
                print(len(blacklist_guids), word)
        return blacklist_guids


def process_guids(data, n=4):
    p = pool.Pool(processes=n)
    c = get_combinations(2)
    map_func = partial(generate_guids, combinations=c)
    results = p.map(map_func, data)
    p.close()

    total = set()
    for r in results:
        total = total.union(r)
    print(len(total))
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

