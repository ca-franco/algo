# DFS with implict stack

from collections import deque

def traverse_dfs(matrix):
    visited = set()

    def dfs(r,c):
        if (r,c) in visited:
           return 
        
        visited.add((r,c))
        for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0 < nr < len(matrix) and 0 < nc < len(matrix[0]):
                dfs(nr,nc)
        
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            dfs(r,c)

        
        


        

