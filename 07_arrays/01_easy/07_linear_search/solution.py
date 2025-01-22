# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1

class Solution:
    def searchInSorted(self,arr, k):
        if not arr:
            return False
            
        l = 0
        r = len(arr) - 1
        return self.searchRecursively(arr, l, r, k)
            
    def searchRecursively(self, arr, l, r, k):
        if l > r:
            return False
        
        m = (l + r) // 2
        
        if arr[m] == k:
            return True
        elif k < arr[m]:
            return self.searchRecursively(arr, 0, m-1, k)
        else:
            return self.searchRecursively(arr, m+1, r, k)