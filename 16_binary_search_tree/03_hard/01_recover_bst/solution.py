# https://leetcode.com/problems/recover-binary-search-tree/
# explanation: https://www.youtube.com/watch?v=ZWGW7FminDM
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder
        def dfs(curr, prev, violated):
            if not curr:
                return None

            dfs(curr.left, prev, violated)

            if prev[0] and prev[0].val > curr.val:
                # check if first violation
                if not violated[0]:
                    violated[0] = prev[0]
                    violated[1] = curr
                else:
                    # if this is second violation
                    violated[2] = curr
            prev[0] = curr
            dfs(curr.right, prev, violated)

        violated = [None] * 3
        # use list to make prev mutable
        # because in inorder traversal, we will encounter root first
        # but the one which would become its prev (in terms of getting printed previously)
        # will be traversed after root.
        # During backtracking, root should get access to updated version of prev
        prev = [TreeNode(float("-inf"))]
        dfs(root, prev, violated)

        node1 = None
        node2 = None

        # case: non - adjacent swapping
        if violated[0] and violated[2]:
            # swap them
            node1 = violated[0]
            node2 = violated[2]
        else:
            # case: adjacent swapping
            node1 = violated[0]
            node2 = violated[1]

        # swap violated nodes   
        node1.val, node2.val = node2.val, node1.val

        return root              
        