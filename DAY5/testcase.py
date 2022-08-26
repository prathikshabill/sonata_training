import unittest
from agetest import agecalculator


class AgeTest(unittest.TestCase):
    def testAge(self):
        self.assertEqual(agecalculator(32), (68,2090))

    def testAge1(self):
        self.assertEqual(agecalculator(10), (90,2112))

    def testAge2(self):
        self.assertEqual(agecalculator(10.4), (89.6,2111.6))

    def testAge3(self):
        self.assertEqual(agecalculator('PRAT'),None)


    @classmethod
    def setUpClass(self):
        print("TEST START")

    @classmethod
    def tearDownClass(self):
        print("TEST END")
