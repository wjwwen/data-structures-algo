# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 07:59:47 2022

Background: Someone wrote the following warshall algorithm, 
1. Amend the adjacency matrix to fit the graph discussed in the lecture case study 
2. execute and check if it solves correctly as the manual work through during lecture
3. if it is not, try to find out where went wrong !
    
"""


def warshall(a):

    assert (len(row) == len(a) for row in a)
    n = len(a)
    for k in range (n):
        for i in range (n):
            for j in range (n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a

#check1 = [[0,0,0],[1,0,1],[1,0,0],[0,0,1]]
check1 = [[0,0,0,1],[1,0,1,0],[1,0,0,1],[0,0,1,0]]

print("given: ")
for each in check1:
    print(each)
print("reachability :")
for each in  warshall(check1):
    print(each)
#[[0, 0, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1], [0, 0, 1, 1]]  wrong


#%% 


