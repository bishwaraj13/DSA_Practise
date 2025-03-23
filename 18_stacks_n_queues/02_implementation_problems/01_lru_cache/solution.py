# https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize cache with the given capacity
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key -> Node mappings
        
        # Initialize dummy head and tail nodes
        self.head = Node()  # Most recently used
        self.tail = Node()  # Least recently used
        
        # Connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def deleteNode(self, node):
        # Remove node from the doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertAfterHead(self, node):
        # Insert node right after the head (making it most recently used)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Key exists, move the node to the front (most recently used)
            node = self.cache[key]
            self.deleteNode(node)
            self.insertAfterHead(node)
            return node.value
        return -1  # Key doesn't exist

    def put(self, key: int, value: int) -> None:
        # If key already exists, update its value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.deleteNode(node)
            self.insertAfterHead(node)
        else:
            # If cache is at capacity, remove least recently used item (tail.prev)
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]
            
            # Add new node to the cache and after head
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insertAfterHead(new_node)