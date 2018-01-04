import unittest
#from unittest import TestCase

import generator


class TestGenerator(unittest.TestCase):

    def test_sample_single_word(self):
        l = ('foo', 'bar', 'foobar')
        word = generator.sample(l)
        assert word in l

    def test_sample_multiple_words(self):
        l = ('foo', 'bar', 'foobar')
        words = generator.sample(l, 2)
        assert len(words) == 2
        assert words[0] in l
        assert words[1] in l
        assert words[0] is not words[1]

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()
        assert len(phrase.split()) >= 5


if __name__ == '__main__':
    unittest.main()