# https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
# this solution includes upperBound as tool
class Solution:
    def median(self, mat):
        ROWS = len(mat)
        COLS = len(mat[0])
        result = -1
        
        median_position = (ROWS * COLS) // 2
        
        low = float("inf")
        high = float("-inf")
        
        # get low as min value of 2d array
        # and get high as max value of 2d array
        for i in range(ROWS):
            low = min(low, mat[i][0])
            high = max(high, mat[i][COLS-1])
        
        # search space is from smallest element to largest element in array
        while low <= high:
            mid = (low + high) // 2
            countSmallerOrEqualElements = self.getCountOfSmallerElements(
                mat, ROWS, COLS, mid
            )
            
            if countSmallerOrEqualElements <= median_position:
                low = mid + 1
            else:
                # Ques: what is the guarantee that mid is part of array?
                # mid may not be part of matrix, but on further binary search iteration,
                # the final result will be something that's in the matrix,
                # because its the smallest element that suffices the condition of 
                # having smaller or equal elements > median_position
                result = mid
                high = mid - 1
        
        return result
    
    def getCountOfSmallerElements(self, mat, ROWS, COLS, x):
        count = 0
        
        for i in range(ROWS):
            count += self.upperBound(mat[i], x, COLS)
            
        return count
    
    def upperBound(self, arr, x: int, n:  int) -> int:
        low = 0
        high = n - 1
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] > x:
                # go more left to see if there is anymore smaller index
                ans = mid
                high = mid - 1
            else:
                # go rightward
                low = mid + 1
        
        return ans