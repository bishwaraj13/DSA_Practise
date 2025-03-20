# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import heapq
from collections import defaultdict
from typing import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Priority queue for Dijkstra's algorithm - (cost, node, stops)
        pq = [(0, src, 0)]  # (cost, current city, stops used)
        
        # Dictionary to track the minimum cost to reach each node with a specific number of stops
        # We track stops because a cheaper path with more stops might not be valid
        visited = {}  # (node, stops) -> cost
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            # If we've reached the destination, return the cost
            if node == dst:
                return cost
            
            # If we've already used up our k stops, we can't explore further from this node
            if stops > k:
                continue
            
            # If we've seen this node with fewer stops and less cost, skip it
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            
            visited[(node, stops)] = cost
            
            # Explore neighbors
            for neighbor, price in graph[node]:
                heapq.heappush(pq, (cost + price, neighbor, stops + 1))
        
        return -1  # If no valid path exists