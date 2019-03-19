import unittest
from code.add import add

class AddTestCase(unittest.TestCase):

    def test_one(self):
        self.assertNotEqual(add(1,1),3)
		
    def test_two(self):
        self.assertEqual(add(1,2),3)
                        
    def test_three(self):
        self.assertEqual(add(-1,-3),-2*2)
        
    def test_string(self):
        self.assertEqual(add("hel","lo"),"hello")
              
if __name__ == '__main__':
    unittest.main()
