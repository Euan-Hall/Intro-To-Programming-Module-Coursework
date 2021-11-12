~~~ TO DO ~~~
- Check if book is out for more than 60 days
- Make GUI for library system
- Reccomend book
- Reutrn what books are loaned to a specific member
- Update bookReturn given bookID and memberID, rather than just bookID.
- Update database to include loan date - -1 if unloaned.
- Update Log to a CSV (makes reccomendations easier.) (I.e. Loan, MemberID, Book, Genre)
- Docstrings

~~~ Completed (or near enough) ~~~ 
- BookCheckout
- BookReturn
- BookSearch
- Database

~~~ Warnings ~~~ 
None so far

~~~ In Detail ~~~
BookCheckout :
	~~ To do ~~
	~~ Completed ~~
	- Contains a function named bookCheckout that takes 2 paramaters (memberID: Str, bookID: Int).
	- Both paramaters are checked if they are valid
	- If valid, it will then check if the book is loaned out
	- If not, it will update the database to say the book is loaned to the given member.
	- Appropriate messages displayed.
	Examples:
	(Unloaned book.)
	>> bookCheckout("coeh", 10)
	>> Book checked out, Updated database.
	
	(Invalid MemberID)
	>> bookCheckout("co1h", 10)
	>> Invalid memberID.

	(Invalid BookID)
	>> bookCheckout("co1h", "10")
	>> Invalid bookID
	
	(Loaned book.)
	>> bookCheckout("coeh", 10)
	>> Book currently loaned to <member>

BookReturn : 
	~~ To do ~~ 
	- Get memberID from User, find any books that might need returned and disiplay them
	
	~~ Completed ~~
	- Contains a function named bookReturn that takes one parameter (bookID: Int)
	- bookID chcked if valid
	- If valid, it will then update the row corresponding to the bookID, on the database, as returned.
	- Appropriate messages displayed.
	Examples:
	(Unloaned book.)
	>> bookReturn(1)
	>> Book not loaned.

	(Loaned book.)
	>> bookReturn(2)
	>> Book returned, Updated database.
		
	(Invalid bookID)
	>> bookReturn("l")
	>> Invalid bookID.

Booksearch:
	~~ To Do ~~
	- Make search in booksearch return the bookID.
	~~ Completed ~~
	- Contains a function named search that takes one parameter (bookName: Str)
	- Checks the database if there exists a book with that name
	- If a book is found an appropriate message is displayed
	- Found books are stored in a list named books - handles books with the same/similar name.
	- If no books are found then an appropriate message is displayed.
	Examples:
	(Book found)
	>> search("bookName")
	>> Book found in row <row>
	
	(Multiple books found)
	>> search("bookName")
	>> Multiple books found: <books>

	(No books found)
	>> search("bookName")
 	>> Book not in database.

Menu: -
	
