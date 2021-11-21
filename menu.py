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

        # Display results
        if type(result) == tuple:
            searchResults.insert(tk.END, result[0])
            for item in result[1]:
                searchResults.insert(tk.END,
                                     f"Book {item[1]} has been out for {item[0].days} days\n")
        else:
            searchResults.insert(tk.END, result)
        


def returnBook():
    """ Returns a book depending on the bookInput value """
    # Returns a book given the bookID
    searchResults.delete('1.0', tk.END)
    book = bookInput.get()
    returnResult = bookreturn.bookReturn(book)
    if type(returnResult) == tuple:
        searchResults.insert(tk.END, returnResult[0])
        searchResults.insert(tk.END, f"Book has been out for {returnResult[1].days} days\n")
    else:
        searchResults.insert(tk.END,returnResult)
    
    

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



# Loading the GUI
root = tk.Tk()
textFrame = tk.Frame(root)
buttonInputFrame = tk.Frame(root)
buttonFrame = tk.Frame(buttonInputFrame)
buttonInput = tk.Frame(buttonInputFrame)


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

# Own frame
bookInputText.grid(row=3, column=0)
bookInput.grid(row=3, column=1)
memberIDText.grid(row=4, column=0)
memberIDInput.grid(row=4, column=1)
buttonInput.grid(row=2, column=0)

buttonInputFrame.grid(row=0, column=0)
# Warning in book results?


# Load the window
root.mainloop()

                
if __name__ == "__main__":
    main()
