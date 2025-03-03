# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import *
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V
        
        def dfs(parent, child):
            visited[child] = 1
            
            for grand_child in adj[child]:
                # Skip the parent node
                if grand_child == parent:
                    continue
                
                # If grand_child is already visited, cycle detected
                if visited[grand_child] == 1:
                    return True
                
                # Recursively check for cycles
                if dfs(child, grand_child):
                    return True
            
            return False
        
        # Check each component of the graph
        for i in range(V):
            if visited[i] == 0:  # If not visited
                if dfs(-1, i):
                    return True
        
        return False