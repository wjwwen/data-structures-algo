# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:18:06 2022

@author: Implementation of DFS using adjacency matrix
Difficulty Level : Medium
Last Updated : 24 Nov, 2021

https://www.geeksforgeeks.org/implementation-of-dfs-using-adjacency-matrix/
"""


# Python3 implementation of the approach
class Graph:
    adj = []
	# Function to fill empty adjacency matrix
    def __init__(self, v, e):
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)]
						for j in range(v)]

	# Function to add an edge to the graph
    def addEdge(self, start, e):
		
		# Considering a bidirectional edge
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1
        
    def DFS(self, start, visited):
        # print current node
        print(start, end = '')
        
        # set current node as visited
        visited[start] = True
        
        # if some node is adjacent to the currnet node and it has not already been visited
        for i in range(self.v):
            if (Graph.adj[start][i] == i and
                    (not visited[i])):
                self.DFS(i,visited)
    
# Driver code
v, e = 5, 4

# Create the graph
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(0, 3)
G.addEdge(0, 4)

print(G.adj)
