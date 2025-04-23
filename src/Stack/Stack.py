class Stack:
    def __init__(self):
        self.items = []
    
    def empty(self):
        if self.items == []:
            return True
        return False

    def push(self, val):
        self.items.append(val)

    def printStack(self):
        print(self.items)
        return self.items
    
    def size(self):
        size = 0
        for item in self.items:
            size += 1

        return size
    
    def pop(self):
        if self.empty():
            print("No items to pop.")
            return
        
        last = self.items[-1]
        self.items = self.items[0:-2]
        return last
    
    def top(self):
        if self.empty():
            return
        
        return self.items[-1]