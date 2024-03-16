class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def add(self, node) -> None:
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        self.count += 1

    def print(self) -> None:
        if not self.head:
            print('List is empty')
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def length(self) -> None:
        print('Length of LinkedList is - ', self.count)



firstNode = Node('Durvesh')
secondNode = Node('Danve')
ll = LinkedList()
ll.add(firstNode)
ll.add(secondNode)
ll.print()
ll.length()




