# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            up = dfs(i-1, j)
            left = dfs(i, j-1)

            return up + left

        return dfs(m-1, n-1)