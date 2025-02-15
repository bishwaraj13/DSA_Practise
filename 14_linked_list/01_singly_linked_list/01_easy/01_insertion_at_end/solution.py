# https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if not head:
            return Node(x)
            
        temp = head
        
        while temp.next:
            temp = temp.next
            
        temp.next = Node(x)
        return head