class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [None] * capacity
        self.size = 0

    def hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, val):
        index = self.hash(key)

        if self.nodes[index]: # check if node already exists at that index
            curr = self.nodes[index] 
            while curr:
                if curr.key == key: # if the key already exists, update the val
                    curr.value = val 
                    return
                curr = curr.next

            new_node = Node(key, val)
            new_node.next = self.nodes[index]
            self.nodes[index] = new_node
            self.size += 1
        else: # there is not a node that index
            new_node = Node(key, val)
            self.nodes[index] = new_node
            self.size += 1

    def search(self, key):
        index = self.hash(key) % self.capacity
        curr = self.nodes[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next