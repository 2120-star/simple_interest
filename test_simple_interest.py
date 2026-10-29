
from simple_interest import simple_interest


def test_simple_interest():
    assert simple_interest(10000, 5, 2) == 1000


def test_zero_principal():
    assert simple_interest(0, 5, 2) == 0


def test_zero_rate():
    assert simple_interest(10000, 0, 2) == 0
