import pytest

def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3
#     assert add('space', 'ship') == 'spaceship'



# def add(a, b):
#     return a + b


# def test_add():
#     assert pytest.approx(add(0.1, 0.2), 0.3)
