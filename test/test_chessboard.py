import unittest

from chesskata import board

class MyTestCase(unittest.TestCase):
    def test_random_board(self):
        actual = board.random_pieces()

        """The order of the pieces on the home rank should be truthy"""
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
