import unittest

from dutchish import sentence_to_dutchish, word_to_dutchish


class DutchishTests(unittest.TestCase):
    def test_possessive_curly_apostrophe(self):
        self.assertEqual(word_to_dutchish("ministry’s"), "minustriez")

    def test_possessive_straight_apostrophe(self):
        self.assertEqual(word_to_dutchish("ministry's"), "minustriez")

    def test_sentence_preserves_punctuation_around_possessive(self):
        self.assertEqual(
            sentence_to_dutchish("The ministry’s office."),
            "Du minustriez ofis.",
        )

    def test_capitalized_word_stays_capitalized(self):
        self.assertEqual(word_to_dutchish("Ministry’s"), "Minustriez")

    def test_uppercase_word_stays_uppercase(self):
        self.assertEqual(word_to_dutchish("NASA"), "NESU")

    def test_single_letter_i_is_not_treated_as_acronym(self):
        self.assertEqual(word_to_dutchish("I"), "Ai")

    def test_common_contraction_straight_apostrophe(self):
        self.assertEqual(word_to_dutchish("Isn't"), "Izunt")

    def test_common_contraction_curly_apostrophe(self):
        self.assertEqual(word_to_dutchish("isn’t"), "izunt")

    def test_sentence_with_contraction_and_i(self):
        self.assertEqual(
            sentence_to_dutchish("Isn't it true that I am here?"),
            "Izunt it troe det Ai em hier?",
        )


if __name__ == "__main__":
    unittest.main()
