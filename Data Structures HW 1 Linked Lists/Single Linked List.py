'''



'''
# ========== class definitions ========== #

class NODE:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class linked_list:
    def __init__(self):
        self.first_node = None
        #self.last_node = None

    def length(self):
        i = 0
        cn = self.first_node
        while cn is not None:
            i += 1
            cn = cn.next_node
        return i
        
    def read(self, pos):
        if (pos > self.length()):
            print("ERROR (read): " + str(pos) + " not added as its out of bounds")
            return
        i = 0
        cn = self.first_node
        while i < pos and cn.next_node is not None:
            i += 1
            cn = cn.next_node
        return cn.data

    def insert(self, data, pos = None):
        node = NODE(data)
        if pos == None:
            pos = self.length()
        # conditions
        # if list is empty then pos does not matter
        if (pos == 0 and self.first_node is None):
            self.first_node = node
            return
        # if pos is 0 on a non empty list
        if (pos == 0 and self.first_node is not None):
            node.next_node = self.first_node
            self.first_node = node
            return
        # pos is out of bounds
        if (pos > self.length()):
            print("ERROR (insert): " + str(pos) + " not added as its out of bounds")
            return
        # if need to move through to a valid pos
        i = 0
        cn = self.first_node
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        node.next_node = cn.next_node
        cn.next_node = node

    def delete(self, pos):
        if pos >= self.length():
            print("ERROR (delete): " + str(pos) + " not added as its out of bounds")
        i = 0
        cn = self.first_node
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        # stop before node being deleted
        # skip over the node
        cn.next_node = cn.next_node.next_node
        
    def search(self, data):
        i = 0
        cn = self.first_node
        while cn is not None:
            if cn.data == data:
                return i
            i += 1
            cn = cn.next_node
        print("ERROR (search): " + str(data) + " not found, returned -1")
        return -1

    def sort(self):
        cn = self.first_node
        while (cn is not None):
            min_node = cn
            nn  = cn.next_node

            while (nn is not None):
                if nn.data < min_node.data:
                    min_node = nn
                nn = nn.next_node
            cn.data, min_node.data = min_node.data, cn.data
            cn = cn.next_node


# ========== main code ========== #

# creating the linked list object

ll = linked_list()

ll.insert(0)
ll.insert(1)
ll.insert(2)
ll.insert(4)
ll.insert(3, 3)
ll.insert(6,2)
ll.insert(5, 0)

ll.sort()
#print(ll.search(3))
#print(ll.read(1))
#print(ll.length())

for i in range(ll.length()):
    print(ll.read(i))
