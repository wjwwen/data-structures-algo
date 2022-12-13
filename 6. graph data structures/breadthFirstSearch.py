# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:04:33 2022

@author: 
"""


def bfs(graph,start):
    visited =[]  #Contains all the nodes that have been visited
    queue =[start] #Contains nodes yet to be visited
    while queue:
        node =queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
    
graph={ 'Amin'   : {'Wasim', 'Nick', 'Mike'},        
        'Wasim' : {'Imran', 'Amin'}, 
        'Imran' : {'Wasim','Faras'},
        'Faras' : {'Imran'},
         'Mike'  : {'Amin'}, 
         'Nick' :  {'Amin'}}

print(bfs(graph,'Amin'))
