from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = []
        stack2 = []
        result = []

        if not root:
            return result

        stack1.append(root)

        while stack1:
            root = stack1.pop()
            stack2.append(root)

            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        
        while stack2:
            result.append(stack2.pop().val)

        return result