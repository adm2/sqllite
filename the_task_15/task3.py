import pprint
import sys
import sqlite3 as lite

data = ''

con = None

query_string = '''
    select distinct G.Name
    from Genre G
    join Track T on T.GenreId = G.GenreId
    join InvoiceLine I on I.TrackId = T.TrackId

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