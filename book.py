class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available = True
    def display(self):
        print("book_id:",self.book_id)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Status:", "Available" if self.is_available else "Borrowed")
