import database
import csv
from datetime import date

def bookReturn(bookID):
    """ Returns the given book if the bookID is valid.
    bookID -> String
    """
    # Checks if bookID is valid
    try: bookID = int(bookID)
    except ValueError: bookID = -1
    if bookID <= len(database.libraryDatabase)-1 and bookID > 1:
        # Updates the local data
        if database.libraryDatabase[bookID][5] != "0":
            # Inefficient way of checking the logs...
            logRead = []
            with open('log.txt')as logFile:
                reader = csv.reader(logFile, delimiter = ',')
                for row in reader:
                    logRead.append(row)

            # Read from end of file to the beginning for recent activity.
            logRead.reverse()
            header = ','.join(logRead[-1]) + "\n"
            print(header)
            del logRead[-1] # Drop the header
            for row in logRead:
                if int(row[3]) == bookID:
                    # Find the number of days it has been loaned out
                    today = date.today()
                    today = today.strftime("%d/%m/%Y")
                    todayLog = today
                    today = list(map(int, today.split("/")))
                    today = date(today[2], today[1], today[0])
                    
                    dateLoaned = list(map(int,row[0].split("/")))
                    dateLoaned = date(dateLoaned[2], dateLoaned[1], dateLoaned[0])

                    dateDifference = today - dateLoaned
                    if dateDifference.days > 60:
                        print(f"Book has been out for {dateDifference} days.")
                        

                    # Update database
                    database.libraryDatabase[bookID][5] = "0"
                    with open('database.txt', 'w') as csvFile:
                        for rows in database.libraryDatabase:
                            csvFile.write(f"{','.join(rows)}\n")
                            
                    # Update logFile
                    row[1] = todayLog
                    print(todayLog, row)
                    with open('log.txt', 'w') as logFile:
                        line = 0
                        for row in logRead:
                            if line == 0: logFile.write(header)
                            rowAdd = ",".join(row) + "\n"
                            logFile.write(rowAdd)
                            line += 1
                    print("Book returned, Updated database.")
                    break
        else:
            print("Book not loaned.")
    else:
        print("Invalid bookID.")
