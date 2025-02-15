# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, n, head, key):
        temp = head
        
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        
        return False