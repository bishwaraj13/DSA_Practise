# https://leetcode.com/problems/binary-tree-right-side-view/description/
# This can be easily done using level order traversal, but then the space complexity would be O(n)
# The below solution is preorder recursive traversal, but root-right-left.
# The worst case space complexity would be O(n) when the tree is skewed, but in general it would be O(log n)
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, level):
            if not node:
                return

            if len(result) < level:
                # its the first node of the level
                result.append(node.val)

            dfs(node.right, level+1)
            dfs(node.left, level+1)
    
        dfs(root, 1)
        return result