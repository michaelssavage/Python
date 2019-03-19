import unittest
from code.add import add

class testAddCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(add(2,4),2*3)

if __name__ == '__main__':
    unittest.main()
