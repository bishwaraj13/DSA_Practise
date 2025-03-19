# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
from typing import List
import sys

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        # create adjList
        adjList = [[] for _ in range(V)]
        
        for edge in edges:
            src = edge[0]
            dest = edge[1]
            wt = edge[2]
            
            adjList[src].append((dest, wt))
            
        dist_arr = [sys.maxsize] * V
        visited = [False] * V
        stack = []
        
        def dfs(node):
            visited[node] = True
            
            for neighbour_details in adjList[node]:
                neighbour, dist = neighbour_details
            
                if visited[neighbour]:
                    continue
                    
                dfs(neighbour)
                 
            stack.append(node)
            
        # step1: do topological sort using dfs
        for node in range(V):
            if not visited[node]:
                dfs(node)
           
        # dist from source to source is 0     
        dist_arr[0] = 0
        
        # step2: pop elements from stack and update dist array
        while stack:
            node = stack.pop()
            
            for neighbour_details in adjList[node]:
                neighbour, dist = neighbour_details
                
                if dist + dist_arr[node] < dist_arr[neighbour]:
                    dist_arr[neighbour] = dist + dist_arr[node]
                    
        # After calculating all shortest paths
        for i in range(V):
            if dist_arr[i] == sys.maxsize:
                dist_arr[i] = -1
                
        return dist_arr