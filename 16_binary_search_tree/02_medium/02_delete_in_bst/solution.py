# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            return self.restructure(root)

        curr = root

        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.restructure(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.restructure(curr.right)
                    break
                else:
                    curr = curr.right

        return root

    def restructure(self, curr):
        if not curr.left:
            return curr.right
        elif not curr.right:
            return curr.left
        
        # we will return curr.left 
        # because we connect curr's parent directly to curr.left
        # In the process, we need to attach right subtree of curr,
        # to the rightmost children of curr's left subtree
        rightChild = curr.right

        # rightmost child of left subtree
        lastRight = self.findLastRight(curr.left)

        # attach curr's right tree to extreme right of curr's left subtree
        lastRight.right = rightChild

        # return curr's left
        return curr.left

    
    def findLastRight(self, curr):
        while curr.right:
            curr = curr.right
        return curr
        