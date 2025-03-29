# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        max_heap = []
        # Add first k elements to the heap
        for i in range(k):
            # Store as negative to simulate max-heap behavior
            heapq.heappush(max_heap, -arr[i])
        
        # For remaining elements, if smaller than current kth element,
        # replace the largest element in our heap
        for i in range(k, len(arr)):
            if -max_heap[0] > arr[i]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -arr[i])
        
        # The root of our max-heap is the kth smallest element
        return -max_heap[0]
    