from utils import percentage_calculateor, is_palindroom

def test_percentage_calculator():
    assert percentage_calculateor(20,10) == 2
    assert percentage_calculateor(0,100) == 0
    assert percentage_calculateor(5,0) == 0

def test_is_palindrome():
    assert is_palindroom("madam")
    assert is_palindroom("racecar")
    assert not is_palindroom("Good Morning")
