import stringCalc1

def test_stringCalc1():
    assert stringCalc1.str_calc("10 *20") == 200

def test_datatype():
    assert type(stringCalc1.str_calc("1/4")) == float