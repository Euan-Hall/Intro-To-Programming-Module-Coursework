import database


# Searches for a book in the database
def search(bookName):
    bookFound = False
    books = []
    count = 0
    # Drop the header
    libraryDatabase = database.libraryDatabase[1:]
    for rows in libraryDatabase:
        print(bookName.lower(), rows[2].lower())
        # Changes both paramaters to lowercase to reduce errors
        if bookName.lower() in rows[2].lower():
            books.append(rows)
            bookFound = True
        count += 1
    if not bookFound:
        print("Book not in database.")
    else:
        return books
        

