import pickle
import sys
import sqlite3 as lite
import pprint
data = ''

con = None

query_string = '''
              SELECT e.FirstName, e.LastName, e.Phone, p.FirstName, p.LastName, p.Phone  
              FROM Employee as e, Employee as p 
              WHERE p.EmployeeID = e.ReportsTo 
'''

try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    pickle_data = cur.fetchall()
    pprint.pprint(pickle_data)
    pickle_file = open('pickle.data','wb')
    pickle.dump(pickle_data, pickle_file)
    pickle_file.close()
except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()
