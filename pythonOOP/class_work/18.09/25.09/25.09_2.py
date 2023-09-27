class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'<<{self.first_name} {self.last_name}>>'

    def print_info(self):
        print("--"*10)
        print(f'{self.first_name[0]}. {self.last_name}', end=' ')
        print(self.school)

class Test:
    def info(self):
        print(f"test = {self.__class__.__name__}!!!")
class Student(Person, Test):
    def __init__(self, first_name, last_name, school):
        super().__init__(first_name, last_name) # виклик init супер-класу
        self.school = school # додавання нового атрибуту для об'єкту

    def __str__(self):
        return f'<<{self.first_name} {self.last_name} {self.school}>>'

    def print_info(self):
        super().info()
        print(self.school)

s = Student("Jon", "Smith", "#3")
print(s)

mro = [x.__name__ for x in Student.__mro__]
s.print_info()
print(Student.__mro__)



