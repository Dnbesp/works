# pytest                                        Беспятий Дмитро
import pytest
from name import Vector
from name import __eq__


@pytest.fixture
def create_obj():
    return Vector(2, 3, 4.6)

@pytest.fixture
def create_obj_2():
    return Vector(5, 12, 2)

def test_create_obj(create_obj):
    obj_vector = create_obj
    assert obj_vector.x == 2
    assert obj_vector.y == 3
    assert obj_vector.z == 4.6

def test_create_obj_2(create_obj_2):
    obj_vector = create_obj_2
    assert obj_vector.x == 5
    assert obj_vector.y == 12
    assert obj_vector.z == 2

# 1. Порівняння двох векторів за рівністю їх координат
def test_create_obj__eq__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert __eq__(obj_vector, obj_vector_2) == False


