# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# The solution is built on top of maximum depth of binary tree
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum_val = float("-inf")
        def dfs(node):
            nonlocal maximum_val
            if not node:
                return 0

            # dont consider negative part
            maxL = max(0, dfs(node.left))

            # dont consider negative part
            maxR = max(0, dfs(node.right))
            
            maximum_val = max(maximum_val, maxL + maxR + node.val)

            return node.val + max(maxL, maxR)

        if not root:
            return 0
            
        dfs(root)
        return maximum_val
        