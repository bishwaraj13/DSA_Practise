# https://leetcode.com/problems/binary-tree-postorder-traversal/
# clever trick built on top of solution_iterative.py
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = []
        result = []

        if not root:
            return result

        stack1.append(root)

        while stack1:
            root = stack1.pop()
            result.append(root.val)

            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
    
        return result[::-1]