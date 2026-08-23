
#29-Create dictionary containing book IDs and book names
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

# Add a book
books[104] = "DBMS"

# Search a book
book_id = 102

if book_id in books:
    print("Book found:", books[book_id])
else:
    print("Book not found")

# Remove a book
books.pop(103)

# Display all books
print("All books:", books)

# Count total books
print("Total books:", len(books))

