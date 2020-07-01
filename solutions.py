import unittest
import calculate


class Calculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate.add(5, 10), 15)

    def test_subtract(self):
        self.assertEqual(calculate.subtract(10, 5), 5)
