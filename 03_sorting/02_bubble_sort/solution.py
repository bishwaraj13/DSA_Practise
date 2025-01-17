class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        last_index = len(arr) - 1
        
        while (last_index >= 0):
            for i in range(1, last_index+1):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    
            last_index-=1