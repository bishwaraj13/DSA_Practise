# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Did it using Morris Traversal
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Note: Inorder traversal returns sorted list, that helps
        curr = root
        counter = 0

        while curr:
            if not curr.left:
                counter += 1
                if counter == k:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left

                while (prev.right and prev.right != curr):
                    prev = prev.right

                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    counter += 1
                    if counter == k:
                        return curr.val
                    curr = curr.right

        return None