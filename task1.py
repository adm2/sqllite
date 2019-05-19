import pprint
import sys
import sqlite3 as lite

data = ''

con = None

query_string = '''
    pass
'''

try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    con.commit()
    con.rollback()
    print('=================================')
    pprint.pprint(cur.fetchall())
    print('=================================')
    pprint.pprint(data)

except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()