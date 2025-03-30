# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
import heapq

def minCost(arr):
    # Create a priority queue
    # By default, heapq provides a min-heap
    heapq.heapify(arr)

    # Initialize result
    res = 0

    # While size of priority queue is more than 1
    while len(arr) > 1:
      
        # Extract shortest two ropes from pq
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        # Connect the ropes: update result and
        # insert the new rope to pq
        res += first + second
        heapq.heappush(arr, first + second)

    return res

if __name__ == "__main__":
  
    arr = [4, 3, 2, 6]
    print(minCost(arr))
