"""
(incomplete) Tests for BookList class
"""
from booklist import BookList
from book import Book

# test empty BookList
book_list = BookList()
if len(book_list.booklists) == 0:
    print("Empty Books")
else:
    print("There are {} books".format(len(book_list.booklists)))
# assert len(book_list.books) == 0

# test loading books
book_list.load_books('books.csv')
if len(book_list.booklists) > 0:
    print("There are {} books".format(len(book_list.booklists)))
else:
    print("No books")
# assert len(book_list.books) > 0  # assuming CSV file is not empty
result = book_list.counting_required_pages()
print(result)

result2 = book_list.counting_completed_pages()
print(result2)

# test sorting books
# book_list.sort_books()

# test adding a new Book
# book_list.add_book("Code Complete","Steve McConnell",960)

# test saving books (check CSV file manually to see results)
book_list.save_books('books.csv')