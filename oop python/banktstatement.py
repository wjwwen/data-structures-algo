# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:56:11 2021

this will be used as assignment 1 part 3 
"""

class BankTransaction:
    def __init__(self, date, description, amount):
        self._date = date
        self._desc = description
        self._amount = amount        
        
class Deposit(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}{self._amount:>15.2f}{'':15s}")
    def broughtForward(self,carriedForwardAmount):
        return carriedForwardAmount + self._amount

class Withdrawal(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}{'':15s}{self._amount:>15.2f}")
    def broughtForward(self,carriedForwardAmount):
        return carriedForwardAmount - self._amount        

class BankStatement:
    def __init__(self,openAmt):
        self.tx =[]
        self._opening = openAmt
    def deposit(self, date, description, amount):
        t1 = Deposit(date,description,amount)
        self.tx.append(t1)        
    def withdrawal(self, date, description, amount):
        t2 = Withdrawal(date,description,amount)
        self.tx.append(t2)
    def __str__(self):
        body = f"""Opening Amount :{self._opening}
{'Date':<15s}{'Description':<25s}{'':15s}{'Amount':>15s}{'Balance':>15s}"""
        balance = self._opening
        for each in self.tx:
            balance = each.broughtForward(balance)
            body += "\n" + str(each) + f"{balance:>15.2f}"
        return body

bs = BankStatement(300)
bs.deposit('2021-12-06','Salary',2500)
bs.withdrawal('2021-12-06','Books',50)
print(bs)
#tx.append(t2)

