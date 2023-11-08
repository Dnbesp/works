permissions = ["user", "admin"]

def required(permission):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if permission in permissions:
                func(*args, **kwargs)
            else:
                raise ValueError(f"Нема доступу для користувача {permission}")
            return
        return wrapper
    return decorate



@required(permission = "jon")
def data():
    print("secret data")

data()