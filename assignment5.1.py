# PARENT CLASS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return "Book borrowed!"
        return "Already borrowed!"

    # Polymorphism
    def get_type(self):
        return "General Book"

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# CHILD CLASS ( from Book)
class TextBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author) 
        self.subject = subject 

    # OVERRIDING the get_type method 
    def get_type(self):
        return "Textbook"


# Testing the classes
if __name__ == "__main__":
    print("=== GENERAL BOOK ===")
    novel = Book("Things Fall Apart", "Chinua Achebe")
    print(novel)
    print("Type:", novel.get_type())
    print(novel.borrow())

    print("\n=== TEXTBOOK (Inheritance & Polymorphism) ===")
    math_book = TextBook("Basic Calculus", "Dr. Math", "Mathematics")
    print(math_book)
    print("Type:", math_book.get_type())  # Different output 
    print("Subject:", math_book.subject)  # New attribute 
    print(math_book.borrow())  # Inherited method