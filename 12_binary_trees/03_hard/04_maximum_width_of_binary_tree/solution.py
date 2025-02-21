# https://leetcode.com/problems/maximum-width-of-binary-tree/
from collections import deque
from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 0

        queue = deque()
        queue.append((root, 0))

        while queue:
            level_size = len(queue)
            current_level = []
            min_index_current_level = queue[0][1]
            first_index = queue[0][1]
            last_index = queue[level_size-1][1]

            for i in range(level_size):
                curr_node, index = queue.popleft()
                current_level.append((curr_node, index))

                if curr_node.left:
                    queue.append((curr_node.left, 2*(index-min_index_current_level)+1))

                if curr_node.right:
                    queue.append((curr_node.right, 2*(index-min_index_current_level)+2))

            ans = max(ans, last_index-first_index+1)

        return ans