'''



'''
# ========== class definitions ========== #

class NODE:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
'''
class double_linked_list:
    def __init__(self):
        self.first_node = None

    def add(self, data):
        node = NODE(data)
        if (self.first_node is None):
            # no first node
            self.first_node = node
        else:
            # first node exists
            current_node = self.first_node
            while (current_node.next_node is not None):
                current_node = current_node.next_node
            node.prev_node = current_node
            current_node.next_node = node
'''

# ========== main code ========== #

# creating the double linked list
#dll = double_linked_list()
'''
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)

cn = dll.first_node # copy list
while True:
    print(cn.data)

    if (cn.next_node is None):
        break
    else:
        cn = cn.next_node


while True:
    print(cn.data)

    if (cn.prev_node is None):
        break
    else:
        cn = cn.prev_node
'''