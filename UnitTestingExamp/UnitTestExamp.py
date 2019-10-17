import unittest
import pytest
from UnitTestingExamp.Example_1 import Examples


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("start before all..")

    @classmethod
    def tearDownClass(cls):
        print("start after all..")

    def setUp(self):
        print("Start Before Method")

    def tearDown(self):
        print("Start After Method")

    def test_add(self):
        result = Examples.addition(self,10,20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = Examples.subtraction(self,30,20)
        self.assertEqual(result, 10)


# if __name__ == '__main__':
#     unittest.main()
