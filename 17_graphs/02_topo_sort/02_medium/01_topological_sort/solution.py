# https://www.geeksforgeeks.org/problems/topological-sort/1
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        V = len(adj)
        visited = [0] * V
        stack = []
        
        def dfs(curr, visited, stack, adj):
            visited[curr] = 1
            
            for next in adj[curr]:
                if visited[next] == 0:
                    dfs(next, visited, stack, adj)
                    
            stack.append(curr)
        
        for i in range(V):
            if visited[i] == 0:
                dfs(i, visited, stack, adj)
                
        answer = []
        
        while stack:
            answer.append(stack.pop())
            
        return answer