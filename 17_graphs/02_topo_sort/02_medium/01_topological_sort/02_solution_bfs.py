# # https://www.geeksforgeeks.org/problems/topological-sort/1
from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
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
                    
        return answer
    