# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:06:38 2022

@author: 
"""


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
    
graph={ 'Amin'   : {'Wasim', 'Nick', 'Mike'},        
        'Wasim' : {'Imran', 'Amin'}, 
        'Imran' : {'Wasim','Faras'},
        'Faras' : {'Imran'},
         'Mike'  : {'Amin'}, 
         'Nick' :  {'Amin'}}

print(dfs(graph,'Amin'))
