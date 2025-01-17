# selection sort
class Solution: 
    def selectionSort(self, arr):
        for index in range(len(arr)):
            # find min element in the arr[i:]
            # the in-built code takes O(n) time
            min_index = arr.index(min(arr[index:]), index)
            
            # swap i-th value with min_index-th
            arr[index], arr[min_index] = arr[min_index], arr[index]
            