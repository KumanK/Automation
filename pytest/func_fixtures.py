'''
runs every time when referenced from test function
'''
import pytest

@pytest.fixture(scope="function")
def inp():
    print "Ran fixture"
    return True

def test_1(inp):
    assert inp == True

def test_2(inp):
    assert inp == True
