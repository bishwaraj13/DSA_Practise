# https://www.geeksforgeeks.org/problems/geek-jump/1
class Solution:
    def minCost(self, height):
        dp_cache = [float("inf")] * len(height)
        dp_cache[0] = 0

        for i in range(1, len(height)):
            left = dp_cache[i-1] + abs(height[i]-height[i-1])

            right = float("inf")
            if i > 1:
                right = dp_cache[i-2] + abs(height[i]-height[i-2])

            dp_cache[i] = min(left, right)

        return dp_cache[len(height)-1]
