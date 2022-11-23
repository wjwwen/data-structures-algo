import sqlite3
import sys

class Car:
    def __init__(self, myid, myname):
        self.id = myid
        self.myname = myname
        self.price = 0
    def setPrice(self,newPrice):
        self.price = newPrice
    def __str__(self):
        return "{} {} ${}".format(self.id , self.myname, self.price) 


class CarDA:
    def __init__(self):
        self.__tableName ="cars"
        try:
            import sqlite3
            con = sqlite3.connect('test.db')
            with con:
                cur = con.cursor()
                cur.execute(f'create table {self.__tableName}(id int, name text, price int)')
        except:
            pass
    def displayCars(self):
        con = sqlite3.connect('test.db')
        with con:
            try:
                cur = con.cursor()
                cur.execute(f'Select * from {self.__tableName}')
                rows = cur.fetchall()
                for row in rows:
                    print(row)
            except:
                print("Error " )
                sys.exit(1)    
    def insertNewCar(self,c1):
        con = sqlite3.connect('test.db')
        with con:
            try:
                cur = con.cursor()
                sql = f'insert into {self.__tableName} values({c1.id},"{c1.myname}", {c1.price})'
                cur.execute(sql)
            except sqlite3.Error:
                print("Error " )
                sys.exit(1)    

    def updateCarPrice(self,c1,newPrice):
        con = sqlite3.connect('test.db')
        with con:
            try:
                cur = con.cursor()
                cur.execute(f'update {self.__tableName} set price = {newPrice} where id = {c1.id}')
            except sqlite3.Error:
                print("Error " )
                sys.exit(1)
    
    def get1Car(self,myid):
        con = sqlite3.connect('test.db')
        with con:
            try:
                cur = con.cursor()
                cur.execute(f'Select * from {self.__tableName} where id = {myid}')
                rows = cur.fetchall()
                c1 = Car(rows[0][0], rows[0][1])
                c1.setPrice(int(rows[0][2]))
                return c1
            except sqlite3.Error:
                print("Error " )
                sys.exit(1)        

class CarController:
    def start(self):
        choice = self.Menu()
        while choice !=9:
            if choice ==1:
                da = CarDA()
                da.displayCars()
            elif choice ==2:
                myid = input("Car ID?")
                myName = input("Car Owner Name?")
                myPrice = input("price? (integer)")            
                c1 = Car(myid, myName)
                c1.setPrice(int(myPrice))
                da = CarDA()
                da.insertNewCar(c1)
            elif choice ==3:
                myid = input("Car ID?")
                da = CarDA()
                c1 = da.get1Car(myid)
                print(c1)
                newPrice = int(input("New Price?"))                
                da.updateCarPrice(c1,newPrice)
            choice = self.Menu()

    def Menu(self):
        print("1. Display all cars")
        print("2. Save New Car")
        print("3. Update Car Price")
        print("9. Quit")
        choice = int(input("Enter your choice"))
        return choice   
    

if __name__ =="__main__":
    go = CarController()
    go.start()

    



        
