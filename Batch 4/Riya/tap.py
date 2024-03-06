import sqlite3

db = sqlite3.connect("mydb.db")
db.execute(
    '''
CREATE TABLE IF NOT EXISTS mytable(
id INTEGER PRIMERY KEY,
name TEXT,
roll INTEGER,
)

'''
)


