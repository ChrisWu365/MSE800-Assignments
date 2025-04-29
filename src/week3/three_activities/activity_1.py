"""
Library Book Manager Using classes
Task: Manage a small library — add and show books.
"""
class Book:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.status = "Available"
        
class LibraryBookManager:
    def __init__(self, library_name):
        self.library_name = library_name
        # maintains a list of Book objects
        self.books = []

    def add_book(self, isbn, title):
        """
        invoke add_book to add a single book

        :param isbn: ISBN of the book
        :param title: title of the book
        """
        new_book = Book(isbn, title)
        self.books.append(new_book)
    
    def add_books(self, books):
        """
        invoke add_books to add a list of Book objects

        :param books: a list of Book objects
        """
        self.books.extend(books)

    def show_books(self, page_size, page_number, search_key_word):
        """
        invoke show_books to display books with pagination
        """
        results = []
        key_word = search_key_word.strip()
        # we can also search through books by a key word

        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        results = self.books[start_index: end_index]
        print(f"Page Size: {page_size}, Page Number: {page_number}")
        print("Index Title ISBN")
        for i, book in enumerate(results):
            print(f"{i + 1} {book.title} {book.isbn}")
        return results
    
# create a library
libraryBookManager = LibraryBookManager("Chris Library")

# add a book into the library
libraryBookManager.add_book("978-1787016064", "Lonely Planet New Zealand's South Island")

# create a list of book objects
book_list = [Book("978-0008609214", "The Lost Bookshop")
             , Book("978-1529146516", "The Diary of a CEO: The 33 Laws of Business and Life")
             , Book("978-1847941831", "Atomic Habits: Tiny Changes, Remarkable Results")]
# add a list of book objects into the library
libraryBookManager.add_books(book_list)

# display books with pagination 
libraryBookManager.show_books(2, 1, "")
print("")
libraryBookManager.show_books(10, 1, "")
