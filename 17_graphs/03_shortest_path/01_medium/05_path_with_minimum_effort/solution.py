import heapq
from typing import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:    
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # Initialize effort matrix with infinity
        efforts = [[1e9] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Min-heap to store (effort, row, col)
        min_heap = [(0, 0, 0)]  # (effort, row, col)
        
        while min_heap:
            effort, row, col = heapq.heappop(min_heap)
            
            # If we've reached the destination
            if row == rows - 1 and col == cols - 1:
                return effort
            
            # If we've found a better path to this cell already
            if effort > efforts[row][col]:
                continue
            
            # Explore all four adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new cell is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate new effort
                    new_effort = max(effort, abs(heights[row][col] - heights[new_row][new_col]))
                    
                    # If we found a better path to the adjacent cell
                    if new_effort < efforts[new_row][new_col]:
                        efforts[new_row][new_col] = new_effort
                        heapq.heappush(min_heap, (new_effort, new_row, new_col))
        
        return -1  # Should not reach here if the grid is connected
        