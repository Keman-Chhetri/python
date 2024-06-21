import sqlite3
conn = sqlite3.connect('college.sqlite3')
cursor=conn.cursor()


cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               address TEXT NOT NULL
               )

 """)
conn.commit()



def insert_students(name,email,address):
     cursor.execute("""
         INSERT INTO students (name,email,address)
         VALUES(?,?,?)
                """,(name,email,address))
     conn.commit()
     print("data inserted successfully")


# def delete(id):
#      cursor.execute("""
#           DELETE FROM students WHERE id=?
# """,(id,))
#      conn.commit
#      print("Data deleted successfully")
# delete(1)
 
name=input("Enter Name")
email=input("Enter Email")
address=input("Address")
insert_students(name,email,address)
 
def show_students():
     cursor.execute("""
          SELECT *FROM students
     """)
     students = cursor.fetchall()
     print(students)
     



show_students()
