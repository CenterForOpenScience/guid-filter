from collections import defaultdict
import itertools
import os
import re
import unicodedata

class WordList(object):
    def __init__(self, lower=False, strip_nonalpha=False):
        self._lower = lower
        self._strip_nonalpha = strip_nonalpha
        self.words = set()
        self._table = []
        self.sets = defaultdict

    def add_words(self, words):
        count_added = 0
        for word in words:
            count_added += self._add_word(word)
        print('Words added: {0}, Total: {1}'.format(count_added, len(self.words)))
        return count_added

    def _add_word(self, word):
        if word not in self.words:
            self.words.add(word)
            return 1
        return 0

    def add_file(self, filename, split_further=None):
        count_total = 0
        count_added = 0
        with open(filename, 'U', encoding='iso-8859-15') as f: # can also try cp437 (so:16528468)
            try:
                for row in f:
                    if split_further is None:
                        words = [row]
                    else:
                        words = row.split(split_further)

                    for word in words:

                        word = word.strip('\n').strip('\r')
                        if self._lower:
                            word = word.lower()
                        word = unicodedata.normalize('NFKD', word).encode('ascii','ignore').decode("utf-8")
                        if self._strip_nonalpha:
                            word = re.sub('[^a-zA-Z]', '', word)
                        number_words_added = self._add_word(word)
                        count_added += number_words_added
                        count_total += number_words_added
            except:
                print('Error')
        print('Words added: {0}, Total: {1}'.format(count_added, len(self.words)))
        self._table.append({
            'filename':filename,
            'words_in_file':count_total
        })

    def dict_by_length(self):
        out = defaultdict(set)
        for word in self.words:
            out[len(word)].add(word)
        return out


def put(word, guid, i):
    return guid[0:i] + word + guid[len(word) + i:]


def n_positions(word, n):
    return n - len(word) + 1


wordlist = WordList(lower=True, strip_nonalpha=True)

# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
# https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/archive/master.zip

for filename in ['de', 'en', 'es', 'fr', 'it', 'nl', 'pt', 'ru']: # 'ja', 'zh'
    fn = os.path.join('dictionaries/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words-master', filename)
    wordlist.add_file(fn)

# http://wordlist.sourceforge.net/12dicts-readme-r5.html
# http://downloads.sourceforge.net/project/wordlist/12Dicts/5.0/12dicts-5.0.zip
for filename in ['2of12inf.txt', '5desk.txt', '2of4brif.txt', '2of12.txt', '6of12.txt', '3esl.txt']:
    fn = os.path.join('dictionaries/12dicts-5.0', filename)
    wordlist.add_file(fn)

wordlist.add_file('dictionaries/12dicts-5.0/neol2007.txt', split_further=',')

# http://icon.shef.ac.uk/Moby/mlang.html
# http://www.dcs.shef.ac.uk/research/ilash/Moby/mlang.tar.Z
for filename in ['french.txt', 'german.txt', 'italian.txt', 'japanese.txt', 'spanish.txt']:
    fn = os.path.join('dictionaries/mlang', filename)
    wordlist.add_file(fn)
