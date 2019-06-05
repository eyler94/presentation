import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
import dice

class TestDiceFunction(unittest.TestCase):

    def test_rolling(self):
        for iter in range(100):
            result = dice.roll(20)
            self.assertLessEqual(result,20)
            self.assertGreater(result,0)
        self.assertEqual(dice.roll(0),'Please enter an integer greater than 0.')
        self.assertEqual(dice.roll(-1),'Please enter an integer greater than 0.')
        self.assertEqual(dice.roll('foo'),'Please enter an integer.')
        self.assertEqual(dice.roll(1.5),'Please enter an integer.')

if __name__ == '__main__':
    unittest.main()
