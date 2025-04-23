class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.items == []:
            print("Queue is empty.")
            return
        last = self.items[-1]
        self.items = self.items[1:]
        return last

    def front(self):
        if self.items == []:
            return
        return self.items[0]
    
    def back(self):
        if self.items == []:
            return
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def printQueue(self):
        print(self.items)
        return self.items