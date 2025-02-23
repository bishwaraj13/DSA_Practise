from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            curr = root
            val = preorder[i]

            while curr:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = TreeNode(val)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = TreeNode(val)
                        break
                    else:
                        curr = curr.right

        return root
