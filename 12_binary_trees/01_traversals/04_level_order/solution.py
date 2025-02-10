# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for i in range(level_size):
                curr_node = queue.popleft()
                current_level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(current_level)

        return result
