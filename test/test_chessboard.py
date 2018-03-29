import unittest

class MockRandom:
    def __init__(self, seed):
        self.seed = seed

    def randrange(self, *_):
        return self.seed

class RandomBoardTestCase(unittest.TestCase):
    def test_different_seeds_give_different_boards(self):
        from chesskata import core as system_under_test
        self.sut_different_seeds_give_different_boards(system_under_test)

    def sut_different_seeds_give_different_boards(self, system_under_test):
        import random
        samples = set()
        for seed in random.sample(range(0,960), 2):
            pieces = system_under_test.random_pieces(MockRandom(seed))
            samples.add(pieces)

        self.assertEqual(len(samples), 2)

    def test_all_seeds_give_different_boards(self):
        from chesskata import core as system_under_test
        self.sut_all_seeds_give_different_boards(system_under_test)

    def sut_all_seeds_give_different_boards(self, system_under_test):
        samples = set()
        for seed in range(0,960):
            pieces = system_under_test.random_pieces(MockRandom(seed))
            samples.add(pieces)
        self.assertEqual(len(samples), 960)

    def test_core_with_examples(self):
        from chesskata import core as system_under_test
        self.sut_matches_all_examples(system_under_test)

    def sut_matches_all_examples(self, system_under_test):
        self.sut_matches_example(system_under_test, 0, "BBRKRQNN")
        self.sut_matches_example(system_under_test, 1, "RBBKRQNN")
        self.sut_matches_example(system_under_test, 2, "RBKRBQNN")
        self.sut_matches_example(system_under_test, 3, "RBKRQNBN")
        self.sut_matches_example(system_under_test, 4, "BRKBRQNN")

        self.sut_matches_example(system_under_test, 15, "RKRQNNBB")
        self.sut_matches_example(system_under_test, 16, "BBRKQRNN")

        self.sut_matches_example(system_under_test, 319, "QNNRKRBB")
        self.sut_matches_example(system_under_test, 320, "BBRKRNQN")
        self.sut_matches_example(system_under_test, 640, "BBRKRNNQ")
        self.sut_matches_example(system_under_test, 959, "NNQRKRBB")

    def sut_matches_example(self, system_under_test, seed, expected_pieces):
        pieces = system_under_test.random_pieces(MockRandom(seed))
        self.assertEqual(pieces, expected_pieces)
        
    def test_imperative_shell(self):
        from chesskata import shell as system_under_test
        self.sut_satisifies_specification(system_under_test)
        
    def test_random_board(self):
        from chesskata import board as system_under_test
        self.sut_satisifies_specification(system_under_test)

    def test_functional_core_all_seeds(self):
        from chesskata import core as system_under_test
        self.sut_satisifies_specification_for_all_seeds(system_under_test)

    def sut_satisifies_specification_for_all_seeds(self, system_under_test):
        for seed in range(0,960):
            pieces = system_under_test.random_pieces(MockRandom(seed))
            self.pieces_satisfy_specification(pieces)

    def sut_satisifies_specification(self, system_under_test):
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
        self.check_opposite_colors(first_position, second_position, pieces)

    def check_opposite_colors(self, first_position, second_position, pieces):
        distance = second_position - first_position
        self.assertEqual(distance % 2, 1, "Bishops are on the same color: " + pieces)

    def has_king_between_rooks(self, pieces):
        first_rook = pieces.find("R")
        second_rook = pieces.rfind("R")
        NOT_FOUND = -1
        king_at = pieces.find("K", first_rook, second_rook)
        self.assertNotEqual(king_at, NOT_FOUND)



if __name__ == '__main__':
    unittest.main()
