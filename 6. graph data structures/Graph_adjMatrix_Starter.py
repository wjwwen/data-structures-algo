# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:18:06 2022

@author: Implementation of Graph using adjacency matrix
Difficulty Level : Medium
Last Updated : 07 Dec 2022

"""

# Python3 implementation of the approach
class Graph:
    adj = []
    
    # Function to fill empty adjacency matrix
    def __init__(self, v, directed):
        self.v = v
        self.e = 0
        self.directed = directed
        Graph.adj = [[0 for i in range(v)]
						for j in range(v)]
        
    # Function to fill empty adjacency matrix    
    def addEdge(self, start, e):
        if Graph.adj[start][e] != 1 :
            Graph.adj[start][e] = 1
            self.e +=1
            if not self.directed :
                Graph.adj[e][start] = 1
                self.e +=1

    def __str__(self):
        retStr =""
        for each in Graph.adj:
            retStr += str(each) + "\n"
        return retStr

if __name__ == "__main__":
    nodes = list('ABCDEFG')
    v = len(nodes)
    G = Graph(v, True)
    G.addEdge(nodes.index("A"), nodes.index("B"))
    G.addEdge(nodes.index("A"), nodes.index("C"))
    G.addEdge(nodes.index("B"), nodes.index("D"))
    G.addEdge(nodes.index("C"), nodes.index("D"))
    G.addEdge(nodes.index("D"), nodes.index("E"))
    G.addEdge(nodes.index("D"), nodes.index("F"))
    G.addEdge(nodes.index("F"), nodes.index("G"))
    print(G)

