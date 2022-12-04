import mysql.connector as sql 
import time as t 
import random as R
import pandas as pd
import csv as c 

mysql = sql.connect(host = "localhost",user="root",password = "",database="Railway")

mycursor=mysql.cursor()
sa = "create database if not exists railway"
mycursor.execute(sa)
def work():
                add = int(input('''Please choose what to update
                                        1. Train Details
                                        2. Train Details Deletion
                                        \n: '''))
                if add == 1:
                    enter = input("Enter Train name : ")
                    print("Route :- ")
                    dest = input('''From : ''')
                    to = input("to: ")
                    example = []
                    Train_no = R.randrange(99999,999999)
                    example.append(enter)
                    example.append(Train_no)
                    example.append(dest)
                    example.append(to)
                    e = (example)
                    new_tab = "create table if not exists train(train_name varchar(255),train_no varchar(255),F varchar(255),T varchar(255))"
                    mycursor.execute(new_tab)
                    insertia = "INSERT INTO train(train_name,train_no,F,T) VALUES (%s,%s,%s,%s)"
                    mycursor.execute(insertia,e)
                    a = "SELECT * FROM train"
                    mycursor.execute(a)
                    for i in mycursor:
                        print("")
                        a = ["Train Name","Train No.","Journey From","Destination"]
                        run = pd.DataFrame([i],columns=a,index=[""])
                        print(run)
                        print("")
                    print("Succesfully added !!!")
                    mysql.commit()
                    print("Want to add More ")
                    YES = input("YES OR NO .. (Type Y/N) \n")
                    if YES == "Y":
                        work()
                    else:
                        print("Thanks !!!!!!")
                elif add == 2: 
                    b = "SELECT * FROM train"
                    mycursor.execute(b)
                    for i in mycursor:
                        print("")
                        a = ["Train Name","Train No.","Journey From","Destination"]
                        run = pd.DataFrame([i],columns=a,index=[""])
                        print(run)
                        print("")
                    mysql.commit()
                    print("Which Train Has to Be Deleted From Above List")
                    train_no = input("Enter Train Number : ")
                    tr = (train_no,)
                    x = "delete from train where train_no = (%s)"
                    mycursor.execute(x,tr)
                    v = "SELECT * FROM train"
                    mycursor.execute(v)
                    t.sleep(1)
                    for i in mycursor:
                        print("")
                        a = ["Train Name","Train No.","Journey From","Destination"]
                        run = pd.DataFrame([i],columns=a,index=[""])
                        print(run)
                        print("")
                    mysql.commit()
                    print("Want to add More ")
                    YES = input("YES OR NO .. (Type Y/N) \n")
                    if YES == "Y":
                        work()
                    else:
                        print("Thanks !!!!!!")


def reservation():
                l1=[]
                np=int(input("Enter number of passenger : "))
                pname=input("enter passenger name = ")
                l1.append(pname)
                age=input("enter age of passenger = ")
                l1.append(age)
                a = "select * from train"
                mycursor.execute(a)
                r = mycursor.fetchall()
                for i in r:
                    print(i)
                trainno=input("enter train number = ")
                l1.append(trainno)
                l1.append(np)
                print("select a class you would like to travel in")
                print("1.AC FIRST CLASS")
                print("2.AC SECOND CLASS")
                print("3.AC THIRD CLASS")
                print("4.SLEEPER CLASS")
                cp=int(input("Enter your choice:"))
                if cp == 1:
                                amount = np*1000
                                cls = 'AC 1'
                elif cp == 2:
                                amount = np*800
                                cls = "AC 2"
                elif cp == 3:
                                amount = np*500
                                cls = 'AC 3'
                else:
                                amount=np*350
                                cls='Sleeper'
                l1.append(cls)           
                print("Total amount to be paid:",amount)
                l1.append(amount)
                pnr = R.randrange(99999,999999)
                print("PNR Number:",pnr)
                print("status: confirmed")
                sts='confirmed'
                l1.append(sts)
                l1.append(pnr)
                train1=(l1)
                cr = "create table if not exists passengers(pname varchar(183),age varchar(183),trainno varchar(183),noofpas varchar(183),cls varchar(183),amt varchar(183),status varchar(183),pnrno varchar(183),primary key(pnrno))"
                sql="insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(cr)
                t.sleep(1)
                mycursor.execute(sql,train1)
                join = "select * from train,passengers where train.train_no = passengers.trainno"
                mycursor.execute(join)
                for y in mycursor:
                    column = ["Train Name","Train No.","From","To","Passenger Name","Age","Train no","No of seat","Class","Amount","Status","PNR"]
                    a = pd.DataFrame([y],columns=column,index=[""])                    
                    print("TICKET")
                mysql.commit()
                print("insertion completed")
                print("Go back to menu OR Skip")
                opt = input("Y for menu or N to Skip : ")
                if opt == "Y":
                    print("\n")
                    railresmenu()
                    t.sleep(1)
                print('\n' *2)

                print("===================================================================" * 3)
def cancel():
                print("Ticket cancel window")
                pnr=input("enter PNR for cancellation of Ticket")
                pn=(pnr,) 
                sql="update passengers set status='deleted' where pnrno=%s"
                mycursor.execute(sql,pn)
                mysql.commit()
                print("Deletion completed")
                print("Go back to menu OR Skip")
                opt = input("Y for menu or N to Skip : ")
                if opt == "Y":
                    print("\n")
                    railresmenu()
                    t.sleep(1)
                print('\n' *2)

                print("==================================================================="* 3)
def displayPNR():
                print("PNR STATUS window")
                pnr=input("enter PNR NUMBER")
                pn=(pnr,) 
                sql= "select * from passengers where pnrno=%s "
                mycursor.execute(sql,pn) 
                #mydb.commit()
                print("PNR STATUS are as follows : ")
                for x in mycursor:
                                x1 = [x]
                                y = pd.DataFrame(x1,columns=["Name","Age","Train no.","No of passenger","Class","Amount","Status","PNR"],index=[""])
                                print(y)   
                #print("Deletion completed")
                print("Go back to menu OR Skip ")
                opt = input("Y for menu or N to ")
                if opt == "Y":
                    print("\n")
                    railresmenu()
                    t.sleep(1)
                print('\n' *2)
                print("==================================================================="* 3)

def railresmenu():
    print("Welcome To IRCTC !!!!! \n")
    print("Railway Reservation ")
    print("1.Reservation of Ticket")
    print("2.Cancellation of Ticket")
    print("3.Display PNR status")
    print("4.Quit")
    n=int(input("enter your choice : "))
    if(n==1):
                    reservation()
    elif(n==2):
                    cancel()
    elif(n==3):
                    displayPNR()
    elif(n==4):
                    print("Done")
    print("\n")
    t.sleep(1.5)


def sign_in():
                Name = input("Enter Your Name : ")
                Age = input("Enter Your Age : ")
                Sex = input("Enter Your Sex M/F : ")
                Mob = input("Enter Your Mobile no : ")
                if len(Mob) == 10:
                    print("")
                else:
                    print("Plzz input correct no.")
                det = [Name,Age,Mob]
                if Sex == "M":
                    det.append("Male")
                else:
                    det.append("Female")
                print("Please set a password of mininmum 6 digits : ")
                pswad = input("")
                det.append(pswad)
                deta = (det)
                w = "create table if not exists user(Name varchar(183),Age varchar(183),Sex varchar(6),Mob varchar(183),Password varchar(183),unique(Mob))"
                w1 = "insert into user(Name,Age,Mob,Sex,Password) values(%s,%s,%s,%s,%s)"
                mycursor.execute(w)
                mycursor.execute(w1,deta)
                mysql.commit()
                railresmenu()

def sign_up():
                x1 = "select Password from user"
                mycursor.execute(x1)
                a1 = mycursor.fetchall()
                for i in a1:
                    print()
                Q  = input("Enter your password : ")
                Q2 = (Q,)
                x2 = "select * from user where Password = %s"
                mycursor.execute(x2,Q2)
                for i in mycursor:
                        print("Name :",i[0])
                        print("Age :",i[1])
                        print("Sex :",i[2])
                        print("Mobile no :",i[3])
                        print("")
                        railresmenu()

def users():
            print("Please Sign In \n If doesn't have account go to different portal:")
            OPTION = input("Want to \n1. Sign In \n2. Sign UP : ")
            if OPTION == "1":
                sign_in()
            elif OPTION == "2":
                sign_up()




print("\t Please login first ! \t")
log = input("""Want to Sign as :
                1.Admin
                2.User
                : """)

if log == "Admin":
    print("Please enter password,")
    pswd = int(input(": "))
    if pswd == 130805:
        print("Correct Password !")
        print("Welcome to IRCTC !!!!!! in Admin mode")
        t.sleep(2)
        work()
elif log == "user":
    users()
