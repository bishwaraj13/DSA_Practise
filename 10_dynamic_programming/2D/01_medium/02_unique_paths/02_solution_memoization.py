# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_cache = [[-1 for j in range(n)] for i in range(m)]

        def dfs(i, j):
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0
            
            if dp_cache[i][j] is not -1:
                return dp_cache[i][j]

            up = dfs(i-1, j)
            left = dfs(i, j-1)

            dp_cache[i][j] = up + left
            return dp_cache[i][j]

        return dfs(m-1, n-1)