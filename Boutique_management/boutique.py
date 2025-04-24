import mysql.connector
import moduless
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="boutiqye_management"
)

mycursor=mydb.cursor()
user_name="admin"
password="admin"

print("enter your role: 1.Employer 2.Employee 3.Customer")
role=input("Enter your role:")

if role=="1":
    print("Enter Username and password:")
    username=input("Username:")
    pass_word=input("Password:")
    if user_name==username and password==pass_word:
        print("------Welcome Employer!------")
    while True:
        print("Enter your task: 1.add 2.view. 3.delete 4.update 5.Exit")
        task=input("Enter Task:")

        if task=="1":
            id=int(input("Create Id:"))
            name=input("Enter Name:")
            username=input("Create Username:")
            password=input("Create Password:")
            email=input("Enter Email id:")
            sql="INSERT INTO employees(id,name,username,password,email) VALUES (%s,%s,%s,%s,%s)"
            values=(id,name,username,password,email)
            mycursor.execute(sql,values)
            mydb.commit()
            print("-------Execution Seccessful-------")
        elif task=="2":
            sql="SELECT * FROM employees"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            for x in result:
                print(x)
            print("-------Execution Seccessful-------")
        elif task=="3":
            print("-------Which ID you Want to Delete from Database-------")
            x=input("Enter ID no.:")
            sql="DELETE From employees WHERE id=%s"
            val=(x,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("-------Execution Seccessful-------")
        elif task=="4":
            old_id=input("Enter the id you want to update:")
            new_id=int(input("Enter the new id:"))
            new_name=input("Enter the new name:")
            new_usrename=input("Enter the new username:")
            new_password=input("Enter the new password:")
            new_email=input("Enter the new email:")
            sql="UPDATE employees SET id=%s, name=%s ,username=%s ,password=%s, email=%s WHERE ID=%s"
            values=(new_id,new_name,new_usrename,new_password,new_email,old_id)
            mycursor.execute(sql,values)
            mydb.commit()
            print("-------Updated Sucessfully-------")
        elif task=="5":
            print("--------End of Task-------")
            break
        else:
            print("Invalid Task")
    else:
        print("Invalid Username and Password!")
elif role=="2":
    print("Enter given Username and Password")
    user__name=input("Username:")
    pass__word=input("Password:")
    sql="SELECT password FROM employees WHERE username=%s"
    mycursor.execute(sql,(user__name,))
    result=mycursor.fetchone()
    if result:
        db_password=result[0]
        if pass__word==db_password:
            print("-------Login Successful-------")
            print("------Welcome",user__name,"!------")
            while True:
                print("Enter your task: 1.add product 2.view product. 3.delete product 4.update product 5. update status 6.Exit")
                task=input("Enter Task:")
                if task=="1":
                    id=int(input("Create Id:"))
                    product_name=input("Enter Product Name:")
                    product_description=input("Enter Product Descroption:")
                    product_price=input("Enter Product Price:")
                    sql="INSERT INTO products(id,product_name,product_description,product_price) VALUES (%s,%s,%s,%s)"
                    values=(id,product_name,product_description,product_price)
                    mycursor.execute(sql,values)
                    mydb.commit()
                    print("-------Execution Seccessful-------")
                elif task=="2":
                    sql="SELECT * FROM products"
                    mycursor.execute(sql)
                    result=mycursor.fetchall()
                    for x in result:
                        print(x)
                    print("-------Execution Seccessful-------")
                elif task=="3":
                    print("-------Which ID you Want to Delete from Database-------")
                    x=input("Enter ID no.:")
                    sql="DELETE From products WHERE id=%s"
                    val=(x,)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("-------Execution Seccessful-------")
                elif task=="4":
                    old_id=input("Enter the Product id you want to update:")
                    new_id=int(input("Enter the new id:"))
                    new_name=input("Enter the new name:")
                    new_desc=input("Enter the description:")
                    new_price=input("Enter the new price:")
                    sql="UPDATE products SET id=%s, product_name=%s ,product_description=%s ,product_price=%s WHERE ID=%s"
                    values=(new_id,new_name,new_desc,new_price,old_id)
                    mycursor.execute(sql,values)
                    mydb.commit()
                    print("-------Updated Sucessfully-------")
                elif task=="5":
                    sql="Select * FROM orderss where order_status='Under Process'"
                    mycursor.execute(sql)
                    a=mycursor.fetchall()
                    for x in a:
                        print(x)
                    order_id=int(input("Enter the order id you want to update status:"))
                    new_status="Dispatched"
                    sql= "UPDATE orderss set order_status=%s WHERE id=%s"
                    values=(new_status,order_id)
                    mycursor.execute(sql,values)
                    mydb.commit()
                    print("-------Status Updated Sucessfully-------")
                elif task=="6":
                    print("-------End of Task-------")
                    break
                else:
                    print("Invalid Task")
        else:
            print("-------Incorrect Password-------")
    else:
        print("-------Username Not Found-------")
elif role=="3":
    print("1.Sign up/n2.Login in")
    register=input("Enter Option:")
    if register=="1":
        id=int(input("Create Id:"))
        name=input("Enter Name:")
        username=input("Create Username:")
        password=input("Create Password:")
        email=input("Enter Email id:")
        sql="INSERT INTO customers(id,name,username,password,email) VALUES (%s,%s,%s,%s,%s)"
        values=(id,name,username,password,email)
        mycursor.execute(sql,values)
        mydb.commit()
        print("-------Execution Seccessful-------")
    elif register=="2":
        print("Enter Username and Password")
        user__name=input("Username:")
        pass__word=input("Password:")
        sql="SELECT password FROM customers WHERE username=%s"
        mycursor.execute(sql,(user__name,))
        result=mycursor.fetchone()
        if result:
            db_password=result[0]
            if pass__word==db_password:
                print("-------Login Successful-------")
                print("------Welcome",user__name,"------")
                while True:
                    print("Enter your task: 1.order product 2.view ordered product. 3.delete ordered product 4.update ordered product 5.Exit")
                    task=input("Enter Task:")
                    if task=="1":
                        sql="SELECT * FROM products"
                        mycursor.execute(sql)
                        result=mycursor.fetchall()
                        for x in result:
                            print(x)
                        id=int(input("Enter Id:"))
                        product_name=input("Enter Product Name:")
                        product_price=input("Enter Price to Pay:")
                        sql="INSERT INTO orderss(id,product_name,product_price,order_status,customer_name) VALUES (%s,%s,%s,%s,%s)"
                        values=(id,product_name,product_price,'Under Process',user__name)
                        mycursor.execute(sql,values)
                        mydb.commit()
                        print("-------Order Placed Successful-------")
                    elif task=="2":
                        sql="SELECT * FROM orderss Where customer_name=%s"
                        mycursor.execute(sql,(user__name,))
                        result=mycursor.fetchall()
                        for x in result:
                            print(x)
                        print("-------Execution Seccessful-------")
                    elif task=="3":
                        print("-------Which ID you Want to Delete from Database-------")
                        x=input("Enter ID no.:")
                        sql="DELETE From orderss WHERE id=%s"
                        val=(x,)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("-------Execution Seccessful-------")
                    elif task=="4":
                        product_id=input("Enter the id you want to update")
                        new_id=int(input("Enter the new id:"))
                        new_name=input("Enter the new name:")
                        new_price=input("Enter the new price:")
                        sql="UPDATE orderss SET id=%s, product_name=%s ,product_price=%s WHERE ID=%s"
                        values=(new_id,new_name,new_price,product_id)
                        mycursor.execute(sql,values)
                        mydb.commit()
                        print("-------Updated Sucessfully-------")
                    elif task=="5":
                        print("-------End of Task-------")
                    else:
                        print("Invalid Task")
            else:
                print("-------Incorrect Password-------")
        else:
            print("-------Username Not Found-------")
    else:
        print("Enter valid option")
else:
    print("Invalid role!")