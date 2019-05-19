import pprint
import sys
import sqlite3 as lite

data = ''

con = None

query_string = '''
    SELECT FirstName, Phone
    FROM Customer 
    LEFT JOIN Invoice 
        ON Customer.CustomerID = Invoice.CustomerID   
    LEFT JOIN InvoiceLine 
        ON InvoiceLine.InvoiceID = Invoice.InvoiceID    
    WHERE InvoiceLine.UnitPrice = (SELECT max(InvoiceLine.UnitPrice) FROM InvoiceLine)
    ORDER BY FirstName
'''

try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    con.commit()
    pprint.pprint(cur.fetchall())

except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()