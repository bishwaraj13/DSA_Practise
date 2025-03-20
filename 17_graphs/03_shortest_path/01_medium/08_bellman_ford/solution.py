# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        num_cycles = V-1
        dist_arr = [int(1e8)] * V
        dist_arr[src] = 0
        
        while num_cycles:
            for u, v, wt in edges:
                if dist_arr[u] != int(1e8) and dist_arr[u] + wt < dist_arr[v]:
                    dist_arr[v] = dist_arr[u] + wt
                    
            num_cycles -= 1
            
        # Vth iteration to check if it has negative cycle
        for u, v, wt in edges:
            if dist_arr[u] != int(1e8) and dist_arr[u] + wt < dist_arr[v]:
                return [-1]
                
        return dist_arr