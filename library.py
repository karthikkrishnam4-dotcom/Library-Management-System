class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,book):
        for existing_book in self.book:
            if existing_book.book_id == book.book_id:
                print("Book id already EXist!")
                return
        self.book.append(book)
        print("Book added Successfully!")
    def display_books(self):
        for book in self.book:
            book.display()
    def search_book(self,books_id):
        found=False
        for book in self.book:
            if book.book_id == books_id:
                print("book found!")
                book.display()
                found=True
                break
        if not found:
            print("Book Not is There")

    def remove_book(self,books_id):
        found=False
        for book in self.book:
            if book.book_id == books_id:
                self.book.remove(book)
                print("book removed sucessfully!")
                found=True
                break
        if not found:
            print("Book Not is There")
    def borrow_book(self,books_id,member):
        found=False
        for book in self.book:
            if book.book_id==books_id:
                found=True

                if book.is_available:
                    book.is_available = False
                    member.borrowed_books.append(book)
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed!")
                break
                
        if not found:
            print("Book is not found")
    def return_book(self,books_id,member):
        found=False
        for book in self.book:
            if book.book_id == books_id:
                found=True
                if not book.is_available and book in member.borrowed_books:
                    book.is_available=True
                    member.borrowed_books.remove(book)
                    print("Book was returned")
                else:
                    print("This member was not borrowed the Book")
                break
        if not found:
            print("Book not found")