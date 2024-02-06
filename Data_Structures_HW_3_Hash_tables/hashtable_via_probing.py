'''
Cole Johnson 2/6
For CS240
'''

class hashtable_probe:
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
    
    # add function
    # adds data to the array with the index based off the key
    def add(self, key, data):
        # gets the hash index
        index = self.hash(key)
        # loops from the index to the max size to find a open slot
        # when a slot is found data is added to that slot
        while (index < self.size):
            if (self.array[index] is None):
                self.array[index] = (key, data)
                break
            index += 1
            if (index == self.size):
                print(f"could not add {index}")
    
    # get function
    # get data from the array with the datas key
    def get(self, key):
        # gets the hash index
        index = self.hash(key)
        # loops from the index to the max size to get those indexes key and data
        # if the indexes key equals the passed key the data is returned
        while (index < self.size):
            if (self.array[index][0] == key):
                return self.array[index][1]
            index += 1
            if (index == self.size):
                print(f"could not find {key}")
        return None

table = hashtable_probe(10, 33, 10)

table.add("cole", 'a')
table.add("henery", 'b')
table.add("jason", 'c')
table.add("stephon", 'd')

print(table.array)