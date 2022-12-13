# -*- coding: utf-8 -*-
"""
https://favtutor.com/blogs/prims-algorithm-python

# Prim's Algorithm in Python
#https://favtutor.com/blogs/prims-algorithm-python

"""

INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 4, 0, 3, 5],
     [4, 0, 2, 0, 0],
     [0, 2, 0, 1, 0],
     [3, 0, 1, 0, 0],
     [5, 0, 0, 0, 0]]

selected_node = [0, 0, 0, 0, 0]
nodeLabel =["A","B", "C", "D", "E"]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(nodeLabel[a]) + "-" + str(nodeLabel[b]) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
    
    