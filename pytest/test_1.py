import random
import pytest

@pytest.fixture(scope="function")
def input():
    print 'running code'
    return random.random()
def test_me(input):
    assert True == input
def test_urself(input):
    assert True == input

