class Vector:

    """Class Vector"""

    def __init__(self, x, y, z):
        if isinstance(x and y and z, (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError(f"Введені знаячення не є числового типу")

    def __str__(self):
        return f'{__class__.__name__}({self.x},{self.y},{self.z})'

    # 1. Порівняння двох векторів за рівністю їх координат
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    # 2. Реалізувати метод __add__ і __sub__
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    # 3. Реалізувати методи __iadd__ і __isub__
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return Vector(self.x, self.y, self.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return Vector(self.x, self.y, self.z)

    # 4.5. Реалізувати метод __mul__, передбачити множення вектора v на a
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = (self.x * other) + (self.y * other) + (self.z + other)
            return result
        elif isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            new_z = self.z * other.z
            result = new_x + new_y + new_z
            return result

    # 6. Реалізувати метод __mul__, передбачити множення вектора v на a
    def __len__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    # 7. Реалізувати метод __int__, що повертатиме цілу частину довжини вектора
    def __int__(self):
        return int(abs(self.x) + abs(self.y) + abs(self.z))

    # 8. Реалізувати метод __neq__, що повертатиме для вектора v протилежний вектор
    def __neg__(self):
        return -self.x, -self.y, -self.z

    # 9. Реалізувати метод __getitem__ і __setitem__, що дозволяють достукатись до координат
    def __getitem__(self, index):
        s = [self.x, self.y, self.z]
        return s[index]

    def __setitem__(self, index, value):
        if index == 0 or index == -3:
            self.x = value
        elif index == 1 or index == -2:
            self.y = value
        elif index == 2 or index == -1:
            self.z = value
        else:
            print("index not found")

    # 10. Реалізувати метод __contains__
    def __contains__(self, item):
        s = [self.x, self.y, self.z]
        if item in s:
            return True
        else:
            return False

    # 11. Реалізувати метод __bool__
    def __bool__(self):
        if abs(self.x) + abs(self.y) + abs(self.z) == 0:
            return False
        else:
            return True

    # 12 Зробіть об'єкти класу Vector функторами за допомогою __call__
    def __call__(self, messege):
        print(f'{__class__.__name__} = {messege}')


# vec = Vector(2, 3, 4.6)
# vec_2 = Vector(5, 12, 2)

#12
# vec("is long")
#11
# print(bool(vec_2))
# print(bool(vec))
#10
# print(5 in vec_2)
# print(1 in vec_2)
#9
# print(vec[1])
# print(vec_2[-1])
# print(*vec_2)
# vec[-1] = 5
# print(vec)
#8
# print(-vec)
# print(-vec_2)
#7
# print(int(vec))
# print(int(vec_2))
#6
# print(f"len vec = {len(vec)}")
# print(f"len vec_2 = {len(vec_2)}")
#5
# print(vec * 2)
#4
# print(vec * vec_2)
#3
# vec += vec_2
# print(vec)
# vec -= vec_2
# print(vec)
#2
# vec_3 = vec + vec_2
# print(vec_3)
# vec_3 = vec - vec_2
# print(vec_3)
#1
# print(vec.__eq__(vec_2))




