import unittest
from code.multiply import multiply

class MulTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(multiply(4,4),16)
              
if __name__ == '__main__':
    unittest.main()
