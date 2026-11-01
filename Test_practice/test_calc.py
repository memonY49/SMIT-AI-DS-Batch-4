import pytest
from calc import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(4, 3) == 7
    assert add(2, 2) == 4
    assert add(1, 3) == 4
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(4,2) == 2
    with pytest.raises(ValueError, match="divide by zero"):
        divide(10, 0)
    with pytest.raises(TypeError):
            divide("abc", 2)


def test_divide_with_error():
    with pytest.raises(Exception):
        divide("abc", 3)

def test_divide_by_zero_message():
    with pytest.raises(TypeError, match = "unsupported operand type(s) for /: 'str' and 'int'"):
        divide("abc", 3)

def test_aprox():
    assert 0.1 + 0.2000001 == 0.3