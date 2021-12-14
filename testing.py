from bookcheckout import bookCheckout
from bookreturn import bookReturn

def testBookCheckout():
    # invalid memberID
    memberID = "1234"
    bookID = 0
    result = bookCheckout(memberID, bookID)
    print(f"bookCheckout({memberID}, {bookID}) := {result}", end='')
    testResult = result == "Invalid memberID\n"
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")

    # invalid bookID
    memberID = "abcd"
    bookID = 0
    result = bookCheckout(memberID, bookID)
    print(f"bookCheckout({memberID}, {bookID}) := {result}")
    testResult = result == ["Invalid bookID, 0.\n"]
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")

    # invalid bookID
    memberID = "abcd"
    bookID = 999999
    result = bookCheckout(memberID, bookID)
    print(f"bookCheckout({memberID}, {bookID}) := {result}")
    testResult = result == ['Invalid bookID, 999999.\n']
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")

    # Correct bookID and memberID
    memberID = "abcd"
    bookID = 5
    result = bookCheckout(memberID, bookID)
    print(f"bookCheckout({memberID}, {bookID}) := {result}")
    testResult = result == [('Book, 5, checked out, Updated database.\n', [])]
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")

    # Book Return, correct bookID
    result = bookReturn(bookID)
    testResult =  result == ['Book 5 returned, Updated database.']
    print(f"bookReturn({bookID}) := {result}")
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")
    
    
def testBookReturn():
    # Invalid bookID
    bookID = -1
    result = bookReturn(bookID)
    testResult =  result == ['Invalid BookID']
    print(f"bookReturn({bookID}) := {result}")
    print(f"Test {'passed'*testResult}{'failed'*(not testResult)}")
    
