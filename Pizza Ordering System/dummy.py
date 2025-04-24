import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pizza_odering_system"
)

mycursor=mydb.cursor()

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
        print("Enter your task: 1.order product 2.view ordered product. 3.delete ordered product 4.update ordered product 5.Exit")
        task=input("Enter Task:")
        if task=="1":
            sql="SELECT product_name,product_price FROM products"
            mycursor.execute(sql)
            products=mycursor.fetchall()

            print("Available Products:")
            for product in products:
                print(f"{product[0]} - Price: {product[1]}")
            p_name=input("Enter Product name:")

            sql="SELECT product_price FROM products WHERE product_name=%s"
            mycursor.execute(sql,(p_name,))
            p_price=mycursor.fetchone()[0]

            quantity=int(input("Enter the Quantity:"))
            print("Select the size of the pizza for Small=s/Medium=m/Large=l")
            size_p=input("Enter the size of the pizza:")
            lagre=100
            medium=80
            if size_p=="s":
                size="Regular size"
                size_charge=0
            elif size_p=="m":
                size="Medium size"
                size_charge=medium
            elif size_p=="l":
                size="Large size"
                size_charge=lagre
            else:
                print("Select valid size")

            topping=input("Do you Want Extra Topping?:(y/n)")
            extra_topping=20
            if topping=="y":
                print(f"{p_name} {size} with Extra Topping")
                total_price=((p_price+size_charge)*quantity)+(extra_topping*quantity)
            else:
                print(f"{p_name} {size}")
                total_price=(p_price*quantity)

            print(f"Total Price to Pay:{total_price}")
            size_p=(size_p.capitalize())
            sql="INSERT INTO orderss(customer_name,product_name,quantity,product_price,size_p,order_status) VALUES (%s,%s,%s,%s,%s,%s)"
            values=(user__name,p_name,quantity,total_price,size_p,'Under Process')
            mycursor.execute(sql,values)
            mydb.commit()
            print("-------Order Placed Successful-------")

