'''
Cole Johnson
For CS240
'''
# a class for creating a stack with arrays
class stack_array:
    def __init__(self, max_size):
        self.max_size = max_size # sets the max size
        self.stack = [] # creates the stack array

    # function to add data to the back of the stack
    def push(self, data):
        if not (self.isFull()):
            self.stack.append(data)

    # function to pop the data from the back of the stack
    def pop(self):
        return self.stack.pop()

    # checks if the stack is empty
    # returns a bool
    def isEmpty(self):
        return len(self.stack) == 0

    # checks if the stack is full
    # returns a bool
    def isFull(self):
        return len(self.stack) == self.max_size

    # gets the top value in the array without popping it
    def peek(self):
        return self.stack[len(self.stack - 1)]

# get the ll from the ll method
from Single_Linked_List import linked_list
# a class to create a stack with ll object
class stack_linked_list:
    def __init__(self, max_size):
        self.max_size = max_size # setting max size
        self.stack = linked_list() # creates the stack with ll object

    # function to add data to the back of the stack
    def push(self, data):
        if not (self.isFull()):
            self.stack.insert(data)

    # function to pop data from the back of the stack
    def pop(self):
        # if stack is not empty delete and return the last value
        if not (self.isEmpty()):
            i = self.stack.length() - 1
            popped = self.stack.read(i)
            self.stack.delete(i)
            return popped
        else:
            return None

    # function to check if stack is empty
    def isEmpty(self):
        return self.stack.first_node is None

    # function to check if stack is full
    def isFull(self):
        return self.stack.length() == self.max_size

    # function to get data from the top of the stack without popping it
    def peek(self):
        return self.stack.read(self.stack.length() - 1)