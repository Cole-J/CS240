'''
Cole Johnson 2/27
For CS240
'''
# heap is in the array with sorted indexs
# rules for the heap

# left child is 2i + 1
# right child is 2i + 2
# parent is (i-1)//2
# root is at index 0

class BHEAP:
    # defualts to min heap
    def __init__(self, is_min = True):
        self.heap = []
        self.is_min = is_min

    # push data to the heap and then sort the heap properly when the value is added
    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        # case for nothing in the heap
        if not self.heap:
            return None
        # case for 1 value in the heap
        if len(self.heap) == 1:
            return self.heap.pop()
        # remove data from heap
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # sort the heap properly once the value is deleted
        self._heapify_down()
        return root

    # delete indexes in the heap and copy to a sorted temp heap
    # return the temp heap
    def sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.pop())
        return sorted_list

    # checks if a value is in the heap
    def search(self, value):
        return value in self.heap

    # checks that all elements parents / children are in the heap array and changes index when needed
    # specifically for when a value is added
    def _heapify_up(self):
        current_index = len(self.heap) - 1
        # for each index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if ((self.is_min and self.heap[current_index] < self.heap[parent_index])
                or (not self.is_min and self.heap[current_index] > self.heap[parent_index])):
                # swap when needed
                self.heap[current_index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[current_index],
                )
                current_index = parent_index
            # else everything is sorted
            else:
                break

    # checks that all elements parents / children are in the heap array and changes index when needed
    # specifically for when a value is deleted
    def _heapify_down(self):
        current_index = 0
        while True:
            # current indexes
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            extreme = current_index
            # check left child
            if (left_child_index < len(self.heap)and ((self.is_min and self.heap[left_child_index] < self.heap[extreme])
                    or (not self.is_min and self.heap[left_child_index] > self.heap[extreme]))):
                extreme = left_child_index
            # check right child
            if (right_child_index < len(self.heap)and ((self.is_min and self.heap[right_child_index] < self.heap[extreme])
                    or (not self.is_min and self.heap[right_child_index] > self.heap[extreme]))):
                extreme = right_child_index
            # does not match so swap
            if extreme != current_index:
                self.heap[current_index], self.heap[extreme] = (
                    self.heap[extreme],
                    self.heap[current_index],
                )
                current_index = extreme
            else:
                break

min = BHEAP()
min.push(3)
min.push(1)
min.push(4)
min.push(2)
print("Min Heap Sorted:", min.sort())

max = BHEAP(False)
max.push(3)
max.push(1)
max.push(4)
max.push(2)
print("Max Heap Sorted:", max.sort())