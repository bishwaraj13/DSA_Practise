# https://leetcode.com/problems/is-graph-bipartite/
from typing import *

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0/1 = two colors
        
        for start in range(n):
            if color[start] == -1:
                queue = [(start, 0)]  # (node, color)
                color[start] = 0
                
                while queue:
                    node, node_color = queue.pop(0)
                    
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:  # Uncolored
                            color[neighbor] = 1 - node_color  # Opposite color
                            queue.append((neighbor, color[neighbor]))
                        elif color[neighbor] == node_color:  # Same color conflict
                            return False
        
        return True  # All components are bipartite
        