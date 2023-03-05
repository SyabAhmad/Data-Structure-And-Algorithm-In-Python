class nodeClass:
    def __init__(self, values1):
        self.values1 = values1
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtPosition(self, values1, position):
        newNode = nodeClass(values1)
        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return

        current = self.head
        currentPosition = 0
        while current is not None and currentPosition < position - 1:
            current = current.next
            currentPosition += 1

        if current is None:
            print("Position out of range")
            return

        nextNode = current.next
        current.next = newNode
        newNode.next = nextNode

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.values1)
            temp = temp.next

llist = LinkedList()
llist.insertAtPosition(3, 0)
llist.insertAtPosition(2, 0)
llist.insertAtPosition(1, 0)

# Inserting node with data=4 at position=2
llist.insertAtPosition(4, 2)
llist.insertAtPosition(7, 3)

llist.printList()