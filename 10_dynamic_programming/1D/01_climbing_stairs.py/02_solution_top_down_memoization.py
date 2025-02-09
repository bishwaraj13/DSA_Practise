# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # step 1 is index 0, step 2 is index 1, step 3 is index 2, ..
        dp_cache = [-1] * n

        def dfs(index):
            # index 1 is step 2, index 0 is step 1
            if index <= 1:
                return index+1

            left = 0
            if index-1 >=0 and dp_cache[index-1] != -1:
                left = dp_cache[index-1]
            else:
                left = dfs(index-1)
                dp_cache[index-1] = left

            right = 0
            if index-2 >=0 and dp_cache[index-2] != -1:
                right = dp_cache[index-2]
            else:
                right = dfs(index-2)
                dp_cache[index-2] = right

            return left+right

        return dfs(n-1)