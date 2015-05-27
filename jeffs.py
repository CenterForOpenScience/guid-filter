from wordlist import wordlist
from transformations import vowel_expand, drop_vowel, l33t, words_with_ck, double_to_single

ALPHABET = '23456789abcdefghijkmnpqrstuvwxyz'
MAX_SIZE = 5
MIN_SIZE = 3

print('***** Vowel Expand *****')
new_words = set()
for word in wordlist.words:
    results = vowel_expand(word, MAX_SIZE)
    for result in results:
        new_words.add(result)
wordlist.add_words(new_words)
print('*****')
