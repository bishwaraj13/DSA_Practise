# https://leetcode.com/problems/n-queens/
from typing import *

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                # Create a deep copy and convert each row to string
                solution = []
                for r in board:
                    solution.append(''.join(r))
                ans.append(solution)
                return

            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    dfs(row+1)
                    # backtrack by reverting value
                    board[row][col] = '.'

        def isSafe(board, row, col):
            # check upward diagonal left
            temp_row = row-1
            temp_col = col-1

            while temp_row >= 0 and temp_col >= 0:
                if board[temp_row][temp_col]=='Q':
                    return False
                temp_row -= 1
                temp_col -= 1

            # check vertically upward
            temp_row = row-1

            while temp_row >= 0:
                if board[temp_row][col] == 'Q':
                    return False
                temp_row -= 1

            # check diagonally right upward
            temp_row = row-1
            temp_col = col+1

            while temp_row >= 0 and temp_col < len(board):
                if board[temp_row][temp_col] == 'Q':
                    return False

                temp_row -= 1
                temp_col += 1

            return True

        dfs(0)
        return ans