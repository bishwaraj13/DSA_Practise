# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from collections import deque
from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        if not root:
            return s

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr = queue.popleft()
                if not curr:
                    s = s + "#,"
                else:
                    s = s + f"{curr.val},"

                    queue.append(curr.left)
                    queue.append(curr.right)

        return s
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        queue = deque()
        node_list = data[0:len(data)-1].split(",")

        # make node_list as queue
        node_list = deque(node_list)
        root_val = int(node_list.popleft())

        # remove root from node_list
        root = TreeNode(root_val)
        queue.append(root)

        while queue:
            curr = queue.popleft()

            # get left element from node_list
            next_elem = node_list.popleft()

            if next_elem == "#":
                curr.left = None
            else:
                left_node = TreeNode(int(next_elem))
                curr.left = left_node
                queue.append(left_node)

            # get right element from node_list
            next_elem = node_list.popleft()

            if next_elem == "#":
                curr.right = None
            else:
                right_node = TreeNode(int(next_elem))
                curr.right = right_node
                queue.append(right_node)

        return root

            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))