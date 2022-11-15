class Node:
    # constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # append the node to DLL
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail  
            self.tail = new_node
        self.length += 1
        return True 
    # prepend node to DLL
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    # insert bode in DLL
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True        
        pre = self.get(index -1)
        new_node.prev = pre
        new_node.next = pre.next
        pre.next = new_node
        new_node.next.prev = new_node
        self.length += 1
        return True        
    # pop node from DLL
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:    
            self.tail = temp.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp    
    # pop node from DLL
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            temp.prev = None
            self.head.prev = None
        self.length -= 1
        return temp    
    # remove node from DLL
    def remove(self, index):
        if index < 0 or index > self.length-1:
            return False
        if index == 0:
            self.pop_first()
            return True
        if index == self.length-1:
            self.pop()
            return True
        temp = self.get(index-1)
        temp.next = temp.next.next
        temp.next.prev = temp
        self.length -= 1
        return temp
             
    # get value at from perticular index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for i in range(index):
                temp = temp.next 
        else:
            temp = self.tail
            for i in range(self.length - 1, index, -1):
                temp= temp.prev        
        return temp 
    # set value of perticular node
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False               
    # print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



dll = DoublyLinkedList(10)
dll.append(23)
dll.prepend(5)
print("all")
dll.print_list()
#print("pop")
#print(dll.pop())
#print("pop_first")
#print(dll.pop_first())
#print("get")
#print(dll.get(2))
#dll.set_value(2, 8)
print(dll.length)
print(dll.remove(-1))
print("all")
dll.print_list()