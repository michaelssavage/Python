import unittest
from code.testy.add import add

class AddTestCase(unittest.TestCase):

    def testing_simple(self):
        self.assertTrue(add(2,3),5)

    def testing_two(self):
        self.assertEqual(add(2,2),4)
        
    def testing_devil(self):
        self.assertAlmostEqual(add(3.33333333,3.66666666),7)

if __name__ == '__main__':
    unittest.main()
