# https://leetcode.com/problems/sort-characters-by-frequency/
import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        heap = []

        for ch, freq in char_count.items():
            # we dont heappush because 
            # heappush for n elements would take O(nlogn),
            # whereas heapify later would do it at O(n) time
            heap.append((-freq, ch))

        # heapify takes O(n) time
        heapq.heapify(heap)

        result = ''
        while heap:
            freq, ch = heapq.heappop(heap)
            result = result + ch * (-freq)

        return result
        