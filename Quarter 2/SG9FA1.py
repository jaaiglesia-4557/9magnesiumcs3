class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
# (This applies to all classes), the "@property" decorator is used to create getter methods for private attributes, allowing controlled access to them.
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    #Secure Setters using try-except
    def set_title(self, title):
        try:
            title.upper() # Type check: will crash if not a string
            self.__title = title
        except AttributeError:
            print("Error: Title must be a string (text).")

    def set_author(self, author):
        try:
            author.lower() # Type check: will crash if not a string
            self.__author = author
        except AttributeError:
            print("Error: Author must be a string (text).")

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        #Super() is used to call the constructor of the parent class to initialize title and author
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        try:
            number_of_pages + 1 # Type check: will crash if not an int/float
            if number_of_pages > 0:
                self.__number_of_pages = number_of_pages
            else:
                print("The number of pages must be positive.")
        except TypeError:
            print("Error: Number of pages must be an integer.")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        #Super() is used to call the constructor of the parent class to initialize title and author
        super().__init__(title, author)
        self.__issue_number = issue_number

    @property
    def issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        try:
            issue_number + 1 # Type check: will crash if not an int/float
            if issue_number > 0:
                self.__issue_number = issue_number
            else:
                print("The issue number must be positive.")
        except TypeError:
            print("Error: Issue number must be an integer.")

#Two Objects initialized each for Publication, Book, and Magazine classes
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Science Daily", "Various Authors")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 400)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Various Authors", 15)

#Test Runs for one object of each class
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310) # Testing negative validation
book1.display_info()
print(f"Number of Pages: {book1.number_of_pages}")

print("\nMagazine Information:")
mag1.display_info()
print(f"Issue Number: {mag1.issue_number}")

#Testing the new Security
print("\nTesting Type Security")
pub1.set_title(123) # Invalid: integer instead of string
book1.set_number_of_pages("310") # Invalid: string instead of integer
mag1.set_issue_number(None) # Invalid: NoneType

