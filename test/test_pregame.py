import unittest

class PregameTestCase(unittest.TestCase):
    def testAlwaysPass(self):
        pass

    def testAssertedPass(self):
        assert True

    @unittest.skip("demonstrate how skips are reported")
    def testAlwaysSkipThisTest(self):
        assert False

    @unittest.expectedFailure
    def testExpectToFail(self):
        assert False