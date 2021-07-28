import stringCalc

def test_string_add():
    assert stringCalc.string_add("10+30") == 40

def test_string_substract():
    assert stringCalc.string_substract("30-10") == 20

def test_string_multiply():
    assert stringCalc.string_multiply("30*0") == 0

def test_string_division():
    assert stringCalc.string_division("30/5") == 6