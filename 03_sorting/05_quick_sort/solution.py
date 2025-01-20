# https://www.geeksforgeeks.org/problems/quick-sort
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            
            self.quickSort(arr, low, pIndex-1)
            self.quickSort(arr, pIndex+1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            while i <= high and arr[i] <= pivot:
                i += 1
                
            while j >= low and arr[j] > pivot:
                j -= 1
                
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # j-th index is where pivot element should be
        arr[low], arr[j] = arr[j], arr[low]
        
        return j