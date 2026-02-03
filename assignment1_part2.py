class Book:
    """
    Represents a book with an author and a title.
    """
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        """
        Prints a string representing the book in the format 'title, written by author'.
        """
        print(f"{self.title}, written by {self.author}")

# Instantiate two objects from the Book class
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Print both of these objects to the screen by calling their display() functions
print("Displaying book details:")
book1.display()
book2.display()
