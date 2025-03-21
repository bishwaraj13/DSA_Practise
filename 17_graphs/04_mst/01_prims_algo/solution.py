# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
from typing import List
import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        visited = [False] * len(adj)
        heap = []
        sum_wt = 0
        mst_list = []
        
        # we insert (wt, node, parent) in heap
        # first node will have -1 weight, and no parent
        heapq.heappush(heap, (-1, 0, 0))
        
        # E log E
        while heap:
            # log E
            wt, node, parent = heapq.heappop(heap)
            
            # if already visited, we dont care
            if visited[node]:
                continue
            
            visited[node] = True
            
            if wt != -1:
                sum_wt += wt
                mst_list.append((parent, node))
            
            # E log E
            for neighbour, wt1 in adj[node]:
                # insert all neighbours if they are unvisited
                if not visited[neighbour]:
                    heapq.heappush(heap, (wt1, neighbour, node))
                    
        return sum_wt
    
        # Total TC: E log E + E log E = E log E