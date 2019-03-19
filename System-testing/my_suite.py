import unittest

from test_add import AddTestCase
from test_is_prime import PrimesTestCase
from test_sub import SubTestCase
from test_mul import MulTestCase


def my_suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(AddTestCase))
    suite.addTest(unittest.makeSuite(PrimesTestCase))
    suite.addTest(unittest.makeSuite(SubTestCase))
    suite.addTest(unittest.makeSuite(MulTestCase))


    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
