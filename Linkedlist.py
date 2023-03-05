class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Llist:
    def __int__(self):
        self.head = None

    def displayList(self):
        tempVariable = self.head
        while(tempVariable):
            print(tempVariable.value)
            tempVariable = tempVariable.next

list = Llist()
list.head = Node(1)
nextHead = Node(2)
nextHead1 = Node(3)

list.head.next = nextHead
nextHead.next = nextHead1

list.displayList()