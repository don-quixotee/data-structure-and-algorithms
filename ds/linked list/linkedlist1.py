class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(Self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    
llist = Node(100)
print(llist.get_data())
llist.set_next(200)
print(llist.get_next())