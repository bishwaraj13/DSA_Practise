# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
from typing import *

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        s = set()
        dist_arr = [1e9] * len(adj)
        
        dist_arr[src] = 0
        s.add((0, src))
        
        while s:
            distance, node = next(iter(s))
            s.remove((distance, node))
            
            for adj_node, edge_wt in adj[node]:
                if distance + edge_wt < dist_arr[adj_node]:
                    dist_arr[adj_node] = distance + edge_wt
                    s.add((dist_arr[adj_node], adj_node))
                    
        return dist_arr