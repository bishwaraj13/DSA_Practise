# https://leetcode.com/problems/binary-search-tree-iterator/description/
# If in following code, you create pushAllRight, and create before function instead of next, etc..
# you get reversed inorder traversal
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAllLeft(root)

    def pushAllLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            self.pushAllLeft(node.right)
            return node.val 

    def hasNext(self) -> bool:
        if not self.stack:
            return False
        return True
