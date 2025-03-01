# https://leetcode.com/problems/split-array-largest-sum/
# This problem is ditto copy of allocate books
from typing import *

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isSplittingPossible(subarraySum, totalSubarrays):
            cntSubarray = 1
            prevSum = 0

            for num in nums:
                if prevSum + num <= subarraySum:
                    prevSum += num
                else:
                    # we have reached the permissible subarraySum
                    # we move to next subarray
                    cntSubarray += 1

                    if cntSubarray > totalSubarrays:
                        return False
                    prevSum = num

            return True

        # each subarray should have min capacity to withold the largest element
        low = max(nums)

        # the max is that one subarray can hold the entirely all the elements
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            if isSplittingPossible(mid, k):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
