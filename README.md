# presentation
Collection of short scripts used for a presentation on unit testing.

_________________________________________________________
********************Python testing********************
_________________________________________________________

To run the pytest module,use the following command:

$pytest <test_ModuleName.py> <-v>

For example:

$pytest test_dice.py -v

If the filename is omitted, then all tests that can be found will be run.
The -v is only necessary if you want more information on the tests. (V for verbose.)

To run the unittest module, use the following command:

$python<3> test_ModuleName.py <-v>

For example:

$python3 test_dice.py -v

Unittest runs with python3 and python.... If you are unfortunate enough to still be using python2... I'm sorry... haha, jk.

_________________________________________________________
********************C++ testing********************
_________________________________________________________

Ensure your CMakelists.txt is setup correctly (I followed an introductory example at https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu/.)

After editing your file, run make, and then run the executable.

$./ModuleName

For example:

$make
$./TestDice
