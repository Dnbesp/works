class User:

    username = UserName()
    first_name = UserName()
    last_name = UserName()
    email = Email()
    password = Password()

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __set_name__(self, owner, name):
