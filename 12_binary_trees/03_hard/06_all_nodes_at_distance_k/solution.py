# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # step 1: get parents pointers for every node using level order traversal
        parent_dict = self.markParents(root)

        # step 2: visit nodes radially in BFS way from target
        visited = []
        visited.append(target)
        queue = deque()
        queue.append(target)
        curr_level = 0

        while queue:
            level_size = len(queue)
            if curr_level == k:
                break

            for i in range(level_size):
                curr = queue.popleft()

                # check left child
                if curr.left and curr.left not in visited:
                    queue.append(curr.left)
                    visited.append(curr.left)

                # check right child
                if curr.right and curr.right not in visited:
                    queue.append(curr.right)
                    visited.append(curr.right)

                # check parent
                if curr in parent_dict and parent_dict[curr] not in visited:
                    queue.append(parent_dict[curr])
                    visited.append(parent_dict[curr])
                    
            curr_level += 1

        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr.val)

        return result

    def markParents(self, root: TreeNode):
        if not root:
            return {}
        hashmap = {}
        queue = deque()

        queue.append(root)

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    hashmap[node.left] = node

                if node.right:
                    queue.append(node.right)
                    hashmap[node.right] = node

        return hashmap
