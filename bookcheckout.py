import database
import re

def bookCheckout(memberID, bookID):
    """ Updates the database with the paramaters memberID and bookID."""
    # Checks if MemberID and bookID are valid
    if len(memberID) == 4 and re.search("([a-zA-z]{4})", memberID):
        try: bookID = int(bookID)
        except ValueError: bookID = -1
        if 1 < bookID <= len(database.libraryDatabase)-1:
        # Updates the database
            
            bookOut = database.libraryDatabase[bookID][5]
            # Check if the book is currently loaned
            if bookOut == "0":
                database.libraryDatabase[bookID][5] = memberID
                with open('database.txt', 'w') as csvFile:
                    for rows in database.libraryDatabase:
                        csvFile.write(f"{','.join(rows)}\n")
                print("Book checked out, Updated database.")

                with open('log.txt', 'a')as logFile:
                    logFile.write(f"Book {bookID} loaned to {memberID}\n")
            else:
                print(f"Book currently loaned to {bookOut}")
        else:
            print("Invalid bookID.")
    else:
        print("Invalid memberID.")

    
