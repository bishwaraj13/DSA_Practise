# https://leetcode.com/problems/max-consecutive-ones/description/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_1 = 0

        left = 0

        while left < n:

            while left < n and nums[left] == 0:
                left += 1

            right = left

            while right < n and nums[right] == 1:
                right += 1

            max_1 = max(right-left, max_1)
            left = right + 1
        
        return max_1