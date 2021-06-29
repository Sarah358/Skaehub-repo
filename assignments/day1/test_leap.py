# import modules

import unittest
from unittest import result
import leap

class TestLeap(unittest.TestCase):
    # function to test leap year

    def test_leap_year(self):
        y = 2020
        result = leap.leap_year(y)
        self.assertTrue(result,True)
        # not leap year

    def test_not_leap_year(self):
        x = 2018
        result = leap.leap_year(x)
        self.assertFalse(result,False) 
        # check for a number that is not an year   
    def test_is_integer(self):
        z = 200
        result = leap.leap_year(z)
        self.assertFalse(result,False)    

if __name__ == '__main__':
    unittest.main()        





