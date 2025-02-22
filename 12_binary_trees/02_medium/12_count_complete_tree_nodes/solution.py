# https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def findLeftHeight(node):
            ht = 0

            while node:
                ht += 1
                node = node.left

            return ht

        def findRightHeight(node):
            ht = 0

            while node:
                ht += 1
                node = node.right

            return ht

        if not root:
            return 0

        lh = findLeftHeight(root)
        rh = findRightHeight(root)

        if lh == rh:
            return 2**lh - 1
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
