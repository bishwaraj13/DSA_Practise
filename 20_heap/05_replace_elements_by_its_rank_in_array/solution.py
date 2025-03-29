# https://www.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1
import heapq

class Solution:
    def replaceWithRank(self, N, arr):
        # Create list of (value, index) pairs
        heap = [(arr[i], i) for i in range(N)]
        
        # Heapify the list (converts to min-heap)
        heapq.heapify(heap)
        
        # Initialize result array
        result = [0] * N
        
        # Extract elements and assign ranks
        prev_val = None
        rank = 0
        
        for _ in range(N):
            val, idx = heapq.heappop(heap)
            
            # If we see a new value, increase the rank
            if val != prev_val:
                rank += 1
            
            # Assign rank to the original position
            result[idx] = rank
            prev_val = val
        
        return result