class Node:
    # constructor
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    # constructor
    def __init__(self):
        self.root = None

    # insert new node to tree
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right 

    # check value is present in tree or not
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.right
            else:
                return True
        return False      
    # minimum value in tree
    def minimum_Value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value    











my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(5)
print(my_tree.minimum_Value(my_tree.root))
print(my_tree.minimum_Value(my_tree.root.right))
#print(my_tree.root.value)
#print(my_tree.root.left.value)
#print(my_tree.root.right.value)
print(my_tree.contains(7))