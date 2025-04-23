class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
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
    
    def insert(self, val, index):
        # if list empty
        if self.head is None:
            self.add(val)
            return
        
        # if index less than or equal to 0, insert at beginning
        if index <= 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        
        # if index within list
        i = 1
        curr = self.head
        while curr:
            if i == index:
                new_node = Node(val)
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                return
            i+=1
            if curr.next is None:
                new_node = Node(val)
                curr.next = new_node
                return
            curr = curr.next

    def delete(self, index):
        if self.head is None:
            print("No nodes to remove.")
            return
        
        if index < 0:
            print("Invalid index.")
            return
        
        if index == 0:
            self.head = self.head.next
            return

        i = 1
        curr = self.head
        while curr.next:
            if i == index:
                temp = curr.next
                if temp.next:
                    curr.next = temp.next
                    return
                else:
                    curr.next = None
                    return
            i += 1
            curr = curr.next

        print("Invalid index.")
        return
    
    def combine(self, list2):
        if self.head is None:
            self.head = list2.head
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = list2.head