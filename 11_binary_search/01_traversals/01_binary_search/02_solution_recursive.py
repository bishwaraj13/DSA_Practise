# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_recursive(low, high):
            if low > high:
                return -1
            
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return search_recursive(mid+1, high)
            else:
                return search_recursive(low, mid-1)
        
        return search_recursive(0, len(nums)-1)