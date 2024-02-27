class SearchableHeap:
    def __init__(self):
        self.heap = []
        self.index_map = {}

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        item = self.heap[0]
        del self.index_map[item]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
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
            self._heapify_down(idx)
            self._heapify_up(idx)

    def search(self, item):
        return item in self.index_map

    def sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.pop())
        return sorted_list

    def _heapify_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent_idx]:
                self._swap(idx, parent_idx)
                idx = parent_idx
            else:
                break

    def _heapify_down(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            min_idx = idx

            if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[min_idx]:
                min_idx = left_child_idx

            if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[min_idx]:
                min_idx = right_child_idx

            if min_idx != idx:
                self._swap(idx, min_idx)
                idx = min_idx
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i]], self.index_map[self.heap[j]] = i, j


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