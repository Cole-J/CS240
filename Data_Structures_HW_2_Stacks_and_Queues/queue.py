'''
Cole Johnson
For CS240
'''
# a class for creating a queue using arrays
class queue_array:
    def __init__(self, max_size):
        self.max_size = max_size # setting the max size of the array
        self.queue = [] # creating the queue array

    # function to add data to the front of the queue
    def enqueue(self, data):
        # if array is not full add data to the front of the array
        if not (self.isFull()):
            self.queue.insert(0, data)

    # function to pop the data from the back of the queue
    def dequeue(self):
        # is array is not empty pop and return data from the back of the array
        if not (self.isEmpty()):
            return self.queue.pop()

    # check if queue is empty
    # returns bool
    def isEmpty(self):
        return len(self.queue) == 0

    # check if queue is full
    # returns bool
    def isFull(self):
        return len(self.queue) == self.max_size

    # returns the back queue data without popping it
    def peek(self):
        return self.queue[len(self.queue)]

# get the dll from the dll method
from Double_Linked_List import double_linked_list
# class for creating a queue with a dll
class queue_double_linked_list:
    def __init__(self, max_size):
        self.max_size = max_size # setting max size
        self.queue = double_linked_list() # creating the dll object

    # function to add data to the back of the queue
    def enqueue(self, data):
        if not (self.isFull()):
            self.queue.insert(data)

    # function to pop data from the front of the queue
    def dequeue(self):
        if not (self.isEmpty()):
            dequeued = self.queue.read(0)
            self.queue.delete(0)
            return dequeued
        else:
            return None

    # checks if the dll is empty
    # returns a bool
    def isEmpty(self):
        return self.queue.first_node is None

    # checks if the dll is full
    # returns a bool
    def isFull(self):
        return self.queue.length() == self.max_size

    # gets the data from the back of the queue without popping it
    def peek(self):
        if not (self.isEmpty()):
            return self.queue.read(self.queue.length() - 1)
        else:
            return None

'''
note that the array version adds to the front and pulls from the back
while the dll version adds to the back and pulls from the front
'''

queue_size = 5

qa = queue_array(queue_size)
qa.enqueue(1)
qa.enqueue(2)
qa.enqueue(3)
qa.enqueue(4)
qa.enqueue(5)
qa.enqueue(6)

print("with arrays")
while not qa.isEmpty():
    print(qa.dequeue())
print()
    
    
ql = queue_double_linked_list(queue_size)
ql.enqueue(1)
ql.enqueue(2)
ql.enqueue(3)
ql.enqueue(4)
ql.enqueue(5)
ql.enqueue(6)

print("with lists")
while not ql.isEmpty():
    print(ql.dequeue())
print()