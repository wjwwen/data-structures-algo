# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:56:11 2021

This will be used as the base for assignmnet 1 part 3
"""

class BankTransaction:
    def __init__(self,bankcode, date, description, amount):
        self._bankCode = bankcode
        self._date = date
        self._desc = description
        self._amount = amount        
        
class Deposit(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}{self._amount:>15.2f}")

class Withdrawal(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}{'':15s}{self._amount:>15.2f}")
        

tx =[]
t1 = Deposit("POSB",'20211206','Salary',2500)
tx.append(t1)
t2 = Withdrawal("POSB",'20211206','Books',50)
tx.append(t2)
for each in tx:
    print (each)
