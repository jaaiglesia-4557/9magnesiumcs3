class Publication:
    #Initialization and Setting of the attributes of the class
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    #Methods

    @property
    def get_title():
        return title
    @property
    def get_author():
        return author

    def set_title(title):
        titleValidation = input("Enter the title of the publication:")
        try:
            title = int(titleValidation)
            if pages > 0:
                print("Valid page count, assigning value to the attribute...")
                self.title = title
            else:
                print("Enter an integer greater than zero")
        except ValueError:
            print("Please give an INTEGER greater than zero")
    def set_author(author):
        self.author = author


#Initialization and setting of new and inherited attributes
class book(Publication):
    #class attributes
    def __init__(self, title, author, numberOfPages):
        #Inherited from superclass "Publication"
        super().__init__(title, author)
        self.numberOfPages = numberOfPages

    def get_numberOfPages():
        return numberOfPages

    def set_numberOfPages(numberOfPages):
        if numberOfPages > 0:
            self.numberOfPages = numberOfPages
        else:
            print("Invalid number of pages, please give an integer greater than zero")
class magazine(Publication):
    def __init__(self, title, author, issueNumber):
        super().__init__(title, author)
        self.issueNumber = issueNumber

    def get_issueNumber():
        return self.issueNumber
    def set_issueNumber(issueNumber):
        if issueNumber > 0:
            self.issueNumber = issueNumber