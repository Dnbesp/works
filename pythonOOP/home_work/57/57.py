class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name):
        print(f"Call __getattr__{name}")


book = Book("Python Programming", "John Zelle")
print(book.__dict__)
# print(book.title, book.author)
print("----------")
print("book.title=", book.title)
print("book.author=", book.author)
