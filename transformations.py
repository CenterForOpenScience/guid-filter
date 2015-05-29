import itertools
import re


def vowel_expand(word, max_size, vowels=['a','e','i','o','u']):
    results = []
    found_list = list(re.finditer('['+''.join(vowels)+']', word))
    for combination in itertools.product(range(0,2), repeat=len(found_list)):
        if sum(combination) == 1:
            for i, do_process in enumerate(combination):
                if do_process:
                    position = found_list[i].span()[0]
                    character = found_list[i].group()
                    repeat_number = max_size-len(word)
                    for n in range(0, (repeat_number + 1)):
                        word_list = list(word)
                        word_list.insert(position, character*n)
                        result = ''.join(word_list)
                        results.append(result)
    return results


def drop_vowel(word, vowels='aeiou', minimum=3):
    result = []
    found_list = get_matched_letters_indices(word, vowels)

    # generate all possible combinations of vowel locations
    positions = list(itertools.product(range(0, 2), repeat=len(found_list)))
    for item in positions:
        word_list = list(word)
        for idx, value in enumerate(item):
            if value == 1:
                word_list[found_list[idx][0]] = ''

        final = ''.join(word_list)
        if len(final) >= minimum:
            result.append(final)

    return result


def l33t(word):
    result = []
    substitutions = {
        'e': '3',
        'a': '4',
        's': '5',
        't': '7'
    }
    found_list = get_matched_letters_indices(word, ''.join(substitutions.keys()))
    positions = list(itertools.product(range(0, 2), repeat=len(found_list)))
    for item in positions:
        word_list = list(word)
        for idx, value in enumerate(item):
            if value == 1:
                word_list[found_list[idx][0]] = substitutions[found_list[idx][1]]
        result.append(''.join(word_list))
    return result


def words_with_ck(word):
    result = []
    if 'ck' in word:
        result.append(word)
        substitutions = ['c', 'cc', 'k', 'kk', 'x', 'xx']
        for s in substitutions:
            new_word = word.replace('ck', s)
            result.append(new_word)
    return result


def repeat_to_single(word):
    word_list = list(word)
    repeats = []
    result = []
    for letter in word_list:
        if word_list.count(letter) > 1 and letter not in repeats:
            repeats.append(letter)
    found_indices = []
    for letter in repeats:
        repeat_indices = []
        for l in range(0, len(word_list)):
            if word_list[l] == letter:
                repeat_indices.append(l)
        found_indices.append(repeat_indices)

    positions = list(itertools.product(range(0, 2), repeat=len(found_indices)))
    for item in positions:
        word_list = list(word)
        for idx, value in enumerate(item):
            if value == 1:
                repeat_set = found_indices[idx]
                for r in repeat_set[1:]:
                    word_list[r] = ''
                    result.append(''.join(word_list))
            else:
                result.append(''.join(word_list))
    return result


def get_matched_letters_indices(word, letters):
    found_list = []
    for found in re.finditer('[' + letters + ']', word):
        match = (found.span()[0], found.group())
        found_list.append(match)
    return found_list


def drop_suffixes(word):
    result = []
    suffixes = ['ed', 'es', 's', 'y', 'ing']
    for s in suffixes:
        if word.endswith(s):
            result.append(word[0:len(word)-len(s)])
    return result