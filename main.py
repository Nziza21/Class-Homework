class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isborrowed = False

class user:  
    def __init__(self, name):
        self.name = name

    def borrowing(self, book):
        if book.isborrowed:
            print(f"Sorry, '{book.title}' is currently unavailable")
        else:
            book.isborrowed = True
            print(f"Successfully borrowed, '{book.title}' by '{self.name}'")


my_book = Book("1984", "George Orwell", 1949, "Dystopian")
member = user("Alice")
member.borrowing(my_book)  
