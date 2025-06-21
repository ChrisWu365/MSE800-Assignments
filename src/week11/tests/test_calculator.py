'''
Activity Week 11-2: Develop a Unit Testing Plan
Develop a unit testing plan for the following project: a command-line engineering calculator that includes the four basic arithmetic operations, power, root, and trigonometric functions (sine, cosine, and tangent). 
'''
import pytest
from mypackage.calculator import add, subtract, multiply, divide, power, root, sine, cosine, tangent

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_power():
    assert power(2, 2) == 4
    assert power(2, 3) == 8

def test_root():
    assert root(8, 3) == 2
    assert root(4, 2) == 2

def test_root_by_zero():
    with pytest.raises(ValueError, match="Cannot take the root with an exponent of zero"):
        root(8, 0)

def test_sine():
    assert sine(90) == 1
    assert sine(180) == pytest.approx(0)

def test_cosine():
    assert cosine(0) == 1
    assert cosine(90) == pytest.approx(0)

def test_tangent():
    assert tangent(0) == pytest.approx(0)
    assert tangent(45) == pytest.approx(1)

def test_tangent_by_invalid_degrees():
    # Python treats \+ as an invalid escape sequence in a string, use a raw string(r"") for the regex pattern or escape the backslash properly
    error_message = r"Tangent of angles 90 \+ n\*180 is undefined"
    with pytest.raises(ValueError, match=error_message):
        tangent(90)
    with pytest.raises(ValueError, match=error_message):
        tangent(90 + 180)
    with pytest.raises(ValueError, match=error_message):
        tangent(90 + 180 * 2)