# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import heapq
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_maps = Counter(nums)
        heap = []
        answer = []

        for num, freq in freq_maps.items():
            heapq.heappush(heap, (freq, num))
            # If heap size exceeds k, remove the element with lowest frequency
            if len(heap) > k:
                heapq.heappop(heap)

        # extract numbers from heap, and we may return result in any order
        result = [pair[1] for pair in heap]

        return result