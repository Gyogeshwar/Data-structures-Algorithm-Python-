# Node 
class Node:
    # Constructor
    def __init__(self,value):
        self.value = value
        self.next = None

# Linked List
class LinkedList:
    # Constructor
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    # Append node to linkedlist
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    # Prepend node to linked list
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    # Insert node in linked list 
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)  

        new_node = Node(value)         
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # Pop last element of the lnked list            
    def pop(self):
        if self.head is None:
            #print('linked list is empty.')
            return None
        else:
            temp = self.head
            pre = temp
            while(temp.next is not None):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None   
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value 
    # Pop first element from linked list
    def pop_first(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
    # Remove node from linked list
    def remove(self, index):
        if index < 0 or index > self.length-1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop() 
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp        
                     
    # Print Whole linked list       
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # Get perticuler node from linked list
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp
    # Set perticuler node from linked list
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
             temp.value = value
             return True
        else:
            return False 
    # Reverce whole linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before =  None
        for _ in range(self.length):
            after = temp.next 
            temp.next = before  
            before = temp  
            temp = after      
        return True        

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.prepend(10)
my_linked_list.insert(3, 0)

my_linked_list.print_list()

my_linked_list.remove(4)
#my_linked_list.reverse()
print("after remove:")
my_linked_list.print_list()
#print(my_linked_list.set_value(2,8))
print("get")
print(my_linked_list.get(2))
#print(my_linked_list.pop())
#print(my_linked_list.pop())

