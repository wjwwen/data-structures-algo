# -*- coding: utf-8 -*-
'''
Simulate 1000 random numbers from 50 to 90 
with equal probabilities. Assign to a list,
from the list, work out the number of 50 to 90 occurrences
print out the list in rows of 10 numbers
'''

# random. randint/randrange function will always generate numbers 
# with equal probability for each number within the range

import random

numlist = [] 
def randomNos():
    for i in range(1000):  
        x = random.randrange(50,90)
        numlist.append(x)

randomNos()

for i in range (4):
    selected_x = random.sample(numlist, min(10, len(numlist)))
    print(selected_x)    

# %%
# ----------------- SOLUTION -----------------
import random
x=[]
d={}
top =50
bottom=90
nos=10
for i in range(top,bottom+1):
    d[i]=0
for i in range(nos):
    n=random.randint(top,bottom)
    x.append(n)
    d[n]+=1
for k,v in d.items():
    print(k,v)
z=0
for z in range(0,len(x),10):
    print(x[z:z+10])


#%%
'''
Simulate 1000 random numbers from 50 to 90 
With 60 to 80 twice likely from 0 to 100
Assign to a list,
from the list, work out the number of 50 to 90 occurrences
print out the list in rows of 10 numbers
'''

# weighted random choices from list with probabilities
import random, numpy as np
def selected(population, weights, k):
    selected = []
    while len(selected) < 10:
        selected += random.choices(population=population, weights=weights, k=10 - len(selected))
        selected = list(set(selected))
    return selected

np.random.seed(0)

# need to calbrate population and weigghts :(
population = np.random.randint(100, size=1000)
weights = np.random.rand(len(population))
k = 10
    
for i in range(4):
    print(selected(population, weights, k))
    
# %%
# ----------------- SOLUTION -----------------
import random
x=[]
d={}
r1 = 90-50
r2 = 80 -60
top =0
bottom=r1+r2
nos=1000
for i in range(50,90+1):
    d[i]=0
for i in range(nos):
    n=random.randint(top,bottom)
    if n >r1:
        n=n-r1+60
    else:
        n= n+50
    x.append(n)
    d[n]+=1
for k,v in d.items():
    print(k,v)
z=0
for z in range(0,len(x),10):
    print(x[z:z+10])
    
    
#%%
"""
Created on Mon Nov 14 23:20:55 2022 
https://atozcoding.com/python-program-to-shuffle-deck-of-cards/

Deck of Cards

A deck in Python is defined as a tuple or a list within a list. It contains two elements. 

The first element will represent the number of cards that are present in a suit, 
that is, from 1 to 13 and the other element represents the four suits. 

These 52 elements in total represent the deck of cards
For program, packages such as itertools and random are used. 

The random library has a method in-built in it called shuffle that is used to mix and randomize 
the order of the data and then print it

Write a program to simulate the shuffling of a deck of 52 cards and draw 5 cards

"""
import itertools, random

# create a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle
random.shuffle(deck)

# draw five cards
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
