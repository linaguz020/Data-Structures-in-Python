import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node.Node(data)
        # check if inserting into empty list
        if self.head is None:
            self.head = new_node
            return
        
        # if list has elements, traverse until we find the last node
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def search(self, data):
        if self.head is None:
            print("List is empty.")
            return False
        
        curr = self.head
        while curr.next:
            if data == curr.val:
                return True
            curr = curr.next

        if data == curr.val:
            return True
        return False
        

    def size(self):
        if self.head is None:
            return 0
        
        size = 1
        curr = self.head
        while(curr.next):
            size += 1
            curr = curr.next
        
        return size

    def printList(self):
        if self.head is None:
            print("Empty list.")
            return []
        
        vals = []
        curr = self.head
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        print(vals)
        return vals