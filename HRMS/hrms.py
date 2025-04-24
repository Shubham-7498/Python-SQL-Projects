import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hrm_system"
)

mycursor=mydb.cursor()

user_name="admin"
pass_word="admin"

print("login")
print("1.Hr 2.Employee")
role=input("Select option for login:")

if role=="1":
    username=input("User name:")
    password=input("Password:")

    if username==user_name and password==pass_word :
        print("Welcome HR!")

        while True:
            print("1.Mark Attendance 2.Record Salary Payment 3.Manage Leave Request 4.Exit")
            action=input("Select option:")

            if action=="1":
                print("Mark Attendance")

                emp_name=input("Enter employee name to mark attendance:")
                sql="SELECT name FROM employees WHERE name=%s"
                mycursor.execute(sql,(emp_name,))
                result=mycursor.fetchone()
                if result:
                    name=result[0]
                    sql="INSERT into attendance(employee_name, remark) VALUES(%s,%s)"
                    value=(name,'Present')
                    mycursor.execute(sql,value)
                    mydb.commit()
                    print("Attendance Marked Sucessfully!")
                else:
                    print("Employee not found!")    

            elif action=="2":
                print("Salary Payment")
                emp_name=input("Enter employee name for salary payment:")
                sql="SELECT name,salary FROM employees WHERE name=%s"
                mycursor.execute(sql,(emp_name,))
                results=mycursor.fetchall()
                for result in results:
                    print(f"Name:{result[0]} ,Salary: {result[1]}")
                if results:
                    name=result[0]
                    salary=int(input("Enter Salary:"))
                    if salary==result[1]:
                        sql="INSERT into salary_record(employee_name, salary) VALUES(%s,%s)"
                        value=(name,salary)
                        mycursor.execute(sql,value)
                        mydb.commit()
                        print("Salary paid Sucessfully!")
                    else:
                        print("Enter valid Salary!")
                else:
                    print("Employee not found!")

            elif action=="3":
                print("Manage leave request")
                sql="SELECT * FROM leave_request WHERE status='Pending'"
                mycursor.execute(sql) 
                results=mycursor.fetchall()
                for result in results:
                    print(result)
                
                ep_name=input("Enter Employee name:")
                state=input("Enter request status to be updated:")
                sql="UPDATE leave_request SET status=%s WHERE employee_name=%s"
                values=(state,ep_name)
                mycursor.execute(sql,values)
                mydb.commit()
                print("Status updated Sucessfully!")

            elif action=="4":
                print("Exit")
                break
            
            else:
                print("Selet valid option!")
    else:
        print("Incorrect Username & Password!")

elif role=="2":
    print("1.Signup 2.Login")
    e_role=input("Select Option:")
    
    if e_role=="1":
        print("Signup")
        ename=input("Enter Name:")
        u_name=input("Enter Username:")
        department=input("Enter Department:")
        designation=input("Enter Designation:")
        salary=int(input("Enter Salary:"))

        sql="INSERT into employees(name,username,department,designation,salary) VALUES(%s,%s,%s,%s,%s)"
        values=(ename,u_name,department,designation,salary)
        mycursor.execute(sql,values)
        mydb.commit()

    elif e_role=="2":    
        user__name=input("Username:")

        sql="SELECT username FROM employees WHERE username=%s"
        mycursor.execute(sql,(user__name,))
        result=mycursor.fetchone()

        if result:
            for x in result:
                print(f"Welcome {user__name}!")
                while True:
                    print("1.View Details 2.View Salary report 3.View Attendance report 4.Apply for Leave 5.view Leave Request status 6.Exit")
                    task=input("Enter task:")
                    if task=="1":
                        print("Details")
                        sql="SELECT * FROM employees Where username=%s"
                        mycursor.execute(sql,(user__name,))
                        details=mycursor.fetchall()
                        for detail in details:
                            print(f"Name: {detail[0]}, Department: {detail[1]}, Designation: {detail[2]}, Salary: {detail[3]} Join date: {detail[5]}")

                    elif task=="2":
                        print("Salary Report")
                        sql="SELECT name FROM employees WHERE username=%s"
                        mycursor.execute(sql,(user__name,))
                        result=mycursor.fetchone()[0]
                        sql="SELECT * FROM salary_record Where employee_name=%s"
                        mycursor.execute(sql,(result,))
                        infos=mycursor.fetchall()
                        for info in infos:
                            print(f"Name: {info[0]}, Salary: {info[1]} Date: {info[2]}")

                    elif task=="3":
                        print("Attendance report")
                        sql="SELECT name FROM employees WHERE username=%s"
                        mycursor.execute(sql,(user__name,))
                        result=mycursor.fetchone()[0]
                        sql="SELECT * FROM attendance Where employee_name=%s"
                        mycursor.execute(sql,(result,))
                        infos=mycursor.fetchall()
                        for info in infos:
                            print(f"Name: {info[0]}, Remark: {info[1]} Date: {info[2]}")

                    elif task=="4":
                        print("Apply for Leave")
                        reason=input("Enter reason:")

                        sql="SELECT name FROM employees WHERE username=%s"
                        mycursor.execute(sql,(user__name,))
                        result=mycursor.fetchone()[0]

                        sql="INSERT into leave_request(employee_name,reason,status) VALUES(%s,%s,%s)"
                        values=(result,reason,'Pending')
                        mycursor.execute(sql,values)
                        mydb.commit()
                        print("Leave request subbmitted sucessfully")

                    elif task=="5":
                        print("view Leave Request status")
                        sql="SELECT name FROM employees WHERE username=%s"
                        mycursor.execute(sql,(user__name,))
                        result=mycursor.fetchone()[0]

                        sql="Select * FROM leave_request Where employee_name=%s"
                        mycursor.execute(sql,(result,))
                        out=mycursor.fetchall()
                        for x in out:
                            print(f"Name:{x[0]}, Reason:{x[1]}, Date:{x[2]}, Status:{x[3]}")

                    elif task=="6":
                        print("Exit")
                        break

                    else:
                        print("Select valid option!")
        else:
            print("Invalid Username!")

    else:
        print("Select valid option!")

else:
    print("Select valid role!")