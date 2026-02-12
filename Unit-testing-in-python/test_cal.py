# naming convention to put up test as the file name

import unittest
import cal

# creating testcases for those test cases
# we can do that by creating class

# inheriting gives us lot of testing capabilities.
class TestCal(unittest.TestCase):

    # naming convention is required!
    def test_add(self):

        result = cal.add(10, 5)
        self.assertEqual(result, 15)

# or you can do this.....
if __name__ == '__main__': #
    unittest.main()