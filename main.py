import datetime
import json
import os

class Base:
    def __init__(self):
        self.id = id(self)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def append_to_file(filename, obj_dict):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
        else:
            data = []
        
        data.append(obj_dict)
        
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


class Book(Base): 
    def __init__(self, title, author, year, genre, isBorrowed=False):
        super().__init__()
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isBorrowed = isBorrowed
        
        Base.append_to_file("books.json", self.to_dict())
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'isBorrowed': self.isBorrowed
        })
        return data


class User(Base):
    def __init__(self, name):
        super().__init__()
        self.name = name

        Base.append_to_file("users.json", self.to_dict())
    
    def borrow_book(self, book):
        if not book.isBorrowed:
            book.isBorrowed = True
            print(f"{self.name} borrowed '{book.title}'")
            # Update book file to reflect borrowing
            Base.append_to_file("books.json", book.to_dict())
        else:
            print(f"Sorry, '{book.title}' is not available")
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name
        })
        return data

book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")