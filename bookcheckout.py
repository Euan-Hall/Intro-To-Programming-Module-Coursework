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
                if row:
                    # Only find the difference if it has not been returned yet.
                    if row[2] == memberID and row[1] == "-1":
                        dateDifference = checkDate(row)
                        if dateDifference[0].days > 60:
                            loanedDates.append([dateDifference[0], row[3]])
                                
        bookID = ''.join(str(bookID).split()).split(',') # Remove whitespaces split via comma
        results = []
        for item in bookID:
            try: item = int(item)
            except ValueError: item = -1
            if 1 <= item <= len(database.libraryDatabase)-1:
                # Updates the loaded database
                bookOut = database.libraryDatabase[item][5]
                
                # Check if the book is currently unloaned
                if bookOut == "0":
                    # Updates database
                    database.libraryDatabase[item][5] = memberID.lower()
                    with open('database.txt', 'w') as csvFile:
                        for rows in database.libraryDatabase:
                            csvFile.write(f"{','.join(rows)}\n")

                    # Updates log
                    with open('log.txt', 'a')as logFile:
                        currDate = date.today()
                        currDate = currDate.strftime("%d/%m/%Y")
                        genre = database.libraryDatabase[item][1]
                        logFile.write(f"{currDate},-1,{memberID},{item},{genre}\n")
                    results.append((f"Book, {item}, checked out, Updated database.\n", loanedDates))
                else:
                    # Book is loaned
                    results.append((f"Book, {item}, currently loaned to {bookOut}.\n", loanedDates))
            else:
                results.append(f"Invalid bookID, {item}.\n")
        return results
    else:
        return "Invalid memberID\n"

    
