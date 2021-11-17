import re
import csv
import random

# Find the books currently loaned out to the given member
# Sum together the same genres, make a ratio out of them
# Find the probability from them


def recommendGenre(memberID):
    """Recommends genre given the memberID"""
    # Check if memberID is valid
    if len(memberID) == 4 and re.search("([a-zA-z]{4})", memberID):
        memberBooks = []
        allBooks = []
        with open('log.txt')as logFile:
            reader = csv.reader(logFile, delimiter = ',')
            for row in reader:
                allBooks.append(row[4])
                # Find what genre of books have been loaned to memberID
                if row[2] == memberID:
                    memberBooks.append(row[4])
        if memberBooks:
            return random.choice(memberBooks)
    return random.choice(allBooks)

def recommendBook(memberID):
    """Recommends genre given the memberID"""
    genre = recommendGenre(memberID)
    with open('database.txt')as database:
        reader = csv.reader(database, delimiter = ',')
        books = []
        for row in reader:
            # Find what genre of books have been loaned to memberID
            if row[1] == genre:
                books.append(row[2])
        if books:
            return books
    return None


