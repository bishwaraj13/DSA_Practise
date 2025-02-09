# https://www.geeksforgeeks.org/problems/geek-jump/1
class Solution:
    def minCost(self, height):
        prev = 0
        prev_prev = float("inf")
        curr = 0

        for i in range(1, len(height)):
            left = prev + abs(height[i]-height[i-1])

            right = float("inf")
            if i > 1:
                right = prev_prev + abs(height[i]-height[i-2])

            curr = min(left, right)
            prev_prev = prev
            prev = curr

        return curr
