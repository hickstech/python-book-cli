# class describes some structure
class Book:
    favs = []

    @staticmethod
    def read_books_from_file():
        books = []
        try:
            with open("input.txt", "r") as file:
                data = file.read().split("\n")
                for book in data:
                    book_data = book.split("\t")
                    if book.strip():
                        books.append(Book(book_data[0], int(book_data[1])))
        except FileNotFoundError as e:
            print("Error FILENOTFOUND:", e)
        except Exception as e:
            print(f"Error reading file: {e}")
        finally:
            # using with auomatically closes the file, so we don't need to worry about it here
            # even if there is an exception
            pass
        return books

    @staticmethod
    def write_books_to_file(books):
        file = open("input.txt", "w")
        for book in books:
            file.write(f"{book.title}\t{book.pages}\n")
        file.close()

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

    __hash__ = None  # Disable hashing for mutable objects

    def is_short(self):
        return self.pages < 100
