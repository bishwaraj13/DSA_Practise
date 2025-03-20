# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
from typing import List
import heapq

class Solution:
    
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # If start is already equal to end, no steps needed
        if start == end:
            return 0
        
        # Initialize distance array
        distance = [float('inf')] * 100000
        
        # Min-heap to store (steps, current_number)
        min_heap = [(0, start)]
        distance[start] = 0
        
        while min_heap:
            steps, current = heapq.heappop(min_heap)
            
            # If we've reached the end
            if current == end:
                return steps
            
            # If we've already found a better path to this node, skip
            if steps > distance[current]:
                continue
            
            # Try multiplying with each number in the array
            for num in arr:
                next_num = (current * num) % 100000
                
                # If this is a shorter path to next_num
                if steps + 1 < distance[next_num]:
                    distance[next_num] = steps + 1
                    heapq.heappush(min_heap, (steps + 1, next_num))
        
        # If end is unreachable
        return -1