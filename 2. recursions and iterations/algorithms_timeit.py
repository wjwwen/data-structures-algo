#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Learning Objectives: Algorithm
Includes: Loops and Slicing
"""

# %%
"""
Exercise 1   assign "ti nrael ot ecnahc a evah i dalg ma i dna og ot yaw eht si nohtyp" to a variable statement 1
             then display the statement1 in the reverse spelling order
"""

statement1 = "ti nrael ot ecnahc a evah i dalg ma i dna og ot yaw eht si nohtyp" 
print(statement1[-1::-1])

# %%
"""
Exercise 2   You received a secret message 'meandyeveopouutwe henhuirandrvoiteoiy cbgspouemngllydeomycmcytmvyenordmnh lkiapoi mkurponimnggmbshvjutpos kutcmnhopobulknrmnasabsepct'
             You are given the clue that this message begins with the word 'you'
             Assign this secret message to a variable statement3 and try to decode this message if the decoding follow a fix pattern

"""
statement3 = 'meandyeveopouutwe henhuirandrvoiteoiy cbgspouemngllydeomycmcytmvyenordmnh lkiapoi mkurponimnggmbshvjutpos kutcmnhopobulknrmnasabsepct'
print(statement3[5::4])

# %%
"""
Exercise 3   Get into your project group
             Devise an algorithms to solve the questions
			 similiar to Exercise 2
"""
statement3 = 'meandyeveopouutwe henhuirandrvoiteoiy cbgspouemngllydeomycmcytmvyenordmnh lkiapoi mkurponimnggmbshvjutpos kutcmnhopobulknrmnasabsepct'

hint = []

for i in range(len(statement3)):
    if statement3[i:i+1]=='y':
        hint.append(i)
print(hint)

hint2 = []
for each in hint:
    for i in range(each, len(statement3)):
        if statement3[i:i+1] == 'o':
            hint2.append((each, i))
print(hint2)

hint3 = []
for each in hint3:
    if each[2]-each[1]==each[1]-each[0]:
        print("the gap is", each[1]-each[0])
        print(statement3[each[0]::each[1]-each[0]])
        
        
# %%       
"""
Exercise 4  Get into your project group
             Devise an algorithms to
             Plot the performance of cases study 2
             Write a program to work out the solution for
	         1 + 2 + 3 + 4 + …… + n

             Can you code with more than 1 algorithm? 
"""

import matplotlib.pyplot as plt
import math
import timeit

def sum1Loop(n):
    total = 0
    for i in range(1, n+1):
        total += 1
    return total

def sumMaths(n):
    return (n)*(n+1)/2

def sum2Loops(n):
    total = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            total += 1
        return total
    
x = [1, 2, 3, 4, 5]
times = 100
prework = ''
s1 = []
s2 = []
s3 = []
for each in x:
   s1.append(timeit.timeit(f'sum1Loop({each})', globals=globals()))
   s2.append(timeit.timeit(f'sumMaths({each})', globals=globals()))
   s3.append(timeit.timeit(f'sum2Loops({each})', globals=globals()))

plt.plot(x, s1, label="1 Loop") 
plt.plot(x, s2, label ='maths') 
plt.plot(x, s3, label='2 loops') 
plt.legend()
plt.show() 

# %%
"""
Exercise 5  Compare the time conplexity of algorithm to compute factorial 
             using loop and using recusive function
             Plot the performance of cases study 
"""
import matplotlib.pyplot as plt 
import timeit


def factorial(n):
#test for a base case
    if n==0:
        return 1
    else:
        # make a calculation and a recursive call
        f= n*factorial(n-1)
        return(f)
    
def factloop(n):
    total = 1
    for i in range(1,n+1):
        total *=i
    return total

def factorialtailend(n,cum=1):
#test for a base case
    if n==0:
        return cum
    else:
        # make a calculation and a recursive call
        return factorialtailend(n-1,cum*n)


x= [1,5,10,15,20] #,100,1000,10000, 100000]

prework = ''
s1=[]
s2=[]
s3=[]
for each in x:
   #print(timeit.timeit(f'[func({each}) for func in (sum1Loop,sumMaths,sum2Loops)]', globals=globals()))
   print(each)
   s1.append(timeit.timeit(f'factorial({each})', globals=globals()))
   s2.append(timeit.timeit(f'factloop({each})', globals=globals()))
   s3.append(timeit.timeit(f'factorialtailend({each})', globals=globals()))
plt.plot(x, s1, label="recursive") 
plt.plot(x, s2, label ='loop') 
plt.plot(x, s3, label ='tail end recursive') 
plt.legend()
plt.show()


