
class Book:
    def __init__(self, name, author):
        self.name   = name
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        print("Adding new book....")
        self.books.append(book.name)
        print(f"Book {book.name} from the author {book.author} added to the library.")
        print()
    
    def edit_book(self,old_title,new_title):
        for i,book in enumerate(self.books):
            if old_title == book:
                print(f"Book {old_title} is changed to {new_title}.")
                self.books[i] = new_title
                return 
        print("There is no book with such title....")
        print()
        
    def delete_book(self, title):
        for book in self.books:
            if book == title:
                self.books.remove(book)
                print(f"{title} removed from library...")
                return
        print("There is no such book.")
        print()

    def list_books(self):
        print("The books in our library: ")
        for i,book in enumerate(self.books):
            print(f"{i+1}. {book}")
        print()


library = Library()

def main():
    while True:
        print("Welcome to our library......\nMenu:")
        print("1. Add new book")
        print("2. Edit book")
        print("3. Delete book")
        print("4. List all books")
        print("5. Quit the program")
    
        choice = int(input("Enter: "))
        print()

        if choice == 1:
            title = input("Book's title: ")
            auth = input("Book's author: ")
            book = Book(title,auth)
            library.add_book(book)
        elif choice == 2:
            old = input("Enter old title: ")
            new = input("Enter new title: ")
            library.edit_book(old,new)
        elif choice == 3:
            title = input("Enter the title of the book to delete: ")
            library.delete_book(title)
        elif choice == 4:
            library.list_books()
        elif choice == 5:
            print("Goodbye...")
            break
        else:
            print("Wrong command. Please choose a number from 1 to 5 ")

main()