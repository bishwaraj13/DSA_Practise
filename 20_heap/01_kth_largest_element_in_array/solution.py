# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
from typing import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # O(n)

        while len(nums) > k:
            heapq.heappop(nums)

        return heapq.heappop(nums)
