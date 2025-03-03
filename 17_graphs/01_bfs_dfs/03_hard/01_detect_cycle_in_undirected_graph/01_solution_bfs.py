# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import *
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [0] * V
        
        # Check each component of the graph
        for i in range(V):
            if visited[i] == 0:  # If not visited
                queue = deque()
                
                # queue will store (parent, child)
                queue.append((-1, i))
                visited[i] = 1
                
                while queue:
                    parent, child = queue.popleft()
                    
                    for grand_child in adj[child]:
                        if grand_child == parent:
                            continue
                        
                        if visited[grand_child] == 1:
                            # it means some one else visited it from some other route
                            return True
                            
                        visited[grand_child] = 1
                        queue.append((child, grand_child))
        
        return False