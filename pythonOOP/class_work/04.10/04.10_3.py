def get_count(self):
    print("Call")
    return self.count


MyClass = type("MyClass", (), {"username": 'admin', "count": 10, "info": get_count})

# class MyClass:
#     pass

obj = MyClass()
print(MyClass.username)
print(obj.info())

print(type(obj).__name__)
print(type(MyClass).__name__)
