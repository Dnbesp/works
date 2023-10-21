import pytest
from main import addition
from myclass import Person


@pytest.fixture
def create_obj():
    return Person("Jon", 18)


def test_addition():
    assert addition(5, 5) == 10
    assert addition(4, 5) == 9
    assert addition(8, 1) == 1


@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 10),
    (4, 5, 9),
    (0, 1, 1),
])
def test_param_addition(a, b, expected):
    assert addition(a, b) == expected





# if __name__ == "__main__":
#     unittest.maipip
