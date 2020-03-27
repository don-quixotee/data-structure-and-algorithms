class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def size(self):
        return len(self.items)

if __name__ == "__main__":

    q = Queue()
    q.enqueue("hey")
    q.enqueue("don")
    q.enqueue("5")
    q.dequeue()
    q.size()
    