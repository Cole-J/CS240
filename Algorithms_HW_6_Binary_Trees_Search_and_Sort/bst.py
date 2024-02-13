'''
Cole Johnson 2/12
For CS240
'''


# ========== pseudo code ========== #

'''
function to generate a bst
    parameter is an array
    sort array
    find mid index
    create node from mid index
    recursive call to the left of the root with the left of the array
    recursive call to the right of the root with the right of the array
    return the starting root

node class
    key
    data
    left node
    right node

binary search tree class
    init:
        generate a root using the generate bst function

    add function
        if root exists
            loop while root exists
                if passed key is less than root key
                    go to the right root
                    is right root empty
                        add new node
                else
                    go to the left root
                    is the left root empty
                        add new node
    
    search function
        if root exists
            while root is not none
                if key > root key
                    return root data
                elif key > root key
                    go to right of root
                else key <= root key
                    go to left of root

    print functions
        if root exists
            # print root data for pre order
            traverse to roots left
            # print root data for in order
            traverse to roots right
            # print root data for post order
'''

# ========== function code ========== #


'''generate function has O(n) time complexity'''

# function to generate a bst from a passed array
def generate_bst(arr):
    # if there is nothing left in the array
    if not arr:
        return None
    # sort the current array
    sorted_arr = sorted(arr)
    # get the mid index of the current array
    mid = len(sorted_arr) // 2
    # create a new node
    root = Node(sorted_arr[mid][0], sorted_arr[mid][1])
    # generate its left side with the left of the current array
    root.left = generate_bst(sorted_arr[:mid])
    # generate its right side with the right of the current array
    root.right = generate_bst(sorted_arr[mid + 1:])
    # return the final root
    return root


# ========== class code ========== #


# a class to store the trees keys and data
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"key: {self.key}, data: {self.data}"

# a class to create and control the binary search tree
class BST:
    def __init__(self, array, auto_generate = True):
        # for the init create the root using the generate function
        self.root = None
        if auto_generate: # auto generate the bst
            self.root = generate_bst(array)
        
    '''add function has O(log(n)) time complexity'''

    # function to add a new node to the tree
    def add(self, key, data):
        # if there is no root create a new node for it
        if self.root is None:
            self.root = Node(key, data)
            return
        # copy of the root for the loop
        current = self.root
        while current is not None:
            # if the new key is greater than the current key
            if key > current.key:
                # is the right empty
                if current.right is None:
                    # create a new node
                    current.right = Node(key, data)
                    return
                else: # if no continue to the right
                    current = current.right
            # if the new key is less than the current key
            else:
                # is the left empty
                if current.left is None:
                    # create a new node
                    current.left = Node(key, data)
                    return
                # if no continue to the left
                else:
                    current = current.left
    
    '''search function has O(log(n)) time complexity'''

    # a function to search the try by a given index
    def search(self, key):
        # if the root exists
        if self.root == None:
            return None
        # copy of the root for loop
        current = self.root
        while current is not None:
            # key is equal to the current nodes key
            if key == current.key:
                return current.data
            # key is greater than the current nodes key
            elif key > current.key:
                current = current.right
            else:
            # key is less than the current nodes key
                current = current.left
        return None


    '''print functions have O(n) time complexity'''

    # print data in pre order
    def print_pre_order(self, root = 0):
        # checks if its the first run of the function
        if root == 0:
            root = self.root
        # if current root exists
        if root:
            # print pre order
            print(root)
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)
    
    # print data in pre order
    def print_in_order(self, root = 0):
        # checks if its the first run of the function
        if root == 0:
            root = self.root
        # if current root exists
        if root:
            self.print_pre_order(root.left)
            # print in in order
            print(root)
            self.print_pre_order(root.right)
    
    # print data in pre order
    def print_post_order(self, root = 0):
        # checks if its the first run of the function
        if root == 0:
            root = self.root
        # if current root exists
        if root:
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)
            # print in post order
            print(root)


# ========== main code ========== #
    

#array = [(4, 'a'), (2, '56'), (5, 'as'), (1, '412'), (6, '6d'), (3, 'dsa'), (7, '7')]
array = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]


tree = BST(array)

tree.add(8, 'h')

print(tree.search(5))

tree.print_pre_order()
#tree.print_in_order()
#tree.print_post_order()