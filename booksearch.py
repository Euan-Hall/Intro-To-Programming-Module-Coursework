import database

# Searches for a book in the database
def search(bookName):
    bookFound = False
    books = []
    for rows in database.libraryDatabase:
        # Changes both paramaters to lowercase to reduce errors
        if bookName.lower() in rows[2].lower():
            books.append(rows)
            bookFound = True
    if not bookFound:
        print("Book not in database.")
    else:
        return books
        

