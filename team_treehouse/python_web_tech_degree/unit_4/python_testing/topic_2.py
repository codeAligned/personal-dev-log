# ============= Part 2 =============

# Task 1 of 2
# The get_anagrams() function takes one or more words and returns anagrams for each of them as a list. Finish the test_in_anagrams() test to check that the anagrams for the string "treehouse" contains the word "house".

import unittest

from string_fun import get_anagrams


class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn("house",get_anagrams("treehouse"))

# Task 2 of 2
# Conversely, we shouldn't see the word "code" in the list of anagrams for "treehouse". Add a new test named test_not_in_anagrams and use self.assertNotIn() to make sure "code" isn't in the anagrams for "treehouse".

import unittest

from string_fun import get_anagrams


class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn("house",get_anagrams("treehouse"))

    def test_not_in_anagrams(self):
        self.assertNotIn("code",get_anagrams("treehouse"))