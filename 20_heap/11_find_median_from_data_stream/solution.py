# https://leetcode.com/problems/find-median-from-data-stream
import heapq

class MedianFinder:

    def __init__(self):
        # Max heap for the lower half (Python heapq is min-heap by default, so we negate values)
        self.max_heap = []  
        # Min heap for the upper half
        self.min_heap = []  

    def addNum(self, num: int) -> None:
        # By default, add to max_heap (lower half)
        heapq.heappush(self.max_heap, -num)
        
        # Make sure every element in max_heap is <= every element in min_heap
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            # Move the largest element from max_heap to min_heap
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        
        # Balance the heaps (their sizes differ by at most 1)
        if len(self.max_heap) > len(self.min_heap) + 1:
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) > len(self.max_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            # If max_heap has more elements, the median is its top element
            return -self.max_heap[0]
        else:
            # If sizes are equal, the median is the average of the two middle elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2