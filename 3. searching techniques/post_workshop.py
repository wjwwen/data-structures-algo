#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Wang Jing Wen

Post-workshop activity:
    
Prepare a .py program to
• Perform analysis on the time complexities for linear and binary search.
Also provide your learning reflections, questions and feedback on today lesson.
You may submit more than once for this activity

"""

from functools import wraps
from time import time
import timeit
from random import randint

mylist = [x for x in range(100000)]
find = randint(0, len(mylist)) # returns int from range 0 to 100000

def measure(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f'{func.__name__} took {total_time:.8f} seconds and the searched number is')
        return result
    return timeit_wrapper

# %%
@measure
def LinearSearch(inlist, item):      
    for i in range(len(inlist)):
        if inlist[i] == item:             
            return i      
    return -1

LinearSearch(mylist, find)

# %%
@measure
def BinarySearch(mylist, item): 
   low = 0 
   high = len(mylist)-1 
   index = -1
   while low<=high :         
        mid = (high + low)//2    
        if mylist[mid] < item:                 
                low = mid+1             
        elif mylist[mid] > item:                    
                high = mid-1        
        else:
            index = mid
            break
   return index

BinarySearch(mylist, find)