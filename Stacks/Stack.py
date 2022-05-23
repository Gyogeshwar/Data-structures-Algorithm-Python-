class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:    
            new_node.next = self.top
            self.top = new_node
        self.height += 1       
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value 

    def print_stack(self):
        temp = self.top
        for _ in range(self.height):
            print (temp.value)
            temp = temp.next


new_stack = Stack(20)

new_stack.push(10)
new_stack.push(11)
print(new_stack.pop())
new_stack.print_stack()