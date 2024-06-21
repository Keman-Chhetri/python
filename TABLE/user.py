import sqlite3
conn = sqlite3.connect('TABLE/user.sqlite3')
cursor=conn.cursor()

cursor.execute("""
     INSERT TABLE IF NOT EXISTS user(
               ID INTEGER PRIMARY KEY AUTOINCREMENT
               
               )

""")






