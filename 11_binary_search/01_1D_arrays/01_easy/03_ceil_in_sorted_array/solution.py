from typing import *

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findCeil(self,arr,k):
        n = len(arr)
        ans = -1
        
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            elif arr[mid] > k:
                ans = mid
                high = mid - 1
                
        return ans