# 
from typing import *
from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # Since the graph is bidirectional
        
        # Function to perform Dijkstra's algorithm from a source vertex
        def dijkstra(src):
            # Initialize distances to all vertices as infinity
            dist = [float('inf')] * n
            dist[src] = 0
            
            # Priority queue to store vertices to be processed
            pq = [(0, src)]  # (distance, vertex)
            
            while pq:
                d, u = heapq.heappop(pq)
                
                # If popped distance is greater than current known distance, skip
                if d > dist[u]:
                    continue
                    
                # Process all neighbors of u
                for v, w in graph[u]:
                    # If there is a shorter path to v through u
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            
            # Count cities reachable within the threshold distance
            count = sum(1 for d in dist if d <= distanceThreshold and d > 0)
            return count
        
        min_reachable = float('inf')
        result_city = -1
        
        # Apply Dijkstra's algorithm for each city
        for city in range(n):
            reachable_cities = dijkstra(city)
            
            # Update result if current city has fewer reachable cities
            # or same number but higher city number
            if reachable_cities < min_reachable or (reachable_cities == min_reachable and city > result_city):
                min_reachable = reachable_cities
                result_city = city
        
        return result_city