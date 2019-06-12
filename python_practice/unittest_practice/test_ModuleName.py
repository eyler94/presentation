import unittest
# https://docs.python.org/3/library/unittest.html#unittest.TestCase
import <ModuleToTest>

# To run, simply enter that directory and use the following command:
# $python<3> test_ModuleName.py -v

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
