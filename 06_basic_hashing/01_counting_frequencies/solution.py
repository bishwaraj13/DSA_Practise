# https://www.geeksforgeeks.org/problems/frequency-of-array-elements
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        result = [0] * len(arr)
        
        for element in arr:
            result[element-1] = 1 + result[element-1]
            
        return result