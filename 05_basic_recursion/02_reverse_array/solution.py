# https://www.geeksforgeeks.org/problems/reverse-an-array/0
class Solution:
    def reverseArray(self, arr):
        self.reverseArrayRecursive(arr, 0, len(arr)-1)
    
    def reverseArrayRecursive(self, arr, left: int, right: int):
        if left >= right:
            return
        
        arr[left], arr[right] = arr[right], arr[left]
        
        return self.reverseArrayRecursive(arr, left+1, right-1)