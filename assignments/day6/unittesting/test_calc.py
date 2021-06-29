# import unittest and the module we are testing

import unittest
import calc


# craete a class and inherit from unit test

class TestCalc(unittest.TestCase):
    # create a method with test_
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)


# using main to run the function
if __name__ == '__main__':
    unittest.main()

