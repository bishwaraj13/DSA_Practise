# https://leetcode.com/problems/01-matrix/
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        
        # Initialize result matrix with infinity
        result = [[float('inf')] * n for _ in range(m)]
        
        # Initialize visited matrix
        visited = [[False] * n for _ in range(m)]
        
        # Queue for BFS - will store (x, y, distance)
        queue = deque()
        
        # Add all 0s to the queue as starting points
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = True
                    result[i][j] = 0
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # BFS
        while queue:
            x, y, dist = queue.popleft()
            
            # Check all four adjacent cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the new position is valid and not visited
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    result[nx][ny] = dist + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        return result
        