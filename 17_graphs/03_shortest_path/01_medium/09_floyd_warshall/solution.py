# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
class Solution:
    def shortest_distance(self, matrix):
        # Get the number of vertices
        V = len(matrix)
        
        # Create a cost matrix from the input matrix
        # Replace -1 with infinity for non-existent edges
        cost = [[float('inf') if matrix[i][j] == -1 else matrix[i][j] for j in range(V)] for i in range(V)]
        
        # Floyd Warshall Algorithm
        for via in range(V):
            for i in range(V):
                for j in range(V):
                    if cost[i][via] != float('inf') and cost[via][j] != float('inf'):
                        cost[i][j] = min(cost[i][j], cost[i][via] + cost[via][j])
        
        # Convert back to original format with -1 for unreachable vertices
        for i in range(V):
            for j in range(V):
                if cost[i][j] == float('inf'):
                    cost[i][j] = -1
                    
        # Update the original matrix in-place
        for i in range(V):
            for j in range(V):
                matrix[i][j] = cost[i][j]
                
        return matrix