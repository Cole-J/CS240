'''
from enum import Enum
type = Enum('type', ['min_heap', 'max_heap'])
class Node:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f"data {self.data}"
class HEAP:
    def __init__(self, arr, heap_type):
        self.arr = arr
        self.type = heap_type
        self.root = Node(min(arr))
        arr.remove(min(arr))
        cn = self.root
        while arr:
            pass
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
heap = HEAP(arr, type.min_heap)
print(heap.type)
'''
'''
from enum import Enum

type = Enum('type', ['min_heap', 'max_heap'])

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"data {self.data}"

class HEAP:
    def __init__(self, arr, heap_type):
        self.arr = arr
        self.type = heap_type
        if self.type == 'min_heap':
            self.root = self.build_min_heap()
        elif self.type == 'max_heap':
            self.root == self.build_max_heap()
        else:
            self.root = None

    def build_min_heap(self):
        pass
    def __build_min__(self):
        pass
    def build_max_heap(self):
        pass
    def __build_max__(self):
        pass
    def search(self, value):
        return self.arr

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
heap = HEAP(arr, type.min_heap)

# Searching
print(heap.search(0))
'''

from enum import Enum
type = Enum('type', ['min_heap', 'max_heap'])

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"data {self.data}"

class HEAP:
    def __init__(self, arr, heap_type):
        self.arr = arr
        self.type = heap_type

    def __generate_root_r__(self, root, arr):
        pass

    def __get_min_max__(self, arr, heap_type):
        if heap_type == 'min_heap':
            pass
        elif heap_type == 'max_heap':
            pass