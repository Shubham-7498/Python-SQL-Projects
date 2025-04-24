import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banking_management"
)

mycursor=mydb.cursor()

print("1.Create Account 2.Login into A/c")
task=input("Select the option:")
if task=="1":
    print("Creating a A/c")
    print("\n")
    ac_holder_name=input("Enter Full Name:")
    phone_no=int(input("Enter Phone No:"))
    initial_deposit=int(input("Enter Deposit Amount:"))
    if initial_deposit>=5000:
        current_balance=initial_deposit
        print("Deposit Accepted")
        sql="INSERT INTO customers(holder_name,phone_no,initial_deposit,Balance) values(%s,%s,%s,%s)"
        values=(ac_holder_name,phone_no,initial_deposit,current_balance)
        mycursor.execute(sql,values)
        mydb.commit()

        sql="INSERT INTO transactions (holder_name, transaction_type, amount) VALUES(%s, %s, %s)"
        values=(ac_holder_name,'Initial Deposit',initial_deposit)
        mycursor.execute(sql,values)
        mydb.commit()

        print("Account Created Sucessfully!")
    else:
        print("Deposit must be at least 5000")

elif task=="2":
    print("Login inti A/c")
    print("\n")
    user_name=input("Enter A/c Holder Name:")

    sql="SELECT holder_name,phone_no,initial_deposit,Balance FROM customers WHERE holder_name=%s"
    mycursor.execute(sql,(user_name,))
    result=mycursor.fetchall()
    if result:
        for x in result:
            print(f"--------Welcome {user_name}!--------")
            print(f"A/c Holder Name:{x[0]}\nPhone no:{x[1]}\nInitial Deposit:{x[2]}\nCurrent Balance:{x[3]}")
        print("\n")
        
        while True:
            print("Select Task:\n1.Deposit Money\n2.Withdraw Money\n3.View Transaction History\n4.Delete Account\n5.Exit")
            do_task=input("Select option:")
            if do_task=="1":
                print("Deposit Money")
                sql="SELECT balance from customers WHERE holder_name=%s"
                mycursor.execute(sql,(user_name,))
                result=mycursor.fetchone()[0]
                ammount=int(input("Enter amount to be deposited:"))
                new_balance=result+ammount

                sql="UPDATE customers SET Balance=%s WHERE holder_name=%s"
                value=(new_balance,user_name)
                mycursor.execute(sql,value)
                mydb.commit()
                print("Amount has been Deposited")
                print(f"Your Current Balance:{new_balance}")

                sql="INSERT INTO transactions (holder_name, transaction_type, amount, balance) VALUES(%s, %s, %s, %s)"
                values=(user_name,'Deposit',ammount,new_balance)
                mycursor.execute(sql,values)
                mydb.commit()

            elif do_task=="2":
                print("Withdraw Money")
                sql="SELECT balance from customers WHERE holder_name=%s"
                mycursor.execute(sql,(user_name,))
                result=mycursor.fetchone()[0]
                ammount=int(input("Enter amount to be withdraw:"))
                if ammount<=result:
                    n_balance=result-ammount
                    sql="UPDATE customers SET Balance=%s WHERE holder_name=%s"
                    value=(n_balance,user_name)
                    mycursor.execute(sql,value)
                    mydb.commit()
                    print("Amount has been Withdrawl")
                    print(f"Your Current Balance:{n_balance}")

                    sql="INSERT INTO transactions (holder_name, transaction_type, amount, balance) VALUES(%s, %s, %s, %s)"
                    values=(user_name,'Withdrawl',ammount,n_balance)
                    mycursor.execute(sql,values)
                    mydb.commit()
                else:
                    print("Insufficent Balance!")

            elif do_task=="3":
                print("Transaction History")
                sql="SELECT transaction_date, transaction_type, amount, balance FROM transactions WHERE holder_name=%s"
                mycursor.execute(sql,(user_name,))
                transactions=mycursor.fetchall()

                for transaction in transactions:
                    print(f"Date: {transaction[0]}, Type: {transaction[1]}, Amount: {transaction[2]}, Balance: {transaction[3]}")
                
            elif do_task=="4":
                print("Delete Account")
                action=input("Are you sure you wan't to delete this Account(y/n):")
                if action=="y":
                    sql="DELETE FROM customers Where holder_name=%s"
                    mycursor.execute(sql,(user_name,))
                    mydb.commit()

                    sql="DELETE FROM transactions Where holder_name=%s"
                    mycursor.execute(sql,(user_name,))
                    mydb.commit()

                    print("Your Account has been Deleted")
                    break
                else:
                    print("Cancelled")

            elif do_task=="5":
                print("Exit")
                break

            else:
                print("Invalid Option!")
    else:
        print("Account Not Found!")       