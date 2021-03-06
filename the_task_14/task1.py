import pprint
import sys
import sqlite3 as lite

data = ''

con = None

query_string = '''
    SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName, Customer.Phone, Customer.Company
    FROM Customer
    JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId
    JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID
    JOIN InvoiceLine ON InvoiceLine.InvoiceID = Invoice.InvoiceID
    JOIN Track ON InvoiceLine.TrackID = Track.TrackID
    JOIN Genre ON Track.GenreID = Genre.GenreID

    WHERE Genre.Name != "Rock" AND Employee.BirthDate < "1969-05-19"
    ORDER BY Employee.City ASC, Employee.Email DESC
    LIMIT 10

'''

try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    pprint.pprint(cur.fetchall())
except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()