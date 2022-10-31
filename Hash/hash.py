from types import NoneType


class HashTable:
    # constructor
    def __init__(self, size = 7):
        self.data_map = [None] * size

    # Hash function
    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # Set item
    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value]) 

    # Get item
    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None            
    
    # All keys
    def keys(self):
        key = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    key.append(self.data_map[i][j][0])

        return key            
        

    # Print map
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i, ": ", val) 


my_hash_table =HashTable()
my_hash_table.set_item('Bolts', 10)
my_hash_table.set_item('Washers', 400)
item = my_hash_table.get_item('Bolts')
print(my_hash_table.keys())
# Hash_key = my_hash_table._hash("y")
# my_hash_table.print_table()
#print(Hash_key)