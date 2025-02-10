# https://leetcode.com/problems/balanced-binary-tree
# this solution is built on top of maximum depth binary tree
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if left_height == float("-inf") or right_height == float("-inf"):
                return float("-inf")

            # if tree is not balanced, we return float("-inf")
            if abs(left_height-right_height) > 1:
                return float("-inf")

            # we return height normally if tree is balanced
            return 1 + max(left_height, right_height)

        output = dfs(root)

        if output != float("-inf"):
            return True

        return False
