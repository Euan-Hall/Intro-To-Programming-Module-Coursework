import database

def bookReturn(bookID):
    # Checks if bookID is valid
    try: bookID = int(bookID)
    except ValueError: bookID = -1
    if bookID <= len(database.libraryDatabase)-1 and bookID > 1:
        # Updates the local data
        if database.libraryDatabase[bookID][5] != 0:
            database.libraryDatabase[bookID][5] = "0"
            with open('database.txt', 'w') as csvFile:
                for rows in database.libraryDatabase:
                    csvFile.write(f"{','.join(rows)}\n")

            with open('log.txt', 'a')as logFile:
                    logFile.write(f"Book {bookID} returned\n")

            print("Book returned, Updated database.")
        else:
            print("Book not loaned.")
    else:
        print("Invalid bookID.")
