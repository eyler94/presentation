import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
import <ModuleToTest>

class <DescriptiveTestName>(unittest.TestCase):

    def test_<FunctionToTest>(self):
        self.assert<something>()

    def test_<FunctionToTest>(self):
        self.assert<something>()

        #...

    def test_<FunctionToTest>(self):
        self.assert<something>()

if __name__ == '__main__':
    unittest.main()
