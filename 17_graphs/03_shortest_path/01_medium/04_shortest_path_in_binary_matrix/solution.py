# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque
from typing import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def get_all_8_directions():
            directions = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    directions.append([i, j])

            return directions

        ROWS, COLS = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        # edge case:
        if ROWS == 1 and COLS == 1 and grid[0][0] == 0:
            return 1
        
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        path_length = 0
        queue = deque()
        directions = get_all_8_directions()
        firstElem = [0, 0]
        queue.append(firstElem)
        visited[0][0] = 1

        while queue:
            queue_len = len(queue)
            path_length += 1

            for i in range(queue_len):
                r, c = queue.popleft()

                for dr, dc in directions:
                    next_row, next_col = r + dr, c + dc

                    if min(next_row, next_col) < 0 or \
                    max(next_row, next_col) > ROWS-1 or \
                    grid[next_row][next_col] == 1 or \
                    visited[next_row][next_col] == 1:
                        continue

                    if next_row == ROWS-1 and next_col == COLS-1:
                        return path_length + 1

                    visited[next_row][next_col] = 1
                    queue.append([next_row, next_col])

        return -1
                