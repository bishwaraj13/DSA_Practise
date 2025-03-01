# https://leetcode.com/problems/kth-missing-positive-number/
# At each position, calculate how many numbers are missing (arr[mid] - (mid+1)), 
# then binary search for the first position where the missing count ≥ k, 
# and return (low + k) which gives the kth missing number.
from typing import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)

        low = 0
        high = n-1

        while low <= high:
            mid = (low+high) // 2
            missing = arr[mid] - (mid+1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k