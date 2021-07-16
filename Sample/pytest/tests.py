from sample import func

def test_answer():
    assert func(3) == 4

def test1():
    assert func(3) == 3
    
def test2():
    assert func(3) == 3
# $ py.test sample.py