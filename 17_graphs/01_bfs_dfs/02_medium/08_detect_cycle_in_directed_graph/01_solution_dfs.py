# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
from typing import *

class Solution:
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        visited = [0] * len(adj)
        path_visited = [0] * len(adj)
        
        def dfs(curr, adj, visited, path_visited):
            visited[curr] = 1
            path_visited[curr] = 1
            
            for next_node in adj[curr]:
                if visited[next_node] == 0:
                    if dfs(next_node, adj, visited, path_visited):
                        return True
                    elif path_visited[next_node] == 1:
                        return True
                        
            # unmark this curr node, because traversal of this path is done
            path_visited[curr] = 0
            return False
                        
        
        # DO dfs for all the components
        for i in range(len(adj)):
            if visited[i] == 0:
                if dfs(i, adj, visited, path_visited):
                    return True
                    
        return False