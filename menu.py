import bookcheckout, bookreturn, booksearch, recommendBook
import random


def printBooks(book):
    """Prints out the books after a search. Book -> List"""
    print(f"{len(book)} Result(s):")
    count = 0
    for i in book:
        print("--------------------")
        print(f"Book ID: {i[0]}\nBook: {i[2]}\nAuthor: {i[1]}")
        print(f"Loaned: {i[5] != '0'}")
        count += 1


def main():
    while True:
        print("""Welcome to the library! What do you want to do?
    ------------------------------------------------------------
        1. Loan book
        2. Return book
        3. Recommend book (Unfinished)
        4. Search for a book
        5. Quit
    ------------------------------------------------------------""")
        # Check if choice is valid
        try: choice = int(input("Choice: "))
        except ValueError: choice = -1

        # Call functions based on choice, and if it matches the choice	
        match choice:
            case 1:
                # Find the book to loan
                book = str(input("What book do you want to loan? "))
                book = booksearch.search(book)

                # Check if it exists
                if book:
                    printBooks(book)
                    print("--------------------")
                    # Find the book to loan
                    book = str(input("Which ID of the book do you want to loan? "))
                    memberID = str(input("What is your ID? "))
                    bookcheckout.bookCheckout(memberID, book)
                else:
                    print("No book found.")
                    print("--------------------")

            case 2:
                # Returns a book given the bookID
                book = str(input("What book do you want to return (ID)? "))
                bookreturn.bookReturn(book)
            case 3:
                # Find the books currently loaned out to the given member
                # Sum together the same genres, make a ratio out of them
                # Find the probability from them, and pick a random number
                # If that random number is bigger than the given P, it's not that genre
                memberID = str(input("What is your ID? "))
                books = recommendBook.recommendBook(memberID)
                print(f"Recommended genre for {memberID}: {random.choice(books)}")


            case 4:
                # Calls the booksearch function
                book = str(input("What book do you want to search? "))
                book = booksearch.search(book)

                # If the list returned isn't empty, print all the items in the list
                if book:
                    printBooks(book)
                else:
                    print("No results found.")
                print("--------------------")
                wait = input("Press enter to continue...")
            case 5:
                print("Bye, have a great time!")
                break
            case _:
                print("Invalid choice.")

                
if __name__ == "__main__":
    main()
