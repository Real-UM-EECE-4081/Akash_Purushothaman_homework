from util import F_to_C
from util import C_to_F
import unittest

class unitTest(unittest.TestCase):

    def testF(self):
        temp = F_to_C(30)
        self.assertEqual(temp,0,"Wrong")

    def testBelowZeroF(self):
        temp = F_to_C(-500)
        self.assertEqual(temp,0,"Wrong")

    def testC(self):
        temp = C_to_F(30)
        self.assertEqual(temp,0,"Wrong")

    def testBelowZeroC(self):
        temp = C_to_F(-500)
        self.assertEqual(temp,0,"Wrong")
