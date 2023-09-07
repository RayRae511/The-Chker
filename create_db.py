import sqlite3


conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
Date DATE,
Description TEXT,
Category TEXT,
Price REAL)""")
            
conn.commit()
conn.close()