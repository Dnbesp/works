# Дескриптори - удосконалення                           Беспятий Дмитро
import string
import re


class UserName:

    def __init__(self, min_length=0, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    # •	Username може містити цифри, символ підкреслення _ або мінус -, а також букви, але не починатись з цифри,
    # з _ або -.  Його довжина має міститься у заданих межах min_length та mах_length включаючи, що задається при
    # ініціалізації дескриптора.
    # •	first_name, last_name – може містити тільки букви.
    def __set__(self, instance, value):
        if self.var == "_username":
            pun = ['True' for i in value if i in string.punctuation]
            pun = ' '.join(map(str, pun))
            if value[0].isalpha() and value[0] != '_' and value[0] != '-' and pun != 'True':
                if self.min_length <= len(value) <= self.max_length:
                    setattr(instance, self.var, value)
                else:
                    raise AttributeError("Error! Len 'username' does not meet the requirements")
            else:
                raise AttributeError("Error! 'username' does not meet the requirements")
        if self.var == "_first_name" or self.var == "_last_name":
            if value.isalpha():
                setattr(instance, self.var, value)
            else:
                raise AttributeError(f"Error! '{value}' does not meet the requirements")

    def __set_name__(self, owner, name):
        var_name = '_' + name
        self.var = var_name

    def __delete__(self, instance):
        print(f'Delete: {instance}')


class Email:

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    # Email має відповідати формату електронної пошти (можна скористатись регулярним виразом і модулем re.
    def __set__(self, instance, value):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, value) is not None:
            setattr(instance, self.var, value)
        else:
            raise AttributeError(f"Error! 'email' does not meet the requirements")

    def __set_name__(self, owner, name):
        var_name = '_' + name
        self.var = var_name

    def __delete__(self, instance):
        print(f'Delete: {instance}')


class Password:

    def __init__(self, min_length=0, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    def __get__(self, instance, owner):
        return getattr(instance, self.var)

    # Password задовольняє всі умови як у username, але також містить спеціальні символи.
    def __set__(self, instance, value):
        if self.var == "_password":
            if value[0].isalpha() and value[0] != '_' and value[0] != '-':
                if self.min_length <= len(value) <= self.max_length:
                    setattr(instance, self.var, value)
                else:
                    raise AttributeError("Error! Len 'password' does not meet the requirements")
            else:
                raise AttributeError("Error! 'password' does not meet the requirements")

    def __set_name__(self, owner, name):
        var_name = '_' + name
        self.var = var_name

    def __delete__(self, instance):
        print(f'Delete: {instance}')


# Реалізувати функціонал, щоб при створенні нових об'єктів типу User, email був унікальним, тобто, щоб не можна було
# створити у програмі 2 об'єкта з тим самим значенням email.
class User:

    username = UserName(2, 7)
    first_name = UserName()
    last_name = UserName()
    email = Email()
    password = Password(5, 10)
    mail = []

    def __init__(self, username, first_name, last_name, email, password):
        self._last_name = None
        if email not in User.mail:
            self.username = username
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password
            User.mail.append(email)
        else:
            raise AttributeError(f"Error! there is a user with such an email")


d = User("Ed", "Edvard", 'Toms', "ed@gmail.com", 'a2389')
m = User("Ed", "Edvard", 'Toms', "qed@gmail.com", 'a2389')
print(d.__dict__)
d.first_name = 'Erik'
print(d.first_name)
del d._last_name
print(d.__dict__)
print(d.mail)
