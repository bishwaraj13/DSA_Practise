# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        if root is None:
            return result

        stack.append(root)

        while stack:
            curr_node = stack.pop()
            result.append(curr_node.val)

            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)

        return result
