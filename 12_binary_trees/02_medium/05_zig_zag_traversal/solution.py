# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        level_number = 0

        while queue:
            level_size = len(queue)

            level = []
            for i in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if level_number % 2 != 0:
                level = level[::-1]
            result.append(level)
            level_number += 1

        return result