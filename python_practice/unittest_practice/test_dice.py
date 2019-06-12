import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
import dice

class TestDiceFunction(unittest.TestCase):

    def test_range(self):
        # Test several rolls to make sure the result is in the proper bound.
        for iter in range(100):
            result = dice.roll(20)
            self.assertLessEqual(result,20)
            self.assertGreater(result,0)

    def test_value(self):
        # Make sure it rejects a zero sided die.
        self.assertEqual(dice.roll(0),'Please enter an integer greater than 0.')
        # Make sure it rejects a negative number of sides.
        self.assertEqual(dice.roll(-1),'Please enter an integer greater than 0.')

    def test_type(self):
        # Make sure it rejects non-number inputs.
        self.assertEqual(dice.roll('foo'),'Please enter an integer.')
        # Make sure it rejects non-integer inputs.
        self.assertEqual(dice.roll(1.5),'Please enter an integer.')

if __name__ == '__main__':
    unittest.main()
