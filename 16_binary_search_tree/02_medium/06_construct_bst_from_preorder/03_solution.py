# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        self.i = 0

        return self.build(preorder, float("inf"))

    def build(self, preorder, upperBound) -> Optional[TreeNode]:
        if self.i >= len(preorder) or preorder[self.i] > upperBound:
            return None

        # create root
        root = TreeNode(preorder[self.i])
        self.i += 1

        # initialize left subtree
        root.left = self.build(preorder, root.val)
        root.right = self.build(preorder, upperBound)

        return root
