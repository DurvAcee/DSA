class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def append(self, newnode) -> None:
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
        self.count += 1

    def prepend(self, newnode) -> None:
        temp = self.head
        self.head = newnode
        newnode.next = temp
        del temp
        self.count += 1

    def insertAt(self, newnode, pos) -> None:
        if pos is not 0:
            temp = self.head
            cnt = 0
            while temp and cnt < pos:
                temp = temp.next
                cnt += 1
            newnode.next = temp.next
            temp.next = newnode
        else:
            self.prepend(newnode) 

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
thirdNode = Node('Web Dev')
ll = LinkedList()
ll.append(firstNode)
ll.append(secondNode)
newnode = Node('SWE')
ll.prepend(newnode)
ll.insertAt(thirdNode, 0)
ll.print()
ll.length()