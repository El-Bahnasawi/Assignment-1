from func import *

def test_factorial():
    result = factorial(3)
    assert result == 6
    result = factorial(4)
    assert result == 24
