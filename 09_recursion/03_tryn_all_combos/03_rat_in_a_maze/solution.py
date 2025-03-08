# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        n = len(mat)
        if n == 0 or mat[0][0] == 0:
            return []
        
        # To track visited cells
        visited = [[0 for _ in range(n)] for _ in range(n)]
        
        # Result list to store all valid paths
        result = []
        
        # Directions: Down, Left, Right, Up
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        direction = ['D', 'L', 'R', 'U']
        
        # Recursive backtracking function
        def solve(i, j, path):
            # Base case: reached destination
            if i == n-1 and j == n-1:
                result.append(path)
                return
            
            # Mark current cell as visited
            visited[i][j] = 1
            
            # Try all four directions
            for k in range(4):
                next_i, next_j = i + di[k], j + dj[k]
                
                # Check if next position is valid and not visited
                if (0 <= next_i < n and 0 <= next_j < n and 
                    mat[next_i][next_j] == 1 and visited[next_i][next_j] == 0):
                    # Recursive call for next position
                    solve(next_i, next_j, path + direction[k])
            
            # Backtrack: mark current cell as unvisited
            visited[i][j] = 0
        
        # Start backtracking from source (0,0)
        solve(0, 0, "")
        
        # Sort results lexicographically as required
        result.sort()
        return result