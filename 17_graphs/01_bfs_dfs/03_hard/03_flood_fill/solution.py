# https://leetcode.com/problems/flood-fill/
from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        def dfs(image_copy, i, j, old_color, color):
            # check out of bounds
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS):
                return

            # if its NOT old color, we dont want anything to do with it:
            if image_copy[i][j] != old_color:
                return

            # if its already new color, dont bother
            if image_copy[i][j] == color:
                return

            image_copy[i][j] = color
            dfs(image_copy, i, j-1, old_color, color)
            dfs(image_copy, i+1, j, old_color, color)
            dfs(image_copy, i, j+1, old_color, color)
            dfs(image_copy, i-1, j, old_color, color)
            return

        image_copy = image.copy()
        old_color = image_copy[sr][sc]
        image_copy[sr][sc] = color

        dfs(image_copy, sr, sc-1, old_color, color)
        dfs(image_copy, sr+1, sc, old_color, color)
        dfs(image_copy, sr, sc+1, old_color, color)
        dfs(image_copy, sr-1, sc, old_color, color)

        return image_copy