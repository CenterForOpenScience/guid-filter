import unittest
from transformations import drop_vowel, words_with_ck, repeat_to_single, vowel_expand, get_matched_letters_indices, l33t


class MyTestCase(unittest.TestCase):

    def test_drop_one_vowel(self):
        bad_words = drop_vowel('duck')
        expected = ['duck', 'dck']
        self.assertEquals(expected, bad_words)

    def test_drop_multiple_vowels(self):
        bad_words = drop_vowel('saman')
        expected = ['saman', 'samn', 'sman', 'smn']
        self.assertEquals(expected, bad_words)
    
    def test_drop_vowel_minimum(self):
        bad_words = drop_vowel('bad')
        expected = ['bad']
        self.assertEquals(expected, bad_words)
    
    def test_words_with_ck(self):
        bad_words = words_with_ck('duck')
        expected = ['duck', 'duc', 'ducc', 'duk', 'dukk']
        self.assertEquals(expected, bad_words)
    
    def test_l33t(self):
        bad_words = l33t('bad')
        expected = ['bad', 'b4d']
        self.assertEquals(expected, bad_words)
    
    def test_get_matched_letter_indices(self):
        indices = get_matched_letters_indices('saman', 'aeiou')
        expected = [(1, 'a'), (3, 'a')]
        self.assertEquals(indices, expected)

    def test_double_to_single(self):
        bad_words = repeat_to_single('coffee')
        self.assertIn('coffee', bad_words)
        self.assertIn('coffe', bad_words)
        self.assertIn('cofee', bad_words)
        self.assertIn('cofe', bad_words)

    def test_repeat_to_single(self):
        bad_words = repeat_to_single('hhhi')
        self.assertIn('hhhi', bad_words)
        self.assertIn('hhi', bad_words)
        self.assertIn('hi', bad_words)

    def test_multiple_repeats_to_single(self):
        bad_words = repeat_to_single('hhff')
        self.assertIn('hhff', bad_words)
        self.assertIn('hff', bad_words)
        self.assertIn('hhf', bad_words)


if __name__ == '__main__':
    unittest.main()
