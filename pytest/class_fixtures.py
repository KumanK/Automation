'''
fixtures executes once per object creations. So all the methods in class gets same state of fixture applied
'''
import pytest
import random

@pytest.fixture(scope="class")
def rand_data(request):
    print "Fixture executed...."
    request.cls.num = random.randint(1,3)

@pytest.mark.usefixtures("rand_data")
class TestRandInts():
    def test_dummy_1(self):
        assert self.num == 1
    def test_dummy_2(self):
        assert self.num == 2

@pytest.mark.usefixtures("rand_data")
class TestRandInts_1():
    def test_dummy_1(self):
        assert self.num == 2
    def test_dummy_2(self):
        assert self.num == 3