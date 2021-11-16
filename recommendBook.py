import re
import csv

# Find the books currently loaned out to the given member
# Sum together the same genres, make a ratio out of them
# Find the probability from them


def recommendBook(memberID):
    # Check if memberID is valid
    if len(memberID) == 4 and re.search("([a-zA-z]{4})", memberID):
        books = []
        with open('log.txt')as logFile:
            reader = csv.reader(logFile, delimiter = ',')
            for row in reader:
                # Find what genre of books have been loaned to memberID
                if row[2] == memberID:
                    books.append(row[4])
        books.sort()
        return books
    return None
