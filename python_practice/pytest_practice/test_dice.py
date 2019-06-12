import dice

def test_range():
    # Test several rolls to make sure the result is in the proper bound.
    for iter in range(100):
        result = dice.roll(20)
        assert result <= 20
        assert result > 0

def test_value():
    # Make sure it rejects a zero sided die.
    assert dice.roll(0) == 'Please enter an integer greater than 0.'
    # Make sure it rejects a negative number of sides.
    assert dice.roll(-1) == 'Please enter an integer greater than 0.'

def test_type():
    # Make sure it rejects non-number inputs.
    assert dice.roll('foo') == 'Please enter an integer.'
    # Make sure it rejects non-integer inputs.
    assert dice.roll(1.5) == 'Please enter an integer.'
