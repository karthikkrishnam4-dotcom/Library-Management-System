class Member:
    def __init__(self,member_id,name,phone):
        self.member_id=member_id
        self.name=name
        self.phone=phone
        self.borrowed_books=[]
    def display(self):
        print("Mamber Id:",self.member_id)
        print("Name:",self.name)
        print("Phone:",self.phone)
    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed Books")
        else:
            for book in self.borrowed_books:
                book.display()
            
