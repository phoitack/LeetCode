from angleBtwClockHands import *
import unittest

class TestAngleClock(unittest.TestCase):

    def test_clock_angle(self):

        self.assertAlmostEqual(angleClock(3, 15), 7.5)
        self.assertAlmostEqual(angleClock(4, 50), 155)
        self.assertAlmostEqual(angleClock(12, 0), 0)
        self.assertAlmostEqual(angleClock(3, 30), 75)
        self.assertAlmostEqual(angleClock(1, 57), 76.5)
        