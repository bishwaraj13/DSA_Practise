# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
from typing import *

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        n = len(arr)
        ans = -1
        
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                ans = mid
                low = mid + 1
            elif arr[mid] > k:
                high = mid - 1
                
        return ans
    
print(Solution().findFloor([5, 7, 7, 8, 8, 10], 8))