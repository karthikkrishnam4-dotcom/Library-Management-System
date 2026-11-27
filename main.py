
from book import Book
from member import Member
from library import Library

lib = Library()
m1 = Member(1, "krishna", "8807654506")

while True:
    print("\n--- Library Management System ---")
    print("1. Add book")
    print("2. Display book")
    print("3. Search book")
    print("4. Remove book")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Exit")
    print("8. Display borrowed books")

    choice = input("Enter the Number: ")

    if choice == "1":
        try:
            book_id = int(input("Enter Book ID: "))

            if book_id <= 0:
                print("Book ID must be a positive number!")
                continue
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            if title.strip() or not author.strip():
                print("Title and Author cannot be empty!")

            else:
                book = Book(book_id, title, author)
                lib.add_book(book)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":
        lib.display_books()

    elif choice == "3":
        try:
            books_id = int(input("Enter Book ID: "))
            lib.search_book(books_id)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        try:
            books_id = int(input("Enter Book ID: "))
            lib.remove_book(books_id)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        try:
            books_id = int(input("Enter Book ID: "))
            lib.borrow_book(books_id, m1)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "6":
        try:
            books_id = int(input("Enter Book ID: "))
            lib.return_book(books_id, m1)

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    elif choice == "8":
        m1.display_borrowed_books()

    else:
        print("Invalid choice! Please select 1-8.")
