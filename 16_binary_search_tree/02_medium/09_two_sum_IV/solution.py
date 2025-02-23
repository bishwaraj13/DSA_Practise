# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode], reverse=False):
        self.stack = []
        self.reverse = reverse
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left
        
    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            if self.reverse:
                self.pushAll(node.left)
            else:
                self.pushAll(node.right)
            return node.val
        return None

    def hasNext(self) -> bool:
        if not self.stack:
            return False
        return True

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        l = BSTIterator(root)
        r = BSTIterator(root, reverse=True)

        i = l.next()
        j = r.next()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = l.next()
            else:
                j = r.next()

        return False
        