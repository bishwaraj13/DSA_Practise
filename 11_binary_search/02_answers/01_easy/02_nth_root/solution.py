# https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        low = 1
        high = m
        
        while low <= high:
            mid = (low + high) // 2
            
            val = self.isValid(mid, n, m)
            
            if val == 1:
                return mid
            elif val == 2:
                high = mid - 1
            elif val == 0:
                low = mid + 1
                
        return -1

    def isValid(self, mid, n, m):
        ans = 1
        
        for i in range(1, n+1):
            ans *= mid
            
            if ans > m:
                return 2
        
        if ans == m:
            return 1
            
        return 0