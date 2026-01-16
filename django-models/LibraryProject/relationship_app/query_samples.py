import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return "Author not found"


# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return "Library not found"


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned to this library"


# Example usage (Optional testing)
if __name__ == "__main__":
    print("Books by Author:")
    print(get_books_by_author("John Doe"))

    print("\nBooks in Library:")
    print(get_books_in_library("Central Library"))

    print("\nLibrarian for Library:")
    print(get_librarian_for_library("Central Library"))
