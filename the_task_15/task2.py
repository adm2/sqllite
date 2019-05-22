import pickle
import sys
import sqlite3 as lite
import pprint
data = ''

con = None

query_string = '''

'''

try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    pickle_data = cur.fetchall()
    pprint.pprint(pickle_data)

except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()
