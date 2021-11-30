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
    bookID = ''.join(bookID.split()).split(',') # Remove whitespaces split via comma
    results = []
    for item in bookID:
        try: item = int(item)
        except ValueError: item = -1
        if item <= len(database.libraryDatabase)-1 and item > 0:
            # Updates the local data
            if database.libraryDatabase[item][5] != "0":
                # Inefficient way of checking the logs...
                logRead = []
                with open('log.txt')as logFile:
                    reader = csv.reader(logFile, delimiter = ',')
                    for row in reader:
                        logRead.append(row)

                # Read from end of file to the beginning for recent activity.
                logRead.reverse()
                header = ','.join(logRead[-1]) + "\n"
                del logRead[-1] # Drop the header
                for row in logRead:
                    if int(row[3]) == item:
                        # Find the number of days it has been loaned out
                        dateDifference, todayLog = checkDate(row)

                        # Update database
                        database.libraryDatabase[item][5] = "0"
                        with open('database.txt', 'w') as csvFile:
                            for rows in database.libraryDatabase:
                                csvFile.write(f"{','.join(rows)}\n")
                                
                        # Update logFile
                        row[1] = todayLog
                        with open('log.txt', 'w') as logFile:
                            line = 0
                            logRead.reverse()
                            for row in logRead:
                                if line == 0: logFile.write(header)
                                # Could do ','.join() but it adds spaces...gonna check later
                                logFile.write(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n")
                                line += 1
                        if dateDifference.days > 60:
                            results.append((f"Book {item} returned, Updated database.", dateDifference))
                        else:
                            results.append(f"Book {item} returned, Updated database.")
                        break
            else:
                results.append(f"Book {item} not loaned")
        else:
            results.append("Invalid BookID")
    return results
