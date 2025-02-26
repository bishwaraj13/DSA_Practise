# https://leetcode.com/problems/triangle/
from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}

        # base case
        for j in range(n):
            memo[(n-1, j)] = triangle[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                down = triangle[i][j] + memo[(i+1, j)]
                diagonal = triangle[i][j] + memo[(i+1, j+1)]
                memo[(i, j)] = min(down, diagonal)

        return memo[(0, 0)]
        
