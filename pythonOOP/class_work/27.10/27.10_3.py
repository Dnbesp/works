class Singleton:
    _instance = None

    def __str__(self):
        return "SQL"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.do_work()
        return cls._instance

    @classmethod
    def do_work(self):
        print("Init connect to Database {self}")

sing_1 = Singleton()
sing_2 = Singleton()
print(sing_1 is sing_2)