# create your BookList class in this file
from book import Book
from operator import attrgetter

FILENAME = "books.csv"
class BookList():
    def __init__(self):
        """This function is to construct the class on BookList class"""
        booklists = []
        self.booklists = booklists

    def __getitem__(self, item):
        """This method is used for refrencing the booklists based on the index(as the booklists is a list of Book objects) in the main.py"""
        return self.booklists[item]

    def add_book(self,title,author,pages):
        """This function is for adding a Book object to the list of Book objects"""
        status = "r"
        book = Book(title,author,pages,status)
        self.booklists.append(book)
        return book

    def counting_required_pages(self):
    # """This function is for counting the required page in order to display the message for total required page"""
        required_booklists_pages = 0#initiate the total required booklist pages
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'r':#iterate the procedure based on the number of items in the booklists (len(self.booklists)) in the certain conditions(status in the Book object is completed)
                required_booklists_pages += (int(self.booklists[i].pages))#adding the pages based on the Book objects that is required
        required_page_result = "Total pages to read: {}".format(required_booklists_pages)
        return required_page_result

    def counting_completed_pages(self):
    # """This method is for counting the completed page in order to display the message for total completed page"""
        completed_booklists_pages = 0#initiate the total completed booklist pages
        for i in range(len(self.booklists)):
            if self.booklists[i].status == 'c':#iterate the procedure based on the number of items in the booklists (len(self.booklists)) in the certain conditions(status in the Book object is required)
                completed_booklists_pages += (int(self.booklists[i].pages))#adding the pages based on the Book objects that is completed
        completed_page_result = "Total pages completed: {}".format(completed_booklists_pages)
        return completed_page_result

    def load_books(self,filename=""):
        """This function is to load the book.csv file and then the contains will be interpreted in the list of Book objects"""
        file_pointer = open(filename, "r")
        for index,data in enumerate(file_pointer.readlines()):
            data = data.strip()
            datum = data.split(",")
            each_book = Book(datum[0],datum[1],datum[2],datum[3])#it is to create the Book object, which used Book() class that makes importing Book() class is useful
            self.booklists.append(each_book)
        file_pointer.close()
        return self.booklists

    def save_books(self,filename=""):
        """This function is to save the book list(contains book objects) to the book.csv file"""
        output_file = open(filename, "w")
        for book in range(len(self.booklists)):
            book = "{},{},{},{}\n".format(self.booklists[book].title,self.booklists[book].author,self.booklists[book].pages,self.booklists[book].status)
            output_file.write(book)#write the book object in the file books.csv for each line
        output_file.close()

    def sort_books(self):
        """This function is to sort the Book objects in a list based on the author and pages"""
        sort = self.booklists.sort(key=attrgetter('author','pages'))
        return sort

