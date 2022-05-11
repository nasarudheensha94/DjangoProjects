import mysql.connector as c
db = c.connect(host= "localhost", user= "root", passwd= "H0twh33l$", database= "alshalawi")
cur = db.cursor()

def display():
    cur.execute("Select * from employees ")
    record = cur.fetchall()
    for i in record:
        print(i)

def Viewrecord():
    cur.execute("Select distinct name from employees ")
    record = cur.fetchall()
    for i in record:
        print(i)

def Addrecord():
    cur.execute("insert into employees values( 10, 'Vasim', 11000, 'Saloon','thurki')")
    db.commit()
    print(" record added successfully")


def delete():
    cur.execute(" delete from employees where empid=3 ")
    db.commit()
    print(" record deleted successfully")

def update():
    cur.execute(" update employees set dept='Jubail' ")
    db.commit()
    print(" record updated successfully")

def Addcolumn():
    cur.execute(" Alter Table employees Add Alternate_city varchar(25) ")
    db.commit()
    print(" attribute added successfully")

def Rencolumn():
    cur.execute(" ALTER Table Trainy rename to Employees ")
    db.commit()
    print(" attribute added successfully")
    
def menu():
    choice= "y"
    while choice == 'y':
        print(" press 1. display")
        print(" press 2. ViewRecord")
        print(" press 3. AddRecord")
        print(" press 4. delete")
        print(" press 5. update")
        print(" press 6. add column")
        print(" press 7. Rename column")
        print(" press 8. exit")
        do= int(input("Enter your choice "))
        if do== 1:
            display()
        elif do== 2:
            Viewrecord()
        elif do== 3:
            Addrecord()
        elif do== 4:
            delete()
        elif do== 5:
            update()
        elif do== 6:
            Addcolumn()
        elif do== 7:
            Rencolumn()    
        elif do== 8:
            print("----exit---")
            break
        else:
            print("invalid choice")
menu()

