'''
Cole Johnson 2/15
For CS240 Midterm
'''
# import library
from library import LIBRARY
l = LIBRARY()
# uncomment what you want to test

# arrays for search and sort functions
array_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [4, 12, 5, 45, 12, 4, 32, 645, 23]
# slls for search and sort functions
ll_sorted = l.SINGLE_LINKED_LIST()
ll_sorted.insert(0)
ll_sorted.insert(1)
ll_sorted.insert(2)
ll_sorted.insert(3)
ll_sorted.insert(4)
ll = l.SINGLE_LINKED_LIST()
ll.insert(4)
ll.insert(42)
ll.insert(124)
ll.insert(10)
ll.insert(3)

#print("DATA STRUCTURES")

#print("single linked list")
'''
sll = l.SINGLE_LINKED_LIST()
sll.insert(0)
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(1, 0)
sll.insert(3, 5)
sll.insert(8)
sll.delete(4)
print(sll.length())
for i in range(sll.length()):
    print(sll.read(i))
'''

#print("double linked list")
'''
dll = l.DOUBLE_LINKED_LIST()
dll.insert(0)
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(1, 0)
dll.insert(3, 5)
dll.insert(8)
dll.delete(4)
print(dll.length())
for i in range(dll.length()):
    print(dll.read(i))
'''

#print("stack array")
'''
stack = l.STACK_ARR(3)
print(stack.isEmpty())
print(stack.isFull())
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.isEmpty())
print(stack.isFull())
print(stack.peek())
while not (stack.isEmpty()):
    print(stack.pop())
'''

#print("stack sll")
'''
stack = l.STACK_SLL(3)
#print(stack.isEmpty())
#print(stack.isFull())
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
#print(stack.stack.length())
#print(stack.isEmpty())
#print(stack.isFull())
print(stack.peek())
while not (stack.isEmpty()):
    print(stack.pop())
'''

#print("queue array")
'''
q = l.QUEUE_ARR(3)
#print(q.isEmpty())
#print(q.isFull())
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
#print(len(q.queue))
#print(q.isEmpty())
#print(q.isFull())
#print(q.peek())
while not (q.isEmpty()):
    print(q.dequeue())
'''

#print("stack dll")
'''
q = l.QUEUE_DLL(3)
#print(q.isEmpty())
#print(q.isFull())
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
#print(q.isEmpty())
#print(q.isFull())
#print(q.queue.length())
#print(q.peek())
while not (q.isEmpty()):
    print(q.dequeue())
'''

#print("search functions")
#element = 124 # element variable to test search functions

#print("linear search array iterative")
#print(l.linear_search_arr_iterative(element, array_sorted)) # tested
#print(l.linear_search_arr_iterative(element, array)) # tested

#print("linear search sll iterative")
#print(l.linear_search_ll_iterative(element, ll_sorted)) # tested
#print(l.linear_search_ll_iterative(element, ll)) # tested

#print("linear search array recursive")
#print(l.linear_search_arr_recurisve(element, array_sorted, 0)) # tested
#print(l.linear_search_arr_recurisve(element, array)) # tested

#print("linear search sll recursive")
#print(l.linear_search_ll_recursive(element, ll_sorted)) # tested
#print(l.linear_search_ll_recursive(element, ll)) # tested

#print("binary search iterative")
#print(l.binary_search_arr_iterative(element, array_sorted)) # tested
#print("binary search recursive")
#print(l.binary_search_arr_recursive(element, array_sorted)) # tested

#print("sorting functions")

#print("selection sort array")
#print(l.selection_sort_arr(array)) # tested
#print("selection sort ll")
#l.print_ll(l.selection_sort_ll(ll)) # tested

#print("insertion sort array")
#print(l.insertion_sort_arr(array)) # tested
#print("insertion sort ll")
#l.print_ll(l.insertion_sort_ll(ll)) # tested

#print("quick sort array")
#print(l.quick_sort_arr(array)) # tested


#print("quick sort ll")
#l.print_ll(l.quick_sort_ll(ll)) # tested

#print("merge sort array")
#print(l.merge_sort_arr(array)) # tested
#print("merge sort ll")
#l.print_ll_from_root(l.merge_sort_ll(ll)) # tested