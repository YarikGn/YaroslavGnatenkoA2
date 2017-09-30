"""
Name: Yaroslav Gnatenko
Date: 29 September
Brief Project Description:
This project is the modified version on the Assignment 1 that is implemented on the app.kv file.
In terms of how the program works, the "Required Books" shows the buttons for the Required Books list and when the
button on the required book object is clicked, the button will mark the book as completed, which makes the button
disappeared and moved to the completed books button list. In terms of the how "Completed Books" works, the button on
the completed button object is clicked and show the description of the Book object(return value of the class).
On the other one, "Add Button" button occurs when the inputs in the text fields are reasonable, which shows the error
messages when the inputs in the text fields shows otherwise. In the "Clear" button, the button is used for clearing all
the inputs in the text fields.
GitHub URL: https://github.com/YarikGn/YaroslavGnatenkoA2
"""

from kivy.app import App
from kivy.app import Builder
from book import Book
from booklist import BookList
from kivy.uix.button import Button

class ReadingListApp(App):
    def __init__(self, **kwargs):
        """This function is to construct the class"""
        super(ReadingListApp, self).__init__(**kwargs)
        book_lists = BookList()#calling the BookList class
        book_object = Book()#calling the Book class
        self.book_lists = book_lists
        self.book_object = book_object
        self.book_lists.load_books("books.csv")#loading the book in order to get the list of the Book objects

    def on_start(self):
        """This function is used for initialise the program/when the user start to run the program"""
        #initialised state
        self.create_books(mode='required')
        self.root.ids.required_book_button.state = 'down'#state is to determine whether the button is on the pressed state or not
        self.root.ids.completed_book_button.state = 'normal'

    def create_books(self, mode):
        """This function is used for creating the book button in the entriesBox widget"""
        self.clear_books()

        if mode == "required":
            # creating the button based on the books that is required
            for book in range(len(self.book_lists.booklists)):
                if self.book_lists[book].status == 'r':
                    temp_button = Button(text=self.book_lists[book].title)#text that will be generated on the button
                    temp_button.bind(on_release=self.click_required_books)#binding the button to the function when clicked
                    page_check = self.book_object.long_pages(self.book_lists[book].pages)#to determine the background color for the button, which is by checking the book object pages
                    if page_check == True:#when page on the book object is more than 500(long)
                        temp_button.background_color = 0, 1, 1, 1#blue color when the book is long
                    else:
                        temp_button.background_color = 0.8, 0.8, 0, 1#yellow color when the book is short
                    self.root.ids.entriesBox.add_widget(temp_button)#adding the button in entriesBox widget
            total_required_pages = self.book_lists.counting_required_pages()#calling the method to display total required pages from the BookList() class
            self.root.ids.bookPages.text = total_required_pages #the variable on the method to call counting_required_pages() method, which is the returned value of the method
            self.root.ids.bookMsg.text = "Click book to mark them as completed"#Initialise the message when clicking "Required books"

        elif mode == "completed":
            #creating the button based on the books that is completed
            for book in range(len(self.book_lists.booklists)):
                if self.book_lists[book].status == 'c':
                    temp_button = Button(text=self.book_lists[book].title)
                    temp_button.bind(on_release=self.click_completed_books)
                    temp_button.background_color = 0.37,0.37,0.37,1
                    self.root.ids.entriesBox.add_widget(temp_button)
            total_completed_pages = self.book_lists.counting_completed_pages()
            self.root.ids.bookMsg.text = "Click book to show the description"#Initialise the message when clicking "Completed books"
            self.root.ids.bookPages.text = total_completed_pages

    def press_required_books(self):
        """the function runs when "Required books" is pressed"""
        self.create_books(mode='required')#to get the required book buttons
        self.root.ids.required_book_button.state = 'down'
        self.root.ids.completed_book_button.state = 'normal'

    def press_completed_books(self):
        """the function runs when "Completed books" is pressed"""
        self.create_books(mode='completed')#to get the completed book buttons
        self.root.ids.required_book_button.state = 'normal'
        self.root.ids.completed_book_button.state = 'down'

    def add_books(self, text_title, text_author, text_pages):
        """This function is to add books on the list of Book object, which occurs when "Add Item" is clicked """
        try:#try the code of the add_books method
            book_pages = int(text_pages)
            if text_title=="" or text_author=="" or text_pages=="":
                self.root.ids.bookMsg.text = "All fields must be completed"
            elif book_pages < 0:
                self.root.ids.bookMsg.text = "Pages must be positive number"
                self.root.ids.text_pages.text = ""#to empty the fields when text and value = ""
                self.root.ids.text_pages.value = ""
            else:
                self.book_lists.add_book(text_title,text_author,text_pages)#call the method add_book in BookLists() class in order to add book in the booklist
                self.clear_text()#to clear the input of those three fields after adding the book
                self.book_lists.sort_books()#sort the books in order to make the button more organised
                self.on_start()#to reset the state, which is to show the required list button
                self.root.ids.bookMsg.text = "{} by {}, {} pages is added".format(text_title,text_author,text_pages)#show the message that the books is added(to replace the message on the starting point of the program)
        except ValueError:
            if text_title=="" or text_author=="" or text_pages=="":#to make the exception runs when there is at least one of the text field is empty
                self.root.ids.bookMsg.text = "All fields must be completed"#to show the message when an exception happens
            else: #it is used when the value in the page text field is not the same type of the input(expected: int, the actual: str)
                self.root.ids.bookMsg.text = "Please enter a valid number"
                self.root.ids.text_pages.text = ""
                self.root.ids.text_pages.value = ""

    def click_required_books(self, instance):
        """This function is used for clicking the button for the book that is created based on create_books() in required books"""
        title = instance.text #instance.text is the text on the Button, which means instance is the Button in the kv file
        for required_name in self.book_lists.booklists:
            if required_name.title == title:#to check whether the text button you click match the title of the object in booklists(required_name.title)
                change_status = self.book_object.mark_completed(required_name.status)#to call method mark_completed() in the Book() class
                if change_status == True:
                    required_name.status = 'c'
                self.on_start()#to make the button immediately dissapear after clicking the button on the required books, otherwise the button is still there
                self.root.ids.bookMsg.text = "{} to be marked as completed".format(required_name.title)

    def click_completed_books(self,instance):
        """This function is used for clicking the button for the book that is created based on create_books() in completed books"""
        title = instance.text
        for completed_name in self.book_lists.booklists:
            if completed_name.title == title:#to check whether the text button you click match the title of the object in booklists(completed_name.title)
                self.root.ids.bookMsg.text = "{} (completed)".format(completed_name)#to show the message after you click the button on a list of completed books

    def clear_books(self):
        """This function is to clear the button in order to prevent duplicates in the button"""
        self.root.ids.entriesBox.clear_widgets()

    def clear_text(self):
        """This function is to clear the text field for adding books"""
        self.root.ids.text_title.text = ""
        self.root.ids.text_author.text = ""
        self.root.ids.text_pages.text = ""

    def build(self):
        """This function is to load the kv file"""
        self.title = "Reading List 2.0"#determine the title of the kv file
        self.root = Builder.load_file("app.kv")#to load the kv file
        return self.root

    def on_stop(self):
        """This function runs when you quit the program"""
        self.book_lists.save_books('books.csv')

ReadingListApp().run()
