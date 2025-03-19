# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
from typing import *
import heapq

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        heap = []
        dist_arr = [1e9] * len(adj)
        
        dist_arr[src] = 0
        heapq.heappush(heap, (0, src)) # O(log n)
        
        while heap: # V times
            distance, node = heapq.heappop(heap) # O(log V)
            
            for adj_node, edge_wt in adj[node]: # for (V-1) times
                if distance + edge_wt < dist_arr[adj_node]:
                    dist_arr[adj_node] = distance + edge_wt
                    heapq.heappush(heap, (dist_arr[adj_node], adj_node)) # O (log V)
                    
        return dist_arr
    # Total TC: V * (log V + (V-1) * log V)
    # ~ V^2 log V
    # ~ E log V
    # So, total TC =  E log V