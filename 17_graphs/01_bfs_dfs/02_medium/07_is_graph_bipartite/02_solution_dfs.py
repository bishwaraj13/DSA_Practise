# https://leetcode.com/problems/is-graph-bipartite/
from typing import *

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0/1 = two colors
        
        def dfs(node, node_color):
            color[node] = node_color
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Uncolored
                    # Color neighbor with opposite color
                    if not dfs(neighbor, 1 - node_color):
                        return False
                elif color[neighbor] == node_color:  # Same color conflict
                    return False
            
            return True
        
        # Try to color each uncolored component
        for start in range(n):
            if color[start] == -1:
                if not dfs(start, 0):
                    return False
        
        return True  # All components are bipartite
        