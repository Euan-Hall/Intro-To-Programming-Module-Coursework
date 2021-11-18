from datetime import date
from bookreturn import checkDate
import csv
import database
import re


def bookCheckout(memberID, bookID):
    """ Updates the database with the parameters memberID and bookID."""
    # Checks if MemberID and bookID are valid
    if len(memberID) == 4 and re.search("([a-zA-z]{4})", memberID):

        # Check for any books the member has out on loan greater than 60 days
        loanedDates = []
        with open('log.txt')as logFile:
            reader = csv.reader(logFile, delimiter = ',')
            for row in reader:
                # Only find the difference if it has not been returned yet.
                if row[2] == memberID and row[1] == "-1":
                    print("a")
                    dateDifference = checkDate(row)
                    loanedDates.append([dateDifference[0], row[3]])

        try: bookID = int(bookID)
        except ValueError: bookID = -1
        if 1 < bookID <= len(database.libraryDatabase)-1:
            # Updates the loaded database
            bookOut = database.libraryDatabase[bookID][5]
            
            # Check if the book is currently unloaned
            if bookOut == "0":
                # Updates database
                database.libraryDatabase[bookID][5] = memberID.lower()
                with open('database.txt', 'w') as csvFile:
                    for rows in database.libraryDatabase:
                        csvFile.write(f"{','.join(rows)}\n")

                # Updates log
                with open('log.txt', 'a')as logFile:
                    currDate = date.today()
                    currDate = currDate.strftime("%d/%m/%Y")
                    genre = database.libraryDatabase[bookID][1]
                    logFile.write(f"{currDate},-1,{memberID},{bookID},{genre}")
                return ("Book checked out, Updated database.\n", loanedDates)
            else:
                # Book is loaned
                return (f"Book currently loaned to {bookOut}\n", loanedDates)
        else:
            return "Invalid bookID.\n"
    else:
        return "Invalid memberID.\n"

    
