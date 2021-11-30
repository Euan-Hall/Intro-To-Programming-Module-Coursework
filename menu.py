from matplotlib.figure import Figure
from matplotlib.pyplot import close
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import bookcheckout, bookreturn, booksearch, recommendBook
import random
import tkinter as tk

def printBooks(book):
    """Prints out the books after a search. Book -> List"""
    searchResults.delete('1.0', tk.END)
    searchResults.insert(tk.END, f"{len(book)} Result(s):\n")
    for i in book:
        searchResults.insert(tk.END, "--------------------\n")
        text = f"Book ID: {i[0]}\nBook: {i[2]}\nAuthor: {i[1]}\n"
        searchResults.insert(tk.END, text)
        text = f"Book ID: {i[0]}\nBook: {i[2]}\nAuthor: {i[1]}\n"
        searchResults.insert(tk.END, text)
        searchResults.insert(tk.END, f"Loaned: {i[5] != '0'}\n")
        
def loan():
    """ Loans a book given a bookInput value"""
    # Find the book to loan
    searchResults.delete('1.0', tk.END)
    book = bookInput.get()
    memberID = memberIDInput.get()
    # Check if bookID and memberID is filled
    if not book:
        searchResults.insert(tk.END, "Invalid BookID.\n")
    else:
        result = bookcheckout.bookCheckout(memberID, book)
        print(result)

        # Display results
        for item in result:
            if type(item) == tuple:
                searchResults.insert(tk.END, item[0])
                for element in item[1]:
                    if element[1] != []:
                        searchResults.insert(tk.END,
                                             f"Book {element[1]} has been out for {element[0].days} days\n")
                        
            else:
                searchResults.insert(tk.END, item)
    plotBooks()
        


def returnBook():
    """ Returns a book depending on the bookInput value """
    # Returns a book given the bookID
    searchResults.delete('1.0', tk.END)
    book = bookInput.get()
    returnResult = bookreturn.bookReturn(book)

    for item in returnResult:
        print(item)
        if type(item) == tuple:
            print(item[0])
            searchResults.insert(tk.END, item[0])
            for element in item[1]:
                if element[1] != []:
                    searchResults.insert(tk.END, f"Book has been out for {element[0].days} days\n")
        else:
            searchResults.insert(tk.END,f"{item}\n")
    
    plotBooks()    

def recommend():
    """ Recommends a book from a given memberID, if the memberID hasn't
        loaned any books, the top 3 genres are displayed."""
    # Recommends a book
    searchResults.delete('1.0', tk.END)
    memberID = memberIDInput.get()
    if memberID:
        books = recommendBook.recommendBook(memberID)
        random.shuffle(books)
        if type(books) == tuple:
            searchResults.insert(tk.END,books[0])
        else:
            searchResults.insert(tk.END,f"Recommended book for {memberID}:\n")
            for row in books:
                searchResults.insert(tk.END,f"{row}\n")
                
    else:
        searchResults.insert(tk.END,f"No memberID entered")

def search():
    # Calls the booksearch function
    searchResults.delete('1.0', tk.END)
    book = bookInput.get()
    book = booksearch.search(book)

    # If the list returned isn't empty, print all the items in the list
    if book:
        printBooks(book)
    else:
        searchResults.insert(tk.END, "No books found.")

def plotBooks():
    fig.clear()

    # list of squares
    genres = recommendBook.popularGenres()
    genres.sort()
    x = list(dict.fromkeys(genres))
    sorted(x)
    y = []
    curr = genres[0]
    count = 0
    for i in enumerate(genres):
        if i[1] == curr:
            count += 1
        else:
            curr = i[1]
            y.append(count)
            count = 1
    y.append(count)
    # adding the subplot
    barChart = fig.add_subplot(111)
    barChart.bar(x, y, align='center', alpha=0.5)
    barChart.set_title('Popular Genres')

    # creating the canvas containing the Matplotlib figure
    canvas.draw()

    # placing the canvas on the window
    canvas.get_tk_widget().pack()
    

# Loading the GUI
root = tk.Tk()
textFrame = tk.Frame(root)
buttonInputFrame = tk.Frame(root)
buttonFrame = tk.Frame(buttonInputFrame)
buttonInput = tk.Frame(buttonInputFrame)
graphFrame = tk.Frame(root)


# Creating the buttons and text

searchButton = tk.Button(buttonFrame,
                         text="Search for book",
                         command=search,
                         width=15)
loanBookButton = tk.Button(buttonFrame,
                           text="Loan book",
                           command=loan,
                           width=15)
returnBookButton = tk.Button(buttonFrame,
                             text="Return book",
                             command=returnBook,
                             width=15)
recommendBookButton = tk.Button(buttonFrame,
                                text="Recommend book",
                                command=recommend,
                                width=15)

bookInputText = tk.Label(buttonInput, text="Book ID:")
memberIDText = tk.Label(buttonInput, text="Member ID:")
bookInput = tk.Entry(buttonInput)
memberIDInput = tk.Entry(buttonInput)

searchResults = tk.Text(textFrame, height=10, width=50)


# Packing the buttons and text
searchResults.grid(row=0, column=2)
textFrame.grid(row=0, column=2)

# Own frame
searchButton.grid(row=1, column=0)
loanBookButton.grid(row=2, column=0)
returnBookButton.grid(row=3, column=0)
recommendBookButton.grid(row=4, column=0)
buttonFrame.grid(row=0, column=0)

# Plot barchart for popular genres
fig = Figure(figsize=(4,2), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=graphFrame)  
plotBooks()

# Own frame
bookInputText.grid(row=3, column=0)
bookInput.grid(row=3, column=1)
memberIDText.grid(row=4, column=0)
memberIDInput.grid(row=4, column=1)
buttonInput.grid(row=2, column=0)

buttonInputFrame.grid(row=0, column=0)

# Warning in book results?

graphFrame.grid(row=0, column=3, padx=10, pady=10)

# Load the window
root.mainloop()

                
if __name__ == "__main__":
    main()
