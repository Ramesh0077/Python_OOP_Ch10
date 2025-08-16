# 9. Delete Instance Variable
# Create a Book class with title and author.
# Delete the author attribute for one object and try printing it.

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display(self):
        print(f"Title is {self.title}, and auther is {self.author}")

book1=Book("Ramesh","Java")
book2=Book("Dhb","Python")
book1.display()
book2.display()

del book2.author
book1.display()
# book2.display()    cause error