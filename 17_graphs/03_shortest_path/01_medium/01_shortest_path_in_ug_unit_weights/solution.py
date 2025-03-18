# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
from collections import deque

class Solution:
    def shortestPath(self, adj, src):
        dist_arr = [-1] * len(adj)
        dist_arr[src] = 0
        
        def bfs():
            queue = deque()
            queue.append((src, 0))
            
            while queue:
                queue_size = len(queue)
                
                for i in range(queue_size):
                    node, dist = queue.popleft()
                    
                    for neighbour in adj[node]:
                        # Only update and enqueue if we found a shorter path
                        if dist_arr[neighbour] == -1:
                            dist_arr[neighbour] = dist + 1
                            queue.append((neighbour, dist + 1))
                        
        bfs()
        return dist_arr