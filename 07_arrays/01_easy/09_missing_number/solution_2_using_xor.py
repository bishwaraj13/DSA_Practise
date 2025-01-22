# https://leetcode.com/problems/missing-number/
# notes: xor of same number is 0, xor of 0 and a number is the number itself
# e.g, 0 ^ 0 = 0, 0 ^ 1 = 1, 1 ^ 1 = 0
# e.g 2: (0 ^ 1 ^ 2 ^ 3) ^ (0 ^ 1 ^ 2 ^ 3) = 0
# e.g 3: (0 ^ 1 ^ 2 ^ 3) ^ (0 ^ 1 ^ 2) = 3

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0

        for i in range(n+1):
            xor ^= i

        for val in nums:
            xor ^= val

        return xor

        return sum
    