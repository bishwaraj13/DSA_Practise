# https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
import heapq

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # Initialize an empty result list
        result = []
        
        # Create a min heap to store elements
        min_heap = []
        
        # Initially add the first element from each array to the min heap
        # along with its array index and element index
        for i in range(K):
            if arr[i]:  # Check if array is not empty
                heapq.heappush(min_heap, (arr[i][0], i, 0))
        
        # Process elements from the min heap
        while min_heap:
            # Get the minimum element, its array index, and element index
            val, array_idx, element_idx = heapq.heappop(min_heap)
            
            # Add the minimum element to the result
            result.append(val)
            
            # If there are more elements in the same array, add the next element to the heap
            if element_idx + 1 < len(arr[array_idx]):
                heapq.heappush(min_heap, (arr[array_idx][element_idx + 1], array_idx, element_idx + 1))
        
        return result