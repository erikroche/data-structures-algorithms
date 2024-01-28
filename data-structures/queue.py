class Node:
    def __init__ (self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def enque(self, item):
        new_node = Node(item)

        if not self.head:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def deque(self):
        if not self.head:
            return None

        self.length -= 1
        head = self.head
        self.head = self.head.next
        head.next = None

        return head.value


    def peek(self):
        return self.head.value
    

my_queue = Queue()

my_queue.enque(9)
my_queue.enque(6)
my_queue.enque(5)
my_queue.enque(4)
my_queue.enque(3)
my_queue.enque(2)
my_queue.enque(1)

print(my_queue.peek())

print(my_queue.deque())
print(my_queue.deque())

print(my_queue.peek())

my_queue.enque(4)

my_queue.enque(14)
my_queue.enque(46)

for i in range(my_queue.length):
    print(my_queue.deque())
