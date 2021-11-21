import database
import csv
from datetime import date


def checkDate(row):
    """Finds the amount of days the book has been loaned out for,
    given the log row.
    Row -> List
    """
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    todayLog = today
    today = list(map(int, today.split("/")))
    today = date(today[2], today[1], today[0])
                    
    dateLoaned = list(map(int,row[0].split("/")))
    dateLoaned = date(dateLoaned[2], dateLoaned[1], dateLoaned[0])

    dateDifference = today - dateLoaned
    return dateDifference, todayLog


def bookReturn(bookID):
    """ Returns the given book if the bookID is valid.
    bookID -> String
    """
    # Checks if bookID is valid
    try: bookID = int(bookID)
    except ValueError: bookID = -1
    if bookID <= len(database.libraryDatabase)-1 and bookID > 0:
        # Updates the local data
        if database.libraryDatabase[bookID][5] != "0":
            # Inefficient way of checking the logs...
            logRead = []
            with open('log.txt')as logFile:
                reader = csv.reader(logFile, delimiter = ',')
                for row in reader:
                    logRead.append(row)
            print(logRead)

            # Read from end of file to the beginning for recent activity.
            logRead.reverse()
            header = ','.join(logRead[-1]) + "\n"
            del logRead[-1] # Drop the header
            for row in logRead:
                if int(row[3]) == bookID:
                    # Find the number of days it has been loaned out
                    dateDifference, todayLog = checkDate(row)
                        

                    # Update database
                    database.libraryDatabase[bookID][5] = "0"
                    with open('database.txt', 'w') as csvFile:
                        for rows in database.libraryDatabase:
                            csvFile.write(f"{','.join(rows)}\n")
                            
                    # Update logFile
                    row[1] = todayLog
                    with open('log.txt', 'w') as logFile:
                        line = 0
                        logRead.reverse()
                        for row in logRead:
                            print(row)
                            if line == 0: logFile.write(header)
                            # Could do ','.join() but it adds spaces...gonna check later
                            logFile.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")
                            line += 1
                    return ("Book returned, Updated database.\n", dateDifference)
                    break
        else:
            return "Book not loaned"
    else:
        return "Invalid BookID"
