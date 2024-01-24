'''
Cole Johnson 1/16/2024
for CS240
'''
# ========== class definitions ========== #

# defines a node class which has a data variable and a next node pointer
class NODE:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# defines the linked list class with the first node in the chain as well as its related functions
class linked_list:
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
            print("ERROR (read): " + str(pos) + " not added as its out of bounds")
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
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # loops through the list while the count variable is less than pos - 1
        while (cn is not None and i < pos - 1):
            i += 1
            cn = cn.next_node
        # inserts the node into the list
        node.next_node = cn.next_node
        cn.next_node = node

    # function to delete data in a given position
    def delete(self, pos): # O(n) linear time complexity
        # checks that the pos is within the range
        if (pos >= self.length() or pos < 0):
            print("ERROR (delete): " + str(pos) + " not deleted as its out of bounds")
            return
        i = 0 # count variable
        cn = self.first_node # copy of the list
        # if deleting first node
        if (pos == 0):
            self.first_node = cn.next_node

        # loops until 1 before the node to be deleted
        while (cn is not None and i < pos - 1): # -1
            i += 1
            cn = cn.next_node
        # stop before node being deleted
        # skip over the node to remove it from the list
        if (cn.next_node is not None):
            cn.next_node = cn.next_node.next_node
        else:
            cn.next_node = None
        
    # function to search the list for a passed data
    # returns its position in the list
    def search(self, data): # O(n) linear time complexity
        i = 0 # count variable
        cn = self.first_node # copy of the list
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
            rn  = cn.next_node # copy of the next node
            # loops through the nodes in the list above (cn) or the current node
            # after the loop min_node is the node with the smallest data above the cn node
            while (rn is not None):
                # checks if the rn's data is less than the cn's / min data
                if rn.data < min_node.data:
                    min_node = rn
                rn = rn.next_node
            # swap the cn node and the node with the smallest data above it
            cn.data, min_node.data = min_node.data, cn.data
            cn = cn.next_node