"""
(incomplete) Tests for Book class
"""
from book import Book

# test empty book (defaults)
book = Book()
print(book)
assert book.author == ""
assert book.title == ""
assert book.pages == 0

# test initial-value book
book2 = Book("Fish fingers", "Dory", 2, 'r')
# test mark_completed()
book2.mark_completed(book2.status)
if book2.status == "c":
    print(book2,"(completed)")
elif book2.status == "r":
    print(book2)