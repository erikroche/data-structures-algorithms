class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.prev = None

class Stack:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None
        
    def push(self, item: int):
        node = Node(item)

        self.length += 1
        if not self.head:
            self.head = node
            return
        
        node.prev = self.head
        self.head = node

    def pop(self):
        if self.length == 0:
            return None
        
        head = self.head
        self.head = head.prev
        self.length -= 1
        return head.value if head else None
    
my_stack = Stack()

my_stack.push(4)
my_stack.push(5)
my_stack.push(6)

print(my_stack.pop())   # Output: 6
print(my_stack.pop())   # Output: 5
print(my_stack.pop())   # Output: 4
print(my_stack.peek())  # Output: None

