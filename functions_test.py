import pytest
from functions import add, minus

#test case for add function
def test_add():
    result = add(2 , 3)
    assert result == 5
    
def test_minus():
    result = minus(5, 2)
    assert result == 3
    
    
