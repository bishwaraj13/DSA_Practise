# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
# Solving it using Kahn's algorithm to get Topological Sort
# Topological sort only works for DAG
# and if it contains cycle, then answer array will have lesser elements
from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        V = len(adj)
        indegree = [0] * V
        answer = []
        
        # create indegree list
        for i in range(V):
            # node-th i goes to these nodes
            dest_nodes = adj[i]
            
            for node in dest_nodes:
                indegree[node] += 1
                
        queue = deque()
        
        # add nodes who has 0 indegree to queue
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            
            # decrement indegree for add the adjacent nodes of curr
            for node in adj[curr]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
                    
        if len(answer) < V:
            # it has a cycle
            return 1
            
        return 0