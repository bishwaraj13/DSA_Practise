# https://www.geeksforgeeks.org/problems/largest-element-in-array4009

class Solution:
    def largest(self, arr):
        largest_element = float('-inf')
        
        for element in arr:
            largest_element = max(element, largest_element)
            
        return largest_element
        