# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        curr = root

        while curr:
            # Case 1: if no left child, print root and move to right child
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            # Case 2: Go to rightmost node of left subtree, and connect link to curr
            # but before connecting thread, make sure they are not already connected to root
            else:
                prev = curr.left
                while (prev.right and prev.right != curr):
                    prev = prev.right

                # Case 2A: rightmost node is not connected to curr yet
                if not prev.right:
                    # connect the right most node to curr,
                    # print root before going to go further to left
                    prev.right = curr
                    result.append(curr.val)
                    curr = curr.left
                else:
                # case 2B: remove connection
                    prev.right = None
                    curr = curr.right

        return result

            