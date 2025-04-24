import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="boutiqye_management"
)

mycursor=mydb.cursor()

def add_task(id,name,username,password,email):
    mycursor=mydb.cursor()
    id=input("Create Id:")
    name=input("Enter Name:")
    username=input("Create Username:")
    password=input("Creaye Password:")
    email=input("Enter Id:")
    sql="INSERT INTO employees(id,name,username,password,email) VALUES (%s,%s,%s,%s,%s)"
    values=(id,name,username,password,email)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Execution Seccessful")
