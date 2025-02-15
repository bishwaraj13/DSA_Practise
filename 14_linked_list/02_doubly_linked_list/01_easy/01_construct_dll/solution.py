# https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None
        head = Node(arr[0])
        prev = head
        
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            prev.next = newNode
            newNode.prev = prev
            
            prev = newNode
            
        return head