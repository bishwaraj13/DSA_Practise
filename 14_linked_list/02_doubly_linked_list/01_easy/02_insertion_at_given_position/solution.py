# https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        newNode = Node(x)
        temp = head
        
        while p:
            temp = temp.next
            p -= 1
            
        newNode.next = temp.next
        temp.next = newNode
        newNode.prev = temp
        
        return head