"""
adding element at the start of a linkedlist
"""

class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__ (self):
        self.head = None


    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def Insert(self, newdata):

        NewNode = Node(newdata)

        NewNode.next = self.head
        self.head = NewNode


llist = Linkedlist()
llist.head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)

llist.head.next = second
second.next = third
third.next = forth

llist.Insert(5)
llist.printlist()