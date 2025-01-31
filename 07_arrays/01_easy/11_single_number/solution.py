# https://leetcode.com/problems/single-number/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_val = 0

        for elem in nums:
            xor_val ^= elem

        return xor_val