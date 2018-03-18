import unittest

class MockRandom:
    def __init__(self, seed):
        self.seed = seed

    def randrange(self, *_):
        return self.seed

class RandomBoardTestCase(unittest.TestCase):
    def test_imperative_shell(self):
        from chesskata import shell as system_under_test
        self.sut_satisfies_specification(system_under_test)

    def test_core_random_pieces(self):
        from chesskata import core as system_under_test
        self.sut_satisfies_core_examples(system_under_test)

    def sut_satisfies_core_examples(self, system_under_test):
        self.example_matches(system_under_test, 0, "BBRKRQNN")
        self.example_matches(system_under_test, 1, "BRBKRQNN")

    def example_matches(self, system_under_test, seed, expected):
        pieces = system_under_test.random_pieces(MockRandom(seed))
        self.assertEqual(pieces, expected)

    def test_core_exhausted_properties(self):
        from chesskata import core as system_under_test
        self.sut_satisfies_exhausted_properties(system_under_test)

    def sut_satisfies_exhausted_properties(self, system_under_test):
        variations = set()
        for seed in range(0,960):
            pieces = system_under_test.random_pieces(MockRandom(seed))
            self.pieces_satisfy_specification(pieces)
            variations.add(pieces)

        self.assertEqual(len(variations), 960)

    def test_core_with_samples(self):
        from chesskata import core as system_under_test
        self.sut_satisfies_samples(system_under_test)

    def sut_satisfies_samples(self, system_under_test):
        import random
        variations = set()
        samples_to_check = 2
        for seed in random.sample(range(0,960), samples_to_check):
            pieces = system_under_test.random_pieces(MockRandom(seed))
            self.pieces_satisfy_specification(pieces)
            variations.add(pieces)
        self.assertEqual(len(variations), samples_to_check)

    def test_random_board(self):
        from chesskata import board as system_under_test
        self.sut_satisfies_specification(system_under_test)

    def sut_satisfies_specification(self, system_under_test):
        pieces = system_under_test.random_pieces()
        self.pieces_satisfy_specification(pieces)

    def pieces_satisfy_specification(self, pieces):
        self.pieces_are_truthy(pieces)
        self.has_all_pieces(pieces)
        self.has_bishops_on_opposite_colors(pieces)
        self.has_king_between_rooks(pieces)

    def pieces_are_truthy(self, pieces):
        """The order of the pieces on the home rank should be truthy"""
        self.assertTrue(pieces, "Pieces should be truthy")

    def has_all_pieces(self, pieces):
        # https://stackoverflow.com/a/15046263/54734
        actual = self.anagram(pieces)
        expected = self.anagram("RNBQKBNR")
        self.match_anagrams(actual, expected)

    def match_anagrams(self, actual, expected):
        self.assertEqual(actual, expected)

    def anagram(self, pieces):
        return ''.join(sorted(pieces))

    def has_bishops_on_opposite_colors(self, pieces):
        """Another way of spelling that the bishops are
        on opposite colors: the second bishop should be
        an odd number of files away from the first"""
        first_position = pieces.find("B")
        second_position = pieces.rfind("B")
        self.check_opposite_colors(first_position, second_position)

    def check_opposite_colors(self, first_position, second_position):
        distance = second_position - first_position
        self.assertEqual(distance % 2, 1)

    def has_king_between_rooks(self, pieces):
        first_rook = pieces.find("R")
        second_rook = pieces.rfind("R")
        NOT_FOUND = -1
        king_at = pieces.find("K", first_rook, second_rook)
        self.assertNotEqual(king_at, NOT_FOUND)



if __name__ == '__main__':
    unittest.main()
