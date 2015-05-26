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
                    word_list = list(word)
                    repeat_number = max_size-len(word)
                    word_list.insert(position, character*repeat_number)
                    result = ''.join(word_list)
                    results.append(result)
    return results
