'''
Cole Johnson 3/17/24
For CS240 Final
'''

# checklist for library file

# dll done

# bst done
# pre in post order search in bst done
 
# bfs and dfs search done

# stack done

# search r and i done

# sort array and ll done


# node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# bst function
        
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

# valid function for dfs
def valid(x, y, maze) -> bool:
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0



class LIBRARY: # LIBRARY class namespace def
    # double linked list definition
    class DOUBLE_LINKED_LIST: # O(1)
        def __init__(self):
            self.root = None

        # function to return the length of the list
        def length(self): # O(n)
            i = 0
            cn = self.root
            # loop through each node and count up
            while cn:
                i += 1
                cn = cn.next
            # return final count
            return i

        # function to read data at an index
        def read(self, index): # O(n)
            # base cases
            if (index > self.length() or index < 0):
                print("error with read")
                return None
            # loop until the index node
            i = 0
            cn = self.root
            while (i < index):
                i += 1
                cn = cn.next
            # return data
            return cn.data

        # function to insert data at a given index
        # if index is not passed it will defualt to append
        def insert(self, data, index = None): # O(n)
            node = Node(data)
            # base cases
            if (index is None):
                index = self.length()
            # no root node
            if (index == 0 and self.root is None):
                self.root = node
                return
            # insert at 0
            if (index == 0):
                node.next = self.root
                # 0 node exists
                if (self.root):
                    self.root.prev = node
                self.root = node
                return
            # error
            if (index > self.length() or index < 0):
                print("error with insert")
                return
            # loop until index node
            i = 0
            cn = self.root
            while (i < index - 1 and cn):
                i += 1
                cn = cn.next
            # insert node
            node.next = cn.next
            if (cn.next):
                cn.next.prev = node
            node.prev = cn
            cn.next = node

        # function to delete data at a given index
        def delete(self, index): # O(n)
            # base cases
            if (index >= self.length() or index < 0):
                print("error with delete")
                return
            if (index == 0):
                self.root = self.root.next
                if (self.root is not None):
                    self.root.prev = None
                else:
                    self.root = None
                return
            # loop to index node
            i = 0 
            cn = self.root 
            while (i < index - 1 and cn):
                i += 1
                cn = cn.next
            # skip over node to delete it
            # case for it node is last node
            if (index == self.length() - 1):
                cn.next = None
                return
            # skip over node and set its prev pointer
            cn.next = cn.next.next
            save_node = cn
            cn = cn.next
            cn.prev = save_node

    # stack via array def
    class STACK_ARR:
        def __init__(self, max_size): # O(1)
            self.max_size = max_size
            self.stack = []

        # function to add data to the top of a stack
        def push(self, data): # O(1)
            if not (self.isFull()):
                # add to back of array
                self.stack.append(data)

        # function to take data from the top of the stack
        def pop(self): # O(1)
            # pull data from the back of the array
            return self.stack.pop()

        # function to see if the stack is empty
        def isEmpty(self): # O(1)
            return (len(self.stack) == 0)

        # function to check if the array is full
        def isFull(self): # O(1)
            return (len(self.stack) == self.max_size)

        # function to check the data from the top of the stack without deleting it
        def peek(self): # O(1)
            return self.stack[len(self.stack) - 1]

    # stack via linked list def
    class STACK_SLL:
        def __init__(self, max_size): # O(1)
            self.max_size = max_size
            self.stack = LIBRARY.SINGLE_LINKED_LIST()

        # function to add data to the top of back of the stack
        def push(self, data): # O(n)
            if not (self.isFull()):
                # add data to the back of the list
                self.stack.insert(data)

        # function to take data from the top of the stack
        def pop(self): # O(n)
            if not (self.isEmpty()):
                # get the data at the back of the list and remove it
                i = self.stack.length() - 1
                popped = self.stack.read(i)
                self.stack.delete(i)
                return popped
            return None

        # function to check if the list is empty
        def isEmpty(self): # O(n)
            return (self.stack.root is None)

        # function to check if the list is full
        def isFull(self): # O(n)
            return (self.stack.length() == self.max_size)

        # function to check the data at the top of the stack without deleting it
        def peek(self): # O(n)
            return (self.stack.read(self.stack.length() - 1))



















    # binary search tree
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

        '''print and search functions have O(n) time complexity'''

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

        # function to search for a key in pre order
        def search_pre_order(self, key, root = 0):
            # checks if its the first run of the function
            if root == 0:
                root = self.root
            # if current root exists
            if root:
                # key found
                if (key == root.key):
                    return root.data
                # check to the left
                elif key < root.key and root.left:
                    return self.search_pre_order(key, root.left)
                # check to the right
                elif key > root.key and root.right:
                    return self.search_pre_order(key, root.right)
                else:
                    return None
            return None
    
        # function to search for a key in in order
        def print_in_order(self, key, root = 0):
            # checks if its the first run of the function
            if root == 0:
                root = self.root
            # if current root exists
            if root:
                # check to the left
                if key < root.key and root.left:
                    return self.search_pre_order(key, root.left)
                # key found
                elif (key == root.key):
                    return root.data
                # check to the right
                elif key > root.key and root.right:
                    return self.search_pre_order(key, root.right)
                else:
                    return None
    
        # function to search for a key in post order
        def print_post_order(self, key, root = 0):
            # checks if its the first run of the function
            if root == 0:
                root = self.root
            # if current root exists
            if root:
                # check to the left
                if key < root.key and root.left:
                    return self.search_pre_order(key, root.left)
                # check to the right
                elif key > root.key and root.right:
                    return self.search_pre_order(key, root.right)
                # key found
                elif (key == root.key):
                    return root.data
                else:
                    return None





















    ''' bfs and dfs '''

    # function to get the shortest path in a graph from a start and goal
    def bfs_shortest_path(graph, start, goal):
        # Check if the start and goal nodes are valid
        if start not in graph or goal not in graph:
        # error
            print("Start or goal node not in the graph")
        # using a list as a queue to perform BFS
        # queue def
        queue = [(start, [start])]
        # save visited nodes
        visited = set()
        while queue:
            # current node def and current path def
            cn, path = queue.pop(0)
            # base case
            if cn == goal:
                return path  # Return the shortest path
            # if the current node is not in the visited set add it to the set
            if cn not in visited:
                visited.add(cn)
                # add neighbor nodes to the queue
                for neighbor in graph[cn]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None

    def dfs(self, x, y, path, end, maze):
        # base case of path not working
        if x == end[0] and y == end[1]:
            return path + [(x, y)]
        # if in a valid position
        if valid(x, y, maze):
            maze[x][y] = -1  # mark the current cell as visited
            # try moving in different directions (up, down, left, right)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # split into multiple paths
                new_path = self.dfs(new_x, new_y, path + [(x, y)], end, maze)
                if new_path:
                    return new_path
            maze[x][y] = 0  # Unmark the cell if no valid path is found
        return None
    
    # function to call the recursive function that solve the maze
    def solve_maze(self, maze, start, end):
        s_x, s_y = start
        solution = self.dfs(s_x, s_y, [], end, maze)
        return solution





















    # linear search function via iteration for arrays
    def linear_search_arr_iterative(element, array): # O(n)
        # check each indexes element using a for loop
        for i in range(len(array)):
            if (array[i] == element):
                return i
        return -1
    
    # linear search function via recursion for arrays
    def linear_search_arr_recurisve(self, element, array, index = 0): # O(n)
        # case for out of bounds
        if (index >= len(array)):
            return -1
        # case for found element index
        if (element == array[index]):
            return index
        # base case
        index += 1
        return self.linear_search_arr_recurisve(element, array, index)

    # linear search function via iteration for lists
    def linear_search_ll_iterative(self, element, linked_list): # O(n)
        cn = linked_list.root
        index = 0
        # loop through each node until data is found
        while cn:
            if (cn.data == element):
                return index
            index += 1
            cn = cn.next
        # return the number of nodes passed
        return -1
    
    # linear search function via recursion for lists
    def linear_search_ll_recursive(self, element, linked_list, index = 0): # O(n)
        # case for first run to properly setup root
        if (index == 0):
            linked_list = linked_list.root
        # case for nodes still in list
        if linked_list:
            # case for found elements node
            if (linked_list.data == element):
                # return nodes passed
                return index
            # base case for recursion
            return self.linear_search_ll_recursive(element, linked_list.next, index + 1)
        # case for none found
        return -1
    
    # binary search function via iteration for arrays
    def binary_search_arr_iterative(self, element, array): # O(log(n))
        # setup search bounds
        low = 0
        high = len(array) - 1
        # while in bounds
        while (low <= high):
            # find mid
            mid = low + (high - low) // 2
            # element found
            if (array[mid] == element):
                return mid
            # mid is less than element
            elif (array[mid] < element):
                low = mid + 1
            # mid is greater than element
            else:
                high = mid - 1
        # no element found
        return -1
    
    # binary search function via recursion for arrays
    def binary_search_arr_recursive(self, element, array, low = None, high = None): # O(log(n))
        # setup search bounds on first run of function
        if (low is None):
            low = 0
        if (high is None):
            high = len(array)
        # case for out of bounds / no element found
        if (low > high):
            return -1
        # find mid
        mid = low + (high - low) // 2
        # element found
        if (array[mid] == element):
            return mid
        # mid is less than element
        elif (array[mid] < element):
            low = mid + 1
        # mid is greater than element
        else:
            high = mid - 1
        return self.binary_search_arr_recursive(element, array, low, high)





















    # selection sort for arrays
    def selection_sort_arr(self, array): # O(n^2)
        n = len(array)
        for i in range(n - 1):
            # find the index of the min element in the unsorted part
            min_index = i
            for j in range(i + 1, n):
                if (array[j] < array[min_index]):
                    min_index = j
            # swap the found min element with the first element
            array[i], array[min_index] = array[min_index], array[i]
        return array

    # selection sort for lists
    def selection_sort_ll(self, linked_list): # O(n^2)
        cn = linked_list.root # copy of the list
        # loops through each node in the list
        while (cn is not None):
            min_node = cn
            rn  = cn.next # copy of the next node
            # loops through the nodes in the list above (cn) or the current node
            # after the loop min_node is the node with the smallest data above the cn node
            while (rn is not None):
                # checks if the rn's data is less than the cn's / min data
                if rn.data < min_node.data:
                    min_node = rn
                rn = rn.next
            # swap the cn node and the node with the smallest data above it
            cn.data, min_node.data = min_node.data, cn.data
            cn = cn.next
        return linked_list
    
    # insertion sort for arrays
    def insertion_sort_arr(self, array): # O(n^2)
        # loop through each element after the first in an array
        for i in range(1, len(array)):
            # save the current element
            element = array[i]
            j = i - 1
            # while loop to loop backwards through the array until
            # count (j) equals 0 / the count is at the begininng of the array
            # or the saved element is less than the current element
            while (j >= 0 and element < array[j]):
                # move current element to the right
                array[j + 1] = array[j]
                # move what element is being searched to the left
                j -= 1
            # assign the saved element once its proper place is found (right of j)
            array[j + 1] = element
        return array

    # insertion sort for lists
    def insertion_sort_ll(self, linked_list): # O(n^2)
        # case for non proper list passed
        if not (linked_list.root) or not (linked_list.root.next):
            return linked_list
        # def sorted root
        sorted_root = None
        cn = linked_list.root # copy of list
        while cn:
            # next node def
            nn = cn.next
            # insert the current node into the sorted part
            # case for not sorted data
            if not (sorted_root) or (cn.data < sorted_root.data):
                cn.next = sorted_root
                sorted_root = cn
            else: # else sort
                sorted_cn = sorted_root
                # nested for sorting
                while (sorted_cn.next) and (sorted_cn.next.data < cn.data):
                    sorted_cn = sorted_cn.next
                cn.next = sorted_cn.next
                sorted_cn.next = cn
            cn = nn
        linked_list.root = sorted_root
        # return final list
        return linked_list

    # quick sort for arrays
    def quick_sort_arr(self, array): # O(n*log(n))
        # case for non proper array
        if (len(array) <= 1):
            return array
        # find mid
        pivot = array[len(array) // 2]
        # create temp arrays
        left = [x for x in array if x < pivot]
        mid = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        # continue recursion
        return self.quick_sort_arr(left) + mid + self.quick_sort_arr(right)

    # quick sort for lists
    def quick_sort_ll(self, linked_list): # O(n*log(n))
        # get end node
        end = linked_list.root
        while (end.next != None):
            end = end.next
        # start quick sort via helper function
        out = self.__helper_quick_sort_ll_sort__(linked_list.root, end)
        # if proper output
        if out:
            return out
        # if output is None return input
        return linked_list
    
    # helper function for quick sort
    # function to sort post partition of list
    def __helper_quick_sort_ll_sort__(self, start, end):
        # inproper passed start and end
        if (start == None or start == end or start == end.next):
            return None
        # split list and partition
        pivot_prev = self.__helper_quick_sort_ll_partition__(start, end)
        self.__helper_quick_sort_ll_sort__(start, pivot_prev)
        # if pivot prev is equal to start start sort at start
        if (pivot_prev != None and pivot_prev == start):
            self.__helper_quick_sort_ll_sort__(pivot_prev.next, end)
        # pivot prev is not None or start start sort at start.next
        elif (pivot_prev != None and pivot_prev.next != None):
            self.__helper_quick_sort_ll_sort__(pivot_prev.next.next, end)

    # helper function for quick sort
    # function to determine the partions point
    def __helper_quick_sort_ll_partition__(self, start, end): # O(n)
        if (start == end or start == None or end == None):
            return start
        pivot_prev = start
        cn = start
        pivot = end.data
        # loop until 1 before the end
        while (start != end):
            if (start.data < pivot):
                # keep track of last modified item
                pivot_prev = cn
                temp = cn.data
                cn.data = start.data
                start.data = temp
                cn = cn.next
            start = start.next
        # swap position of current (cn) and pivot
        temp = cn.data
        cn.data = pivot
        end.data = temp
        # return the prev pivot as its swapped
        return pivot_prev 

    # merge sort function for arrays
    def merge_sort_arr(self, array): # O(n*log(n))
        # check that the length is greater than 1
        if (len(array) > 1):
            # get the mid point in the array
            mid = len(array)//2
            # divide into its left and right parts
            l_arr = array[:mid]
            r_arr = array[mid:]
            # recursive sort for each half
            self.merge_sort_arr(l_arr)
            self.merge_sort_arr(r_arr)
            i = 0 # variables for the following loops
            j = 0
            k = 0
            # loop through left and right sides
            while (i < len(l_arr) and j < len(r_arr)):
                #if the left side is less than right side
                if (l_arr[i] <= r_arr[j]):
                    array[k] = l_arr[i]
                    i += 1
                else:
                    # if the right side is less than right side
                    array[k] = r_arr[j]
                    j += 1
                k += 1
            # make sure that all indexs were checked
            while (i < len(l_arr)):
                array[k] = l_arr[i]
                i += 1
                k += 1
            while (j < len(r_arr)):
                array[k] = r_arr[j]
                j += 1
                k += 1
        return array

    # merge sort function for lists
    def merge_sort_ll(self, linked_list): # O(n*log(n))
        # start recursive helper function
        return self.__helper_merge_sort_ll_merge_sort__(linked_list.root)
    
    # helper function for merge sort
    # function to properly merge nodes
    def __helper_merge_sort_ll_sorted_merge__(self, anode, bnode):
        result = None
        # base case
        if (anode == None):
            return bnode
        if (bnode == None):
            return anode
        # pick node for recursion
        if (anode.data <= bnode.data):
            result = anode
            result.next = self.__helper_merge_sort_ll_sorted_merge__(anode.next, bnode)
        else:
            result = bnode
            result.next = self.__helper_merge_sort_ll_sorted_merge__(anode, bnode.next)
        return result
    
    # helper function for merge sort
    # recursive function for merge sorting a list
    def __helper_merge_sort_ll_merge_sort__(self, root):
        # base case if head is none
        if (root == None) or (root.next == None):
            return root
        # get the mid of the list
        mid = self.__helper_merge_sort_ll_get_mid__(root)
        mid_next = mid.next
        # set the mid next to none
        mid.next = None
        # mergeSort left
        left = self.__helper_merge_sort_ll_merge_sort__(root)
        # mergesort on right
        right = self.__helper_merge_sort_ll_merge_sort__(mid_next)
        # merge
        sorted_list = self.__helper_merge_sort_ll_sorted_merge__(left, right)
        return sorted_list
    
    # helper function for merge sort
    # function to get mid node
    def __helper_merge_sort_ll_get_mid__(self, root): # O(n)
        if (root == None):
            return root
        # define 2 coppies of the root
        slow = root
        fast = root
        while (fast.next != None and fast.next.next != None):
            # fast node moves through the list at twice the speed
            # so the the slow is then the mid
            slow = slow.next
            fast = fast.next.next
        return slow





















    # function to print a linked list to the terminal
    # note that this requires a SINGLE_LINKED_LIST() obj
    def print_ll(self, linked_list): # O(n)
        cn = linked_list.root
        while cn:
            print(cn.data)
            cn = cn.next
    
    # function to print a linked list to the terminal
    # note that this requires a root of a linked list obj
    def print_ll_from_root(self, root): # O(n)
        while root:
            print(root.data)
            root = root.next