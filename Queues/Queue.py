class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

    def Enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True

    def Dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:  
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp.value


new_queue = Queue(10)
new_queue.Enqueue(20)
new_queue.Enqueue(30)
new_queue.Dequeue()
new_queue.print_queue()     

