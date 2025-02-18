# https://leetcode.com/problems/copy-list-with-random-pointer/
from typing import *

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        dict = {}
        temp = head
        dummyNode = Node(-999)
        curr = dummyNode

        # this loop will copy all nodes and link next pointers
        while temp:
            newNode = Node(temp.val)
            newNode.random = temp.random
            dict[temp] = newNode
            curr.next = newNode
            curr = curr.next
            temp = temp.next

        # we will update the random pointer with new nodes
        curr = dummyNode.next

        while curr:
            curr.random = dict.get(curr.random)
            curr = curr.next

        return dummyNode.next
