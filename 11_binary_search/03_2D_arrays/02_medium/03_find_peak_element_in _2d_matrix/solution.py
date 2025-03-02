# https://leetcode.com/problems/find-a-peak-element-ii/
# Here binary search is ONLY used to cut half the search space.
# And finding max in a column is the best way to get best shot at peak, 
# because up and down comparison is fixed for you that way.
from typing import *

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])

        low = 0
        high = COLS - 1

        while low <= high:
            mid = (low + high) // 2
            maxRowIndex = self.findMaxIndex(mat, ROWS, COLS, mid)

            left = -1
            right = -1

            if mid-1>=0:
                left = mat[maxRowIndex][mid-1]

            if (mid + 1) < COLS:
                right = mat[maxRowIndex][mid+1]

            if mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid] > right:
                return [maxRowIndex, mid]

            elif (mat[maxRowIndex][mid] < left):
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]

    def findMaxIndex(self, mat, n, m, col):
        maxValue = -1
        index = -1

        for i in range(n):
            if mat[i][col] > maxValue:
                maxValue = mat[i][col]
                index = i
            
        return index