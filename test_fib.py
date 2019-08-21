from fib import *

def test_fib0():
    obs = fib(0)
    assert obs == 1

def test_fib1():
    obs = fib(1)
    assert obs == 1

def test_fibn():
    obs = fib(2)
    assert obs == 2

    
