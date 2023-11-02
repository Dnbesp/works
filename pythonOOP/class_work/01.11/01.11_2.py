from abc import ABC, abstractmethod


class IOutput(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def display(self):
        pass


class ConsonOutput(IOutput):
    def display(self):
        print(f"{self.data}")


class FileOutput(IOutput):
    def display(self):
        with open('output.txt', 'w') as f:
            f.write(self.data)


obj = ConsonOutput("some string")
obj.display()
obj_to_file = FileOutput("some string")
obj_to_file.display()