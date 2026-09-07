# Book Record Management

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully.")


def search_book():
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.")
            else:
                print("Book is already available.")
            return

    print("Book not found.")


def display_available():
    print("\nAvailable Books:")

    found = False

    for book in books:
        if book["available"]:
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print()
            found = True

    if not found:
        print("No books are available.")


while True:
    print("\n--- BOOK MANAGEMENT ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        display_available()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")