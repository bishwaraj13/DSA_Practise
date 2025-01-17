# insertion sort
class Solution:
    def insertionSort(self, arr):
        sorted_till = 0
        
        while sorted_till < len(arr) - 1:
            # the next index whose value has to be inserted in sorted array
            next = sorted_till + 1
            
            while next > 0 and arr[next] < arr[next-1]:
                arr[next], arr[next-1] = arr[next-1], arr[next]
                next-=1
            
            # we sorted one more element in the array 
            sorted_till += 1