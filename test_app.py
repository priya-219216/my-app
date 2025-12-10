from app import add_numbers
import pytest
from calculator import multiply, divide

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5

def test_divide_success():
    assert divide(10, 2) == 5

def test_divide_zero_error():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_numbers():
    assert add_numbers(2, 3) == 5
