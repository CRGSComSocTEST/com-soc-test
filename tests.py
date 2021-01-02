import unittest
import maths

class testAdd(unittest.TestCase):

    def test_add(self):
        self.assertTrue(maths.add(1, 2) == 3)

    def test_subtract(self):
        self.assertTrue(maths.sub(2, 1) == 1)

unittest.main()