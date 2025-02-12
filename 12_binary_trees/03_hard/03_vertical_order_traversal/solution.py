# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vertical_dict = {}
        queue = deque()
        # store (node, axis, level) in queue
        queue.append((root, 0, 0))

        while queue:
            queue_size = len(queue)
            level_nodes = []

            for i in range(queue_size):
                node, axis, level = queue.popleft()
                level_nodes.append((node.val, axis, level))

                if node.left:
                    queue.append((node.left, axis-1, level+1))
                if node.right:
                    queue.append((node.right, axis+1, level+1))

            # process level nodes
            for val, axis, level in level_nodes:
                if axis in vertical_dict:
                    vertical_dict[axis].append((level, val))
                else:
                    vertical_dict[axis] = [(level, val)]

        result = []

        for axis in sorted(vertical_dict.keys()):
            column = sorted(vertical_dict[axis], key=lambda x: (x[0], x[1]))
            result.append([val for level, val in column])

        return result
            
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))
print(Solution().verticalTraversal(root))
