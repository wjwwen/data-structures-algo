# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:11:30 2021

@author: 
"""
#%%
'''P1
'''
class Shoppingcart:
    """ Contains item in the shopping cart """
    pass

x = Shoppingcart()
print(x)
#%%


'''P2
'''
class Shoppingcart():
    def __init__ (self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty
        

item1 = Shoppingcart('P001', 21.45, 2)
print(item1)
print(item1.pid, item1.uprice, item1.qty)

#%%

'''P3
'''
class Shoppingcart():
    def __init__(self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty
    def __str__(self):
        return f'{self.pid} => {self.uprice} x {self.qty}'

item1 = Shoppingcart('P001', 21.45, 2)
print(item1)

#%%
'''P4
'''
class Shoppingcart():
    def __init__(self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty
    def __str__(self):
        return f'{self.pid} => {self.uprice} x {self.qty}'
    def updatePrice (self,  price):
    	self.uprice = price
            
item1 = Shoppingcart('P001', 21.45, 2)
item1.updatePrice(44.23)
print(item1)
#%%

''' P5
'''
class Shoppingcart():
    def __init__(self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty
    def __str__(self):
        return f'{self.pid} => {self.uprice} x {self.qty}'

class WalkIn(Shoppingcart):
    pass

class PhoneIn(Shoppingcart):
    pass

#%%

class Shoppingcart():
    def __init__(self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty
    def __str__(self):
        return f'{self.pid} => {self.uprice} x {self.qty}'

class WalkIn(Shoppingcart):
    def clockIn(self,timeIn):
        self.clockIn = timeIn
    def __str__(self):
        return f'Welcome to my shop, {self.pid} => {self.uprice} x {self.qty}'

class PhoneIn(Shoppingcart):
    def __str__(self):
        return f'Thanks for calling, {self.pid} => {self.uprice} x {self.qty}'
    def informCaller(self):
        return "You call may be recorded for training purposes"

item1 = Shoppingcart('P001', 21.45, 2)
print(item1)
item2 = WalkIn('P333', 25.78, 20)
print(item2)
item3 = PhoneIn('P909', 7.66, 40)
print(item3)

#%%
class Shoppingcart():
    def __init__(self, productID, price, qty):
        self.pid = productID
        self.uprice = price
        self.qty = qty


    def __str__(self):
        return f'{self.pid} => {self.uprice} x {self.qty}'

class WalkIn(Shoppingcart):
    def __str__(self):
        return f'Welcome to my shop, {self.pid} => {self.uprice} x {self.qty}'


class PhoneIn(Shoppingcart):
    def __init__(self, productID, price, qty):
         super().__init__(productID, price, qty)
         self.__linetotal = price * qty
         self._canStillSee = "I am still not protected"
        
    def __str__(self):
        return f'Thanks for calling, {self.pid} => {self.uprice} x {self.qty} = {self.__linetotal}'
    
    def informCaller(self):
        return "You call may be recorded for training purposes"
item1 = Shoppingcart('P001', 21.45, 2)
print(item1)
item2 = WalkIn('P333', 25.78, 20)
print(item2)
item3 = PhoneIn('P909', 7.66, 40)
print(item3)
print(item3.pid)
print(item3.uprice)
print(item3._canStillSee)
#print(item3._PhoneIn__linetotal)
#print(item3.__linetotal)


#%%
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
        
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()

#%%
class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
        
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
        
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


#%%
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
        
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()
    
obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)

#%% https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


def in_the_pacific(fish):
    fish.swim()

sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
    
in_the_pacific(sammy)
in_the_pacific(casey)
    

#%% https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3
class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


def in_the_pacific(fish):
    fish.swim()

dict1={}

sammy = Shark()
sammy.skeleton()

dict1["sammy"]= sammy

casey = Clownfish()
casey.skeleton()

dict1["casey"]= casey

for fish in dict1.values():
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
    
in_the_pacific(sammy)
in_the_pacific(casey)

in_the_pacific(dict1["sammy"])
    
