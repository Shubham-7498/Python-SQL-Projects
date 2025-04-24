import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizza_odering_system"
)

mycursor=mydb.cursor()

print("Select your role 1.Employer 2.Customer")
role=input("Enter your role:")
user="admin"
passs="admin"
if role=="1":
    print("Enter Username and Password")
    username=input("username:")
    password=input("password:")
    if username==user and password==passs:
        print("--------Wemcome Emolpyer!--------")
        while True:
            print("Enter your task: 1.add product 2.view product. 3.delete product 4.update product 5. update status 6.End Task")
            task=input("Enter Task:")
            if task=="1":
                id=int(input("Create Id:"))
                product_name=input("Enter Product Name:")
                product_description=input("Enter Product Descroption:")
                product_price=input("Enter Product Price:")
                sql="INSERT INTO products(id,product_name,product_desc,product_price) VALUES (%s,%s,%s,%s)"
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
                sql="UPDATE products SET id=%s, product_name=%s ,product_desc=%s ,product_price=%s WHERE ID=%s"
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
                new_status=input("Status:")
                sql= "UPDATE orderss set order_status=%s WHERE id=%s"
                values=(new_status,order_id)
                mycursor.execute(sql,values)
                mydb.commit()
                print("-------Status Updated Sucessfully-------")
            elif task=="6":
                print("---------End of Task-------")
                break
            else:
                print("Invalid Task")
    else:
        print("Invalid Username and Password")
elif role=="2":
    print("1.Sign up/n2.Login in")
    register=input("Enter Option:")
    if register=="1":
        id=int(input("Create Id:"))
        name=input("Enter Name:")
        username=input("Create Username:")
        password=input("Create Password:")
        email=input("Enter Email id:")
        sql="INSERT INTO customers(customer_id,customer_name,username,password,email) VALUES (%s,%s,%s,%s,%s)"
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
                        product_name=input("Enter Product Name:")
                        quantity=int(input("Enter the quantity:"))
                        product_price=int(input("Enter the prize of Pizza:"))
                        print("Extra topping(yes=y/no=n):")
                        topping=input("Do you want extra topping!(y/n)")
                        extra_topping_price=20
                        if topping=="y":
                            print(f"-------{product_name} with extra topping-------")
                            extra_charge=extra_topping_price
                        else:
                            print(product_name)
                            extra_charge=0
                        print("Select the size of the pizza for Small=s/Medium=m/Large=l")
                        size_p=input("Enter the size of the pizza:")
                        lagre_size=100
                        medium_size=80
                        if size_p=="s":
                            print(f"-------{product_name} small-------")
                            size_charge=0
                        elif size_p=="m":
                            print(f"-------{product_name} medium-------")
                            size_charge=medium_size
                        elif size_p=="l":
                            print(f"-------{product_name} large-------")
                            size_charge=lagre_size
                        else:
                            print("Select valid size")
                        total_price=((product_price+size_charge)*quantity)+(extra_charge*quantity)
                        print(f"Total price to pay:{total_price}")
                        size_p=(size_p.capitalize())
                        sql="INSERT INTO orderss(product_name,quantity,product_price,size_p,order_status,customer_name) VALUES (%s,%s,%s,%s,%s,%s)"
                        values=(product_name,quantity,total_price,size_p,'Under Process',user__name)
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
                        break
                    else:
                        print("Invalid Task")
            else:
                print("-------Incorrect Password-------")
        else:
            print("-------Username Not Found-------")
    else:
        print("Enter valid option")
else:
    print("Invalid Role")