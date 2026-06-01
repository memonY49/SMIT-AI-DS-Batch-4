## Problem Statement: Library Management System

# ### System Requirements

# 1. Create a decorator named `track_action` that:

#    * Prints a message whenever a function starts and ends.
#    * Saves all activity logs into a file named `library_logs.txt`.

# 2. Create a base class named `Book` with:

#    * Attributes:
#      * `title`
#      * `author`
#      * `pages`

# 3. Create a derived class named `EBook` that inherits from `Book`.
#    * Add an additional attribute:
#      * `file_size`

# 4. Implement the following methods:

#    * `borrow_book()`
#    * `return_book()`

#    Apply the decorator to both methods.

# 5. Implement the following magic methods:

#    * `__str__()` → display book details in a readable format.
#    * `__len__()` → return the total number of pages in the book.
#    * `__add__(other)` → return the combined pages of two books.

# 6. Implement file handling:

#    * Create a file named `books_record.txt`.
#    * Save book borrowing and return records into the file using append mode.

# 7. In the main program:

#    * Create multiple book and ebook objects.
#    * Borrow and return books.
#    * Demonstrate all magic methods.
#    * Read and display contents of both files.

from datetime import datetime as dt


def track_action(func):
    def wrapper(*args,**kwargs):
        log = f"{dt.now()} {func.__name__} is called.\n"
        print(log)
        with open("logs.txt", "a") as file:
            file.write(log)
        return func(*args,**kwargs)
    return wrapper


class Book:
    def __init__(self,title:str,author:str,pages:int):
        self.title = title
        self.author = author
        self.pages = pages

class EBook(Book):
    def __init__(self, file_size:float,**kwargs):
        super().__init__(**kwargs)
        self.file_size = file_size

class library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_ebooks = []
        self.borrow_list = []

    @track_action
    def add_book(self,book:object, type:str):
        if type.lower() == "ebook":
            self.list_of_ebooks.append(book)
        elif type.lower() == "book":
            self.list_of_books.append(book)

    @track_action
    def borrow(self,title:str,type:str):
        if type.lower() == "ebook":
            for ebook in self.list_of_ebooks:
                if ebook.title == title:
                    self.list_of_ebooks.remove(ebook)
                    self.borrow_list.append({"book":ebook,"type":"ebook"})
                    self.add_record(ebook,"Borrow")
                    return ebook
        elif type.lower() == "book":
            for book in self.list_of_books:
                if book.title == title:
                    self.list_of_books.remove(book)
                    self.borrow_list.append({"book":book,"type":"book"})
                    self.add_record(book,"Borrow")
                    return book
        return None
    
    @track_action
    def return_book(self,book,type:str):
        self.add_book(book,type)
        self.add_record(book,"Returned")
        self.borrow_list.remove({"book":book,"type":type})

    @track_action
    def add_record(self,book,act):
        with open("record.txt","a") as file:
            file.write(f"{dt.now()} {book.title} ({act})\n")

b1 = Book("Atitude is everything","Jeff Keller",100)
eb1 = EBook(file_size=25.5,title="Atitude is everything",author = "Jeff Keller",pages = 100)

list_book = library()
list_book.add_book(b1,"Book")
list_book.add_book(eb1,"ebook")

borrowbook = list_book.borrow("Atitude is everything","book")
list_book.return_book(borrowbook,"book")