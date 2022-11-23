class Car:
    def __init__(self, myid, myname):
        self.id = myid
        self.myname = myname
        self.price = 0
    def setPrice(self,newPrice):
        self.price = newPrice
    def __str__(self):
        return "{} {} ${}".format(self.id , self.myname, self.price) 

def Menu():
    print("1. Display all cars")
    print("2. Save New Car")
    print("3. Update Car Price")
    print("9. Quit")
    choice = int(input("Enter your choice"))
    return choice

import sqlite3
import sys
def displayCars():
    con = sqlite3.connect('test.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('Select * from cars')
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except:
            print("Error " )
            sys.exit(1)

def insertNewCar():
    myid = input("Car ID?")
    myName = input("Car Owner Name?")
    myPrice = input("price? (integer)")            
    c1 = Car(myid, myName)
    c1.setPrice(int(myPrice))
    con = sqlite3.connect('test.db')
    with con:
        try:
            cur = con.cursor()
            sql = 'insert into cars values({},"{}", {})'.format(
                  c1.id, c1.myname, c1.price)
            cur.execute(sql)
        except sqlite3.Error:
            print("Error " )
            sys.exit(1)

def updateCar():
    myid = input("Car ID?")
    con = sqlite3.connect('test.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('Select * from cars where id = {}'.format(myid))
            rows = cur.fetchall()
            c1 = Car(rows[0][0], rows[0][1])
            c1.setPrice(int(rows[0][2]))
            print(c1)
            price = int(input("New Price?"))
            cur.execute('update cars set price = {1} where id = {0}'.format(myid, price))
        except sqlite3.Error:
            print("Error " )
            sys.exit(1)
        
    

if __name__ =="__main__":
    try:
        import sqlite3
        con = sqlite3.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute('create table cars(id int, name text, price int)')
    except:
        print("Data exists")
    choice = Menu()
    while choice !=9:
        if choice ==1:
            displayCars()
        elif choice ==2:
            insertNewCar()
        elif choice ==3:
            updateCar()
        choice = Menu()
    



        
