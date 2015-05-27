from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, double_to_single
from wordlist import wordlist
import itertools

ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'
BLACKLIST = wordlist.words


def main():
    blacklist = set(generate_blacklist(BLACKLIST))
    blacklist_guids = generate_guids(list(blacklist))


def generate_blacklist(blacklist):
    result = []
    result += blacklist
    print('Generating blacklist...')
    n = 0
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


def generate_guids(blacklist):
    blacklist_guids = set()
    n = 0
    n_guid = 0
    total = len(blacklist)
    for word in blacklist:
        if 2 < len(word) <= 5:
            n += 1
            print('Processing word {0}/{1}'.format(n, total))
            positions = n_positions(word, 5)
            n_random = 5 - len(word)
            combinations = list(itertools.product(ALPHABET, repeat=n_random))

            for c in combinations:
                for i in range(0, positions):
                    word_list = create_word_list(word, i)
                    available_indices = [i for i, x in enumerate(word_list) if not x]
                    for idx in available_indices:
                        for letter in c:
                            word_list[idx] = letter
                            continue
                    result = ''.join(word_list)
                    blacklist_guids.add(result)
                    print(len(blacklist_guids))
                    n_guid += 1
    return blacklist_guids


def create_word_list(word, index):
    word_list = [None] * 5

    for letter in word:
        word_list[index] = letter
        index += 1
    return word_list


def put(word, guid, i):
    return guid[0:i] + word + guid[len(word) + i:]


def n_positions(word, n):
    return n - len(word) + 1


if __name__ == '__main__':
    main()