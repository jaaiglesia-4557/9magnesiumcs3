class Publication:
    #Initialization and Setting of the attributes of the class
    def __init__ (self, title, author):
        self.__title = title
        self.__author = author

    #Methods
    @property
    def get_title(self):
        return self.__title
    @property
    def get_author(self):
        return self.__author

    def set_title(self, title):
        titleValidation = input("Enter the title of the publication:")
        try:
            title = str(titleValidation)
            self.__title = title
        except ValueError:
            print("Please give a valid name/string, NOT integer")
    def set_author(self, author):
        self.__author = author


#Initialization and setting of new and inherited attributes
class book(Publication):
    #class attributes
    def __init__(self, title, author, numberOfPages):
        #Inherited from superclass "Publication"
        super().__init__(title, author)
        self.numberOfPages = numberOfPages
    @property
    def get_numberOfPages(self):
        return self.numberOfPages
    @numberOfPages.setter
    def set_numberOfPages(self, numberOfPages):
        raw_numberofPages = input("Enter the number of pages in the book: ")
        try:
            numberOfPages = int(raw_numberofPages)
            if numberOfPages > 0:
                self.numberOfPages = numberOfPages
            else:
                print("Invalid number of pages, please give an integer greater than zero")
        except ValueError:
            print("Please give a valid integer")
class magazine(Publication):
    def __init__(self, title, author, issueNumber):
        super().__init__(title, author)
        self.issueNumber = issueNumber

    def get_issueNumber(self):
        return self.issueNumber
    @issueNumber.setter
    def set_issueNumber(self, issueNumber):
        raw_issuenumber = int(input("Enter the issue number of the magazine: "))
        try:
            if raw_issuenumber > 0:
                self.issueNumber = raw_issuenumber
            else:
                print("Invalid, give a valid issue number greater than zero")
        except ValueError:
            print("Please give an INTEGER")
