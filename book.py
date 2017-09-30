# create your simple Book class in this file
class Book:
    def __init__(self,title="",author="",pages=0,status=""):
        """To construct the Book class"""
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status

    def __str__(self):
        """To return the message on the book object"""
        return "{} by {}, total pages is {}.".format(self.title, self.author, self.pages)

    def mark_completed(self,status):
        """Mark the book as completed when clicking the button(interpreted in the main.py)"""
        if status == "r":
            self.status = "c"#It is to test the mark complete function in the test_book.py, otherwise this program works fine in the main.py
            return True
        elif status == "c":
            return False

    def long_pages(self,pages):
        """Method to determine whether the book is long or not"""
        if int(pages) > 500:
            return True  #It is to determine the button color, which will be interpreted in the main.py
        else:
            return False