import unittest

def add(a, b):
    return a + b

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 5), 8)
