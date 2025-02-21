# https://www.naukri.com/code360/problems/childrensumproperty_790723
from os import *
from sys import *
from collections import *
from math import *

class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
def changeTree(root): 
    if not root:
        return root
        
    def dfs(node, val):
        if val > node.data:
            node.data = val

        if not node.left and not node.right:
            return node.data

        left_val = 0
        right_val = 0

        if node.left:
            left_val = dfs(node.left, node.data)
        if node.right:
            right_val = dfs(node.right, node.data)

        node.data = left_val + right_val
        return node.data

    dfs(root, root.data)

    return root