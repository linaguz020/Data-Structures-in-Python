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
        
        new_list = []
        for i in range(0, self.size() - 1):
            new_list.append(self.items[i])
        last = self.items[-1]
        self.items = new_list
        return last