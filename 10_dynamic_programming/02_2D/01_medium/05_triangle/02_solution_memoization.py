# https://leetcode.com/problems/triangle/
from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            nonlocal n
            if i == n - 1:
                return triangle[i][j]

            down = triangle[i][j] + dfs(i+1, j)
            diagonal = triangle[i][j] + dfs(i+1, j+1)

            memo[(i, j)] = min(down, diagonal)

            return memo[(i, j)]

        return dfs(0, 0)
        