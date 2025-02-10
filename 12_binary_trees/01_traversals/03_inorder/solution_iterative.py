from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        while True:
            if (root):
                stack.append(root)
                root = root.left

            else:
                if not stack:
                    break

                root = stack.pop()
                result.append(root.val)

                root = root.right

        return result
    
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(Solution().inorderTraversal(root))