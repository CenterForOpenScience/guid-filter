from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, repeat_to_single, drop_suffixes
from wordlist import WordList
import itertools
import os
import re

ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'

assert len(list(itertools.product(ALPHABET, repeat=5))) == 33554432

wordlist = WordList(lower=True, strip_nonalpha=True)

def not_in_alphabet(word, alphabet=ALPHABET):
    if re.findall('[^{}]'.format(alphabet), word):
        return True
    return False

# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/archive/master.zip

for filename in ['de', 'en', 'es', 'fr', 'it', 'nl', 'pt', 'ru', 'custom.txt']: # 'ja', 'zh'
    fn = os.path.join('dictionaries/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words-master', filename)
    wordlist.add_file(fn, min=3, max=10, reject=[not_in_alphabet], transforms=[
        lambda x: vowel_expand(x, 5) if len(x) < 5 else [],
        lambda x: drop_vowel(x),
        lambda x: l33t(x) if 3 <= len(x) <= 5 else [],
        lambda x: words_with_ck(x),
        lambda x: repeat_to_single(x),
        lambda x: drop_suffixes(x)
    ])

# http://wordlist.sourceforge.net/12dicts-readme-r5.html
# http://downloads.sourceforge.net/project/wordlist/12Dicts/5.0/12dicts-5.0.zip
# for filename in ['2of12inf.txt', '5desk.txt', '2of4brif.txt', '2of12.txt', '6of12.txt', '3esl.txt']:
for filename in ['6of12.txt', '5desk.txt', '3esl.txt', '2of4brif.txt']:
    fn = os.path.join('dictionaries/12dicts-5.0', filename)
    wordlist.add_file(fn, min=3, max=5)

wordlist.add_file('dictionaries/12dicts-5.0/neol2007.txt', min=3, max=5, split_further=',')

# http://icon.shef.ac.uk/Moby/mlang.html
# http://www.dcs.shef.ac.uk/research/ilash/Moby/mlang.tar.Z
# for filename in ['french.txt', 'german.txt', 'italian.txt', 'japanese.txt', 'spanish.txt']:
#     fn = os.path.join('dictionaries/mlang', filename)
#     wordlist.add_file(fn, min=4)
