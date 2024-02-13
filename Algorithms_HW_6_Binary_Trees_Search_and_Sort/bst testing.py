'''
Cole Johnson 2/12
For CS240
'''

# ========== pseudo code ========== #

# ========== class code ========== #

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

# ========== function code ========== #

def generate_root(arr):
    if not arr:
        return None
    sorted_arr = sorted(arr)
    mid = len(sorted_arr) // 2
    root = Node(sorted_arr[mid][0], sorted_arr[mid][1])
    root.left = generate_root(sorted_arr[:mid])
    root.right = generate_root(sorted_arr[mid + 1:])
    return root

def search_pre_order(root, index, current_index=0):
    pass
def search_in_order(root, index, current_index=0):
    pass
def search_post_order(root, index, current_index=0):
    pass

# ========== main code ========== #

array = [(4, '4'), (2, '2'), (5, '5'), (1, '1'), (6, '6'), (3, '3'), (7, '7')]
root = generate_root(array)

#print(root.data)
#print(root.left.data)
#print(root.left.left.data)
##print(root.left.left.left)
##print(root.left.left.right)
##print(root.left.right)
#print(root.right.data)
#print(root.right.left.data)
##print(root.right.left.left)
##print(root.right.left.right)
##print(root.right.right)

#print(search_pre_order(root, 3))
#print(search_pre_order(root, 0))
#print(search_pre_order(root, 1))
#print(search_pre_order(root, 2))
#print(search_pre_order(root, 3))
#print(search_pre_order(root, 4))


def test_pre(root):
    if root:
        print(root.data)
        test_pre(root.left)
        test_pre(root.right)
def test_in(root):
    if root:
        test_in(root.left)
        print(root.data)
        test_in(root.right)
def test_pos(root):
    if root:
        test_pos(root.left)
        test_pos(root.right)
        print(root.data)
#test_pre(root)
#print()
#test_in(root)
#print()
#test_pos(root)
        



class BST:
    def __init__(self, arr):
        self.root = generate_root(arr)
        self.current_index = 0
        self.returnn = None

    def helper_pre_order(self, root, index):
        if root:
            if index == self.current_index:
                self.returnn = root.data
            self.current_index += 1
            self.helper_pre_order(root.left, index)
            self.helper_pre_order(root.right, index)

    def search_pre_order(self, index):
        self.current_index = 0
        self.returnn = None
        self.helper_pre_order(self.root, index)
        return self.returnn
    
    def helper_in_order(self, root, index):
        if root:
            self.current_index += 1
            self.helper_in_order(root.left, index)
            if index == self.current_index:
                self.returnn = root.data
            self.helper_in_order(root.right, index)

    def search_in_order(self, index):
        self.current_index = 0
        self.returnn = None
        self.helper_in_order(self.root, index)
        return self.returnn
    
    def helper_post_order(self, root, index):
        if root:
            self.current_index += 1
            self.helper_post_order(root.left, index)
            self.helper_post_order(root.right, index)
            if index == self.current_index:
                self.returnn = root.data

    def search_post_order(self, index):
        self.current_index = 0
        self.returnn = None
        self.helper_post_order(self.root, index)
        return self.returnn

            

tree = BST(array)
for n in range(len(array)):
    print(f"pre {tree.search_pre_order(n)}, in {tree.search_in_order(n)}, post {tree.search_post_order(n)}")