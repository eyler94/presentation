import <ModuleToTest>
#https://docs.pytest.org/en/latest/

# To run tests, first install using:
#
# $sudo apt-install python<3>-pytest
#
# Then, either use:
#
# $py.test test_<ModuleToTest>.py -v
# or if it is the only test in that directory (or any sub directories), use
# $py.test -v

def test_<FunctionToTest>():
    assert <ModuleToTest>.<FunctionToTest>(inputs) == ExpectedResult

def test_<FunctionToTest>():
    assert <ModuleToTest>.<FunctionToTest>(inputs) == ExpectedResult

    #...

def test_<FunctionToTest>():
    assert <ModuleToTest>.<FunctionToTest>(inputs) == ExpectedResult
