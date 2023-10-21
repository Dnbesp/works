def get_data():
    return [12, 11, 10]

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def get_year(self):
        return 2023 - self.age

    def check_name(self):
        return len(self.name) > 3

    def process_data(self):
        data = get_data()
        return sum(data) / len(data)