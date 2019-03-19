import unittest
from code.multiply import multiply

class multiplyTestCase(unittest.TestCase):

    def testone(self):
        self.assertNotEqual(multiply(2,2),6)

if __name__ == '__main__':
    unittest.main()
