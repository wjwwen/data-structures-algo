# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:53:10 2021

@author: 
"""

'''
Exercise 1 : Someone wrote a function nest as follows, you are suppose to prepare 
             a function to measure the performance of this algorithm for test for n=0 to 1000
'''

import timeit
 
# code snippet to be executed only once
# mysetup = "from math import sqrt"
 
# code snippet whose execution time is to be measured
function = '''
def nest(n): 
    for i in range(n): 
        for j in range(n): 
            i+j 

'''
 
# timeit statement
print (timeit.timeit(stmt = function,
                     number = 1000,
                     globals=globals()))

#%%
'''
Exercise 2 :
Write an algorithm to suport the printing of (1+x)^n
Pascals Triangle
                       1
                   1   2   1
                1    3   3   1
              1    4   6   4   1
Pascal’s Triangle is a triangle of numbers where each number is the two numbers directly above it added together (except for the edges, which are all “1”)
expected output for n=6 is
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
'''

def pascal(n):
    if n == 1 :
        print([1,1])
        return [1, 1]  # Default case
    else: 
        pascal_list = [1]
        prev_pascal = pascal(n-1) # # If index is greater than 2, then we recursively call the function to get previous  pascal's triangle row.
        for i in range(len(prev_pascal)):
            num = sum(prev_pascal[i:i+2])
            pascal_list.append(num)
        print(pascal_list)
        return pascal_list
            
        
pascal(6)

#%%
'''
Exercise 3 :
Reverse a string using a recursive function
The original string is modified so that the characters in it are arranged in a reverse manner 
starting from the last character to the first character, thus forming a new string that will be the exact reverse of the original.
The expected output of the given test cases below is :
stresseD
stinK
lageR
slipuP
tramS
slaP
wartS
emiT
ratS

'''
def reverse(string):
    SeqType = type(string)
    emptySeq = SeqType()
    if string == emptySeq: 
        return emptySeq
    
    restrev = reverse(string[1:])
    first = string[0:1]
    a = restrev + first    
    if string[0]=='-':
        return f"-{a[:-1]}"   
    else:
        return a

def main():
    for each in ('Desserts','Knits','Regal','Pupils','Smart','Pals','Straw','Time','Star'):
        print(reverse(each))
    
if __name__ == "__main__":
    main()