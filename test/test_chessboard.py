import unittest

from chesskata import board

class RandomBoardTestCase(unittest.TestCase):
    def test_random_board(self):
        system_under_test = board
        self.sut_satisifies_specification(system_under_test)

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
