# Вступ до метакласів                               Беспятий Дмитро

# class Student:
#
# team = "Python31"
# __slots__ = ['name', 'age', 'gender']

def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

def greet(self):
    print("Hi, my name is", self.name)

def description(self):
    print(f"Person <{self.name}, {self.age}, {self.gender}>")


Student = type("Student", (), {'team': "Python31", 'name': "Erik", 'age': 35, 'gender': "men",
                               'greet': greet, 'description': description})


s = Student()
print(type(Student))
s.greet()
s.description()
Student.study = 'python'
print(Student.study)
print(Student.__dict__)