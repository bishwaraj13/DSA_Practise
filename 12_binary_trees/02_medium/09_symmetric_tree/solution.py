# https://leetcode.com/problems/symmetric-tree/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricCheck(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left or not right:
                return left == right

            if left.val != right.val:
                return False

            return (
                isSymmetricCheck(left.left, right.right) 
                and isSymmetricCheck(left.right, right.left)
            )

        if not root:
            return True

        return isSymmetricCheck(root.left, root.right)