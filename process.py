from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, double_to_single
from wordlist import WordList

import itertools
import os
import multiprocessing as mp

ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'

import itertools
assert len(list(itertools.product(ALPHABET, repeat=5)))==33554432

wordlist = WordList(lower=True, strip_nonalpha=True)

# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/archive/master.zip

for filename in ['de', 'en', 'es', 'fr', 'it', 'nl', 'pt', 'ru']: # 'ja', 'zh'
    fn = os.path.join('dictionaries/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words-master', filename)
    wordlist.add_file(fn, min=3, transforms=[
        lambda x: vowel_expand(x, 5),
        lambda x: drop_vowel(x),
        lambda x: l33t(x),
        lambda x: words_with_ck(x)
    ])

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
