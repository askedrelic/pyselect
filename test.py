
import pyselect
import unittest

class TestPyselect(unittest.TestCase):
    def test_it_works(self):
        self.assertEqual(1,2)
        self.assertEqual(pyselect.select('apples oranges bananas'.split()) == 'aplles')
