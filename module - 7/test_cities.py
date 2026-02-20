# Daniel Fryer
# Assignment 7
# 2/20/26

import unittest
from city_functions import DisplayCityCountry

class DisplayNamesTest(unittest.TestCase):

    def testCityCountry(self):
        formattedName = DisplayCityCountry('Santiago', 'Chile')
        self.assertEqual(formattedName, 'Santiago, Chile')



if __name__ == '__main__':
    unittest.main()