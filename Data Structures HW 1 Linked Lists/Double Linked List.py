'''
Cole Johnson 1/16/2024
for CS240
'''
# ========== class definitions ========== #

# defines a node class which has a data variable and a next and prev node pointer
class NODE:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

# defines the double linked list class with the first node in the chain as well as its related functions
class double_linked_list:
    def __init__(self):
        # first node in the list
        self.first_node = None

    # function to get the length of the list
    def length(self): # O(n) linear time complexity
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # loops while there are still nodes in the list
        while cn is not None:
            i += 1
            cn = cn.next_node
        # returns the final count
        return i

    # function to read data from a given nodes position
    def read(self, pos): # O(n) linear time complexity
        # is the desired node in the bound of the list
        if (pos > self.length()):
            print("ERROR (read): " + str(pos) + " not read as its out of bounds")
            return
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # loops while the count variable is less than the pos
        while i < pos and cn.next_node is not None:
            i += 1
            cn = cn.next_node
        # returns the data of the current node
        return cn.data

    # function to insert data into a position in the list
    def insert(self, data, pos = None): # O(n) linear time complexity
        # create a new node with the passed data
        node = NODE(data)
        # if there is no pos passed it will append the data to the end
        if (pos == None):
            pos = self.length()
        # insert conditions
        # if the list is empty
        if (pos == 0 and self.first_node is None):
            self.first_node = node
            return
        # if the pos is 0 and the list is not empty
        if (pos == 0 ):
            # insert the new node behind the first node and point the first node at it
            # also point the new first node at the old first node
            node.next_node = self.first_node
            if (self.first_node is not None):
                self.first_node.prev_node = node
            self.first_node = node
            return
        # if the pos is out of bounds
        if (pos > self.length() or pos < 0):
            # send error
            print("ERROR (insert): " + str(data) + " not inserted as its out of bounds")
            return
        # if need to move through to a valid pos
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # loops through the list while the count variable is less than pos - 1
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        # inserts the node into the list
        node.next_node = cn.next_node
        if (cn.next_node is not None):
            cn.next_node.prev_node = node
        node.prev_node = cn
        cn.next_node = node

    # function to delete data in a given position
    def delete(self, pos): # O(n) linear time complexity
        # checks that the pos is within the range
        if pos >= self.length():
            print("ERROR (delete): " + str(pos) + " not deleted as its out of bounds")
            return
        # if deleting the first node in the list
        if (pos == 0):
            # skip over the first node
            self.first_node = self.first_node.next_node
            # set the next nodes prev node to None
            self.first_node.prev_node = None
            return
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # loops until 1 before the node to be deleted
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        # now at the node before the node to be deleted
        # if the current pos is the last in the list
        # / trying to delete the last position
        if (pos == self.length() - 1):
            # skips the last node
            cn.next_node = None
            return
        # remove the current nodes next node from the list
        cn.next_node = cn.next_node.next_node
        save_node = cn
        cn = cn.next_node
        cn.prev_node = save_node

    # function to search the list for a passed data
    # returns its position in the list
    def search(self, data): # O(n) linear time complexity
        i = 0 # count variable
        cn = self.first_node # copy of list
        # loops through the loop until it reaches the end of the list
        while cn is not None:
            # if a nodes data equals the search data
            if cn.data == data:
                # stop the loop and return the nodes position
                return i
            i += 1
            cn = cn.next_node
        # if no nodes data equals the search data then return -1
        print("ERROR (search): " + str(data) + " not found, returned -1")
        return -1

    # function to sort the list
    # uses selection sort
    def sort(self): # O(n^2) quadratic time complexity
        cn = self.first_node # copy of the list
        # loops through each node in the list
        while (cn is not None):
            min_node = cn
            nn  = cn.next_node # copy of the next node
            # loops through the nodes in the list above (cn) or the current node
            # after the loop min_node is the node with the smallest data above the cn node
            while (nn is not None):
                # checks if the rn's data is less than the cn's / min data
                if nn.data < min_node.data:
                    min_node = nn
                nn = nn.next_node
            # swap the cn node and the node with the smallest data above it
            cn.data, min_node.data = min_node.data, cn.data
            cn = cn.next_node


# ========== main code ========== #

# creating the double linked list
dll = double_linked_list()

# adds data from a txt file to the double linked list
with open('numbers-2.txt', 'r') as fh:
    for i in [int(num) for num in fh.readlines()]:
        dll.insert(i)

# prints each nodes data
cn = dll.first_node
for i in range(dll.length()):
    p = None
    n = None
    if (cn.prev_node is not None):
        p = cn.prev_node.data
    if (cn.next_node is not None):
        n = cn.next_node.data
    print("prev node data " + str(p) + " current node data " + str(cn.data) + " next node data " + str(n))

    cn = cn.next_node