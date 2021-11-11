import csv

# Opens the database and reads it as a CSV file
libraryDatabase = []
with open('database.txt') as csvFile:
    reader = csv.reader(csvFile, delimiter = ',')
    # Includes the header
    for row in reader:
        libraryDatabase.append(row)



    
        
