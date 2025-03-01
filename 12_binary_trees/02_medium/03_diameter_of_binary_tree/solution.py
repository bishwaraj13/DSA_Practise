# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_value = 0

        def dfs(node):
            nonlocal max_value
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_value = max(max_value, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)
        
        return max_value