'''



'''
# ========== class definitions ========== #

class NODE:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class double_linked_list:
    def __init__(self):
        self.first_node = None

    def length(self):
        i = 0
        cn = self.first_node
        while cn is not None:
            i += 1
            cn = cn.next_node
        return i

    def read(self, pos):
        if (pos > self.length()):
            print("ERROR (read): " + str(pos) + " not read as its out of bounds")
            return
        i = 0
        cn = self.first_node
        while i < pos and cn.next_node is not None:
            i += 1
            cn = cn.next_node
        return cn.data

    def insert(self, data, pos = None):
        node = NODE(data)
        if (pos == None):
            pos = self.length()

        if (pos == 0 and self.first_node is None):
            self.first_node = node
            return
        if (pos == 0 ):
            node.next_node = self.first_node
            if (self.first_node is not None):
                self.first_node.prev_node = node
            self.first_node = node
            return
        
        if (pos > self.length() or pos < 0):
            print("ERROR (insert): " + str(data) + " not inserted as its out of bounds")
            return

        i = 0
        cn = self.first_node
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node

        if (not cn):
            print("out of bound")
            return
        
        node.next_node = cn.next_node
        if (cn.next_node is not None):
            cn.next_node.prev_node = node
        node.prev_node = cn
        cn.next_node = node


    def delete(self, pos):
        if pos >= self.length():
            print("ERROR (delete): " + str(pos) + " not deleted as its out of bounds")
            return
        cn = self.first_node
        if (pos == 0):
            self.first_node = self.first_node.next_node
            self.first_node.prev_node = None
            return
        i = 0
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        if (pos == self.length() - 1):
            cn.next_node = None
            return
        cn.next_node = cn.next_node.next_node
        save_node = cn
        cn = cn.next_node
        cn.prev_node = save_node


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

# creating the double linked list
dll = double_linked_list()

dll.insert(0)
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.insert(6)

dll.delete(4)
#dll.sort()
#print(dll.search(3))
#print(dll.read(1))
#print(dll.length())

cn = dll.first_node
for i in range(dll.length()):
    #print(dll.read(i))
    p = None
    n = None
    if (cn.prev_node is not None):
        p = cn.prev_node.data
    if (cn.next_node is not None):
        n = cn.next_node.data
    print("p " + str(p) + " c " + str(cn.data) + " n " + str(n))

    cn = cn.next_node