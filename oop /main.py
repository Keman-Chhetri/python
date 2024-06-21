# class Laptop:
#     price=938398
#     def bran(self):
#         print(self.price)
#         print("Dell")

#     def add(self,x,y):
#         return x+y
    

# obj=Laptop()
# 





# class Calculator:

#     def add(self,x,y):
#         return x+y
#     def substract(self,x,y):
#         return x-y
#     def multiply(self,x,y):
#         return x*y
#     def divide (self,x,y):
#         return x/y
# obj=Calculator()
# print("1.Add 2.Substract 3.Multiply 4. Divide")
# z=int(input("Enter Your Choice"))
# if z==1:
#     x=int(input("Enter first number"))
#     y=int(input("Enter Second Number"))
#     print(obj.add(x,y))

# elif z==2:
#     x=int(input("Enter first number"))
#     y=int(input("Enter Second Number"))
#     print(obj.substract(x,y))

# elif z==3:
#     x=int(input("Enter first number"))
#     y=int(input("Enter Second Number"))
#     print(obj.multiply(x,y))




# import sqlite3
# con = sqlite3.connect('oop/product.sqlite3')
# cursor=con.cursor()

# def create_table():
#     cursor.execute("""
#       CREATE TABLE IF NOT EXISTS product(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT
#                    name TEXT NOT NULL
#                    price INTEGER NOT NULL
#                    quantity INTEGER NOT NULL)

# """)
# con.commit()   



# def insert_students(name,email,address):
#      cursor.execute("""
#          INSERT INTO students (name,pricequantity)
#          VALUES(?,?,?)
#                 """,(name,email,address))
#      con.commit()
#      print("data inserted successfully")



# class Laptop:
#     def __init__(self,name):
#         print("I am ",name)

#     def __str__(self):
#         return f'Company({self.name})'
#     print(Company)
    
    




# obj=Laptop('Keman')