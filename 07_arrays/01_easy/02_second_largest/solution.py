# https://www.geeksforgeeks.org/problems/second-largest3735
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
            
        largest = second_largest = float('-inf')
        
        for elem in arr:
            if elem > largest:
                second_largest = largest
                largest = elem
            elif elem < largest and elem > second_largest:
                second_largest = elem
                
        return second_largest if second_largest != float('-inf') else -1