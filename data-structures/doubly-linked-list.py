class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None
        

class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item: Node):
        node = Node(item)

        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAt(self, item: Node, idx: int):
        if idx > self.length:
            print("error")
            return
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return
        
        self.length += 1 
        
        curr = self.head
        for i in range(0, idx):
            if not curr:
                return
            
            node = Node(item)

            node.next = curr
            node.prev = curr.prev
            curr.prev = node
            if curr.prev:
                curr.prev.next = curr

    def append(self, item: Node):
        
        self.length += 1

        node = Node(item)

        if not self.tail:
            self.head = self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, item: Node):
        curr = self.head

        for i in range(0, i):
            if not curr:
                return
            
            if curr.value == item:
                break

            self.length -= 1

            if self.length == 0:
                out = self.head.value
                self.head = self.tail = None
                return out
            
            if curr.prev:
                curr.prev = curr.next
 
            if curr.next:
                curr.next = curr.prev


            if curr == self.head:
                self.head = curr.next
            
            if curr == self.tail:
                self.tail = self.prev

            curr.prev = curr.next = None
    
    def get(self, idx: int):
        return self.getAt(idx).value

    def removeAt(self, idx: int):
        node = self.getAt(idx)

        if not node:
            return None
        
    def getAt(self, idx: int):
        curr = self.head
        for i in range(0, idx):
            if not curr:
                return
            curr = curr.next
        return curr
