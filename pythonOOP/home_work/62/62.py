# pytest                                        Беспятий Дмитро
import pytest
from name import Vector
import math


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
    assert obj_vector != obj_vector_2


# 2. Реалізувати метод __add__ і __sub__
def test_create_obj__add__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert obj_vector.x + obj_vector_2.x == 7


def test_create_obj__sub__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert obj_vector.y - obj_vector_2.y == -9


# 3. Реалізувати методи __iadd__ і __isub__
def test_create_obj__iadd__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert obj_vector.z + obj_vector_2.z == 6.6


def test_create_obj__isub__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert obj_vector.x - obj_vector_2.x == -3


# 4.5. Реалізувати метод __mul__, передбачити множення вектора v на a
def test_create_obj__mul__(create_obj, create_obj_2):
    obj_vector = create_obj
    obj_vector_2 = create_obj_2
    assert (obj_vector.x * 2) + (obj_vector.y * 2) + (obj_vector.z * 2) == 19.2
    assert (obj_vector.x * obj_vector_2.x) + (obj_vector.y * obj_vector_2.y) + (obj_vector.z * obj_vector_2.z) == 55.2


# 6. Реалізувати метод __len__, передбачити множення вектора v на a
def test_create_obj__len__(create_obj):
    obj_vector = create_obj
    assert abs(obj_vector.x) + abs(obj_vector.y) + abs(obj_vector.z) == 9.6


# 7. Реалізувати метод __int__, що повертатиме цілу частину довжини вектора
def test_create_obj__int__(create_obj):
    obj_vector = create_obj
    assert int(abs(obj_vector.x) + abs(obj_vector.y) + abs(obj_vector.z)) == 9


# 8. Реалізувати метод __neq__, що повертатиме для вектора v протилежний вектор
def test_create_obj__neq__(create_obj):
    obj_vector = create_obj
    assert -obj_vector.x == -2
    assert -obj_vector.y == -3
    assert -obj_vector.z == -4.6


# 9. Реалізувати метод __getitem__ і __setitem__, що дозволяють достукатись до координат
def test_create_obj__getitem__(create_obj):
    obj_vector = create_obj
    assert [obj_vector.x, obj_vector.y, obj_vector.z]
    assert obj_vector[0] == 2


def test_create_obj__setitem__(create_obj):
    obj_vector = create_obj
    assert [obj_vector.x, obj_vector.y, obj_vector.z]
    assert obj_vector[-1] == 4.6


# 10. Реалізувати метод __contains__
def test_create_obj__contains__(create_obj):
    obj_vector = create_obj
    assert [obj_vector.x, obj_vector.y, obj_vector.z]
    assert 3 in obj_vector


# 11. Реалізувати метод __bool__
def test_create_obj__bool__(create_obj):
    obj_vector = create_obj
    assert abs(obj_vector.x) + abs(obj_vector.y) + abs(obj_vector.z) != 0

# 12 Зробіть об'єкти класу Vector функторами за допомогою __call__
def test_create_obj__call__(create_obj):
    create_obj = "Hello"
    assert f'{create_obj}' == "Hello"