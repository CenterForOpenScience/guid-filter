from process import wordlist
import itertools
import time
import os
ALPHABET = '23456789abcdefghjkmnpqrstuvwxyz'


def main():
    blacklist_all = wordlist.dict_by_length()
    blacklist = blacklist_all[3].union(blacklist_all[4]).union(blacklist_all[5])
    combinations = get_combinations(2)
    tick = time.time()
    bad_guids = generate_guids(blacklist, combinations=combinations)
    print('Time: {}, Length: {}'.format(time.time()-tick, len(bad_guids)))
    with open('guid_blacklist.txt', 'w') as writer:
        for item in bad_guids:
            writer.write(item + os.linesep)


def get_combinations(length, alphabet=ALPHABET):
    combinations = {}
    for x in range(length):
        combinations[x + 1] = list(itertools.product(alphabet, repeat=(x+1)))
    return combinations


def generate_guids(words, combinations=None, length=5, alphabet=ALPHABET):
    guids = set()

    if not combinations:
        combinations = get_combinations(2, alphabet)

    n = 0
    for word in words:
        if n % 1000 == 0:
            print(str(n))
        if len(word) > length:
            raise Exception
        if len(word) == length:
            guids.add(word)
        else:
            positions = n_positions(word, length)
            n_random = length - len(word)
            for c in combinations[n_random]:
                for i in range(0, positions):
                    word_list = create_word_list(word, i)
                    available_indices = [i for i, x in enumerate(word_list) if not x]
                    for idx in available_indices:
                        index = available_indices.index(idx)
                        word_list[idx] = c[index]
                    result = ''.join(word_list)
                    guids.add(result)
        n += 1
    return guids


def create_word_list(word, index):
    word_list = [None] * 5

    for letter in word:
        word_list[index] = letter
        index += 1
    return word_list


def n_positions(word, length):
    return length - len(word) + 1


if __name__ == '__main__':
    main()

