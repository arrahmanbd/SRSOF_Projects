import sqlite3

def create_connection(database_name):
    return sqlite3.connect(database_name)

def create_table(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS students(student_roll INT PRIMARY KEY, name VARCHAR(50),marks INT)")


