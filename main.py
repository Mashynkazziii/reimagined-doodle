BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book({self.id!r}, {self.name!r}, {self.pages!r})"


if __name__ == "__main__":
    # Инициализация списка книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Проверка метода __str__
    for book in list_books:
        print(book)

    # Проверка метода __repr__
    print(list_books)
