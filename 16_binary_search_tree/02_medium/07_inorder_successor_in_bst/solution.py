# https://leetcode.com/problems/inorder-successor-in-bst/description/
# Problem Description:
"""
Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        curr = root
        successor = None

        while curr:
            if p.val < curr.val:
                successor = curr
                curr = curr.left
            else:
                curr = curr.right

        return successor