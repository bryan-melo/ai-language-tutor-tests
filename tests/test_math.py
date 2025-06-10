import pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2 
    

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
    

@pytest.mark.math
def test_divide_by_zero(): 
   with pytest.raises(ZeroDivisionError) as e:
      num = 1 / 0 # This test is intentionally failing to demonstrate the testing framework
   
   assert 'division by zero' in str(e.value)  # Check if the exception message contains 'division by zero'

# Multiplication test ideas:
# two positive integers
# identity: multiply by 1
# zero: multiply by 0
# positive by negative
# negative by negative
# floats 
products = [ 
   (2, 3, 6), 
   (1, 99, 99), 
   (0, 99, 0), 
   (3, -4, -12), 
   (-5, -5, 25), 
   (2.5, 6.7, 16.75)
]


@pytest.mark.math
@pytest.mark.parametrize("a, b, product", products)
def test_multiplication(a, b, product):
   assert a * b == product