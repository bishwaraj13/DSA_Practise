# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq
from typing import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums_heap = nums
        heapq.heapify(self.nums_heap)

        while len(self.nums_heap) > k:
            heapq.heappop(self.nums_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums_heap, val)

        if len(self.nums_heap) > self.k:
            heapq.heappop(self.nums_heap)

        return self.nums_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)