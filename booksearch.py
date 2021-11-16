import database


# Searches for a book in the database
def search(bookName):
    bookFound = False
    books = []
    count = 0
    for rows in database.libraryDatabase:
        if not count:
            continue
        # Changes both paramaters to lowercase to reduce errors
        if bookName.lower() in rows[2].lower():
            books.append(rows)
            bookFound = True
        count += 1
    if not bookFound:
        print("Book not in database.")
    else:
        return books
        

