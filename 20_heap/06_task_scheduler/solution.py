from collections import Counter
from typing import *
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency of each task
        task_counts = Counter(tasks)

        # create a max heap
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        # Process tasks until all are completed
        while max_heap:
            # Store tasks that need cooling
            temp = []
            cycle = n + 1  # Process up to n+1 tasks in each cycle
            
            # Process as many high-frequency tasks as possible in this cycle
            while cycle > 0 and max_heap:
                count = -heapq.heappop(max_heap)  # Get most frequent task
                if count > 1:  # If task still has occurrences left
                    temp.append(-(count - 1))  # Put it back with decremented count
                cycle -= 1
                time += 1
            
            # Add tasks back to heap after cooling period
            for count in temp:
                heapq.heappush(max_heap, count)
            
            # If heap is empty, we're done
            if not max_heap:
                break
                
            # If cycle > 0, we need to idle for remaining slots in cycle
            time += cycle  # Add idle time
        
        return time