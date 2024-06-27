class Book:
    def __init__(self,title,author,is_borrowed = False) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def display_status(self):
        return f"Book : {self.title} Borrowed : {self.is_borrowed}"
    

books = []
books.append(Book("Wings of Fire","Abdul Kalam"))
books.append(Book("Alchemist","Paulo Coehlo"))
books.append(Book("Harry Potter","JK Rowling"))

is_over = False

def show_status():
    for book in books:
        print(book.display_status())
while not is_over:
    print("--------------Status of all books---------------")
    show_status()
    name = input("Enter a book to borrow/return (or 'exit'): ")
    if name.lower() == "exit":
        is_over = True

    else:
        for book in books:
            if book.title.lower() == name.lower():
                if book.is_borrowed:
                    book.return_book()
                else:
                    book.borrow()


