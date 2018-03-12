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

    def pieces_are_truthy(self, pieces):
        """The order of the pieces on the home rank should be truthy"""
        self.assertTrue(pieces, "Pieces should be truthy")


if __name__ == '__main__':
    unittest.main()
