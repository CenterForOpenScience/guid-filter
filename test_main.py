from main import generate_guids, generate_69s, n_positions, get_combinations
import unittest

combinations = get_combinations(3)


class TestMain(unittest.TestCase):
    def test_n_positions(self):
        n = n_positions('word', 5)
        self.assertEquals(n, 2)

    def test_generate_guids(self):
        guids = generate_guids(['test'], combinations=combinations, length=5)
        self.assertEquals(len(guids), 64)

    def test_generate_guids_returns_five_character_words(self):
        guids = generate_guids(['tests'])
        self.assertEquals(len(guids), 1)

    def test_generate_guids_does_not_process_words_over_length_max(self):
        with self.assertRaises(Exception):
            guids = generate_guids(['testing'])
            self.assertEquals(len(guids), 0)

    def test_generate_69(self):
        bad_guids_69 = generate_69s(combinations)
        self.assertNotIn('12697', bad_guids_69)
        self.assertIn('69aaa', bad_guids_69)
        self.assertIn('a69aa', bad_guids_69)
        self.assertIn('aaa69', bad_guids_69)
        self.assertIn('a69a3', bad_guids_69)
        self.assertIn('69bad', bad_guids_69)



