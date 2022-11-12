# %%
# define a variable limitNos and assign 10 to this variable
def limitNos():
    n = 10
    return n

# %%
# define a list call mylist that contains all integers from 0 to limitNos but excluding limitNos 
# to chec
def mylist():
    for i in range(limitNos()):
        print(i)
    
# %%
# print out the first element in mylist
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def getFirst(mylist): 
    return mylist[0]

# print out all numbers in mylist with a for 
for i in range(mylist):
    print(i) 
    
''' expected output :
0
1
2
3
4
5
6
7
8
9
'''

# print pairs of numbers from mylist with itself with nested for 
for i in range(len(mylist)):
    for j in range(i, len(mylist)):
        print (i, j)

''' expected output
0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
1 0
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
2 0
2 1
2 2
2 3
2 4
2 5
2 6
2 7
2 8
2 9
3 0
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
3 9
4 0
4 1
4 2
4 3
4 4
4 5
4 6
4 7
4 8
4 9
5 0
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
5 9
6 0
6 1
6 2
6 3
6 4
6 5
6 6
6 7
6 8
6 9
7 0
7 1
7 2
7 3
7 4
7 5
7 6
7 7
7 8
7 9
8 0
8 1
8 2
8 3
8 4
8 5
8 6
8 7
8 8
8 9
9 0
9 1
9 2
9 3
9 4
9 5
9 6
9 7
9 8
9 9
'''

#%%
'''
Code to work out the solution for
	1 + 2 + 3 + 4 + …… + n
'''

# there are 3 solutions:
def sum1Loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sumMaths(n):
    return (n)*(n+1)/2

def sum2Loops(n):
    total = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            total += 1
        return total
    
if __name__== "__main__":
    print(sum1Loop(100))
    print(sumMaths(100))
    print(sum2Loops(100))
    
#%%
'''
assign 100 to x
assign 200 to y
provide the code to swap x and y content
''' 

# %%
# FIRST METHOD
x = 100
y = 200

x, y = y, x
print("x =", x)
print("y =", y)

# SECOND METHOD
# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# %%
# SOLUTION
def swap1(x,y):
    t = x
    x = y
    y = t
    return x, y

def swap2(x, y):
    x, y = y, x
    return x,y

# ^ = XOR
# When there's two inputs 
def swap3(x, y):
    x = x^y
    y = x^y
    x = x^y
    return x,y

print(swap1(5,6))
print(swap2(5,6))
print(swap3(5,6))

#%%
# Import timeit
# timeit.timeit('random.randint(1, 100)', 'import random', number=10000)

# %%
# Given a variable x = 1
# How to use a same piece of programming statement to toggle 1 to 2 and then 
# with the same statement code toggle 2 to 1 again?

x = 1 
x = 3 - x
x = 3 - x 

# %%
# Case 1
# Do you understand what each function is doing?
# What will each function affected by the parameter limitNos?

def printFirst(thisList):
    print(thisList[0])

def printAll(thisList):
    for each in thisList:
        print(each)
        
def printPairs(thislist):
    for first thisList: 
        print(first, second)

def printTwice(thislist):
    for first in thisList:
        print(first)
    for second in thisList:
        print(second)
    
if __name__ == "__main__": 
    limitNos = 10
    mylist = [x for x in range (limitNos)]
    printFirst(mylist)
    printAll(mylist)
