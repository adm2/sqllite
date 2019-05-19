import pprint
import sys
import sqlite3 as lite

data = ''

con = None

query_string = '''
    SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName, Customer.Phone, Customer.Company
    FROM Customer
    LEFT JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId








    ORDER BY Employee.City ASC, Employee.Email DESC


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