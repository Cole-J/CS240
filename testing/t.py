
import heapq

class SearchableHeap:
    def __init__(self):
        self.heap = []
        self.index_map = {}

    def push(self, item):
        heapq.heappush(self.heap, item)
        self.index_map[item] = len(self.heap) - 1

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        item = self.heap[0]
        del self.index_map[item]
        heapq.heappop(self.heap)
        return item

    def remove(self, item):
        idx = self.index_map.get(item)
        if idx is not None:
            self._remove_at(idx)

    def _remove_at(self, idx):
        last_item = self.heap.pop()
        if idx < len(self.heap):
            self.heap[idx] = last_item
            self.index_map[last_item] = idx
            heapq._siftup(self.heap, idx)
            heapq._siftdown(self.heap, 0, idx)

    def search(self, item):
        return item in self.index_map

    def sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.pop())
        return sorted_list

# Example usage:
heap = SearchableHeap()
heap.push(5)
heap.push(2)
heap.push(9)
heap.push(3)

print("Heap:", heap.heap)  # Output: [2, 3, 9, 5]

print("Searching for 3:", heap.search(3))  # Output: True
print("Searching for 7:", heap.search(7))  # Output: False

print("Sorted list:", heap.sort())  # Output: [2, 3, 5, 9]