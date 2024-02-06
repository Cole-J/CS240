'''
Cole Johnson 2/6
For CS240
'''

# creates a node to store the data
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class hashtable_linkedlist:
    def __init__(self, size, base, mod):
        self.size = size
        self.base = base
        self.mod = mod
        self.array = [None] * size # creates an empty array

    # hash function from hashfunction.py in HW5
    # gets the hash of a key
    def hash(self, key):
        value = 0
        for char in key:
            value = (value * self.base + ord(char)) % self.mod
        return value
    
    def add(self, key, data):
        # gets the hash index
        index = self.hash(key)
        # creates the data node
        data = Node(key, data)
        # check if there is a node in that slot
        if (self.array[index] is None):
            # if not, add
            self.array[index] = data
        else:
            # if there is then loop through the nodes until the end
            current_node = self.array[index]
            while (current_node.next is not None):
                current_node = current_node.next
            # add data to the end of the linked list
            current_node.next = data
            
    def get(self, key):
        # gets the hash index
        index = self.hash(key)
        # gets the linked list of the hash
        current_node = self.array[index]
        # loop through each node in the list
        while (current_node is not None):
            # if the current nodes key equals the key parameter
            if (current_node.key == key):
                # return the data
                return current_node.data
            # if not go to the next node
            current_node = current_node.next
        # no node with the key matching the key parameter
        return None
        
table = hashtable_linkedlist(10, 33, 10)

table.add("cole", 'a')
table.add("henery", 'b')
table.add("jason", 'c')
table.add("stephon", 'd')

print(table.array)

print(table.get("cole"))
print(table.get("henery"))
print(table.get("jason"))
print(table.get("stephon"))
print(table.get("stephonnnn"))